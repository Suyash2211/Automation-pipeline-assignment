import os
import json
import logging

from scripts.extract_demo_data import extract_account_data
from scripts.generate_agent_spec import generate_agent_spec
from scripts.onboarding_update import update_account
from scripts.changelog import create_changelog
from scripts.utils import save_json




os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Pipeline started")


DEMO_FOLDER = "dataset/demo_calls"
ONBOARD_FOLDER = "dataset/onboarding_calls"
ACCOUNTS_FOLDER = "outputs/accounts"

os.makedirs(ACCOUNTS_FOLDER, exist_ok=True)



summary = {
    "accounts_processed": 0,
    "v1_generated": 0,
    "v2_generated": 0,
    "errors": 0
}


try:
    for file in os.listdir(DEMO_FOLDER):

        path = os.path.join(DEMO_FOLDER, file)

        with open(path) as f:
            transcript = f.read()

        account = extract_account_data(transcript)

        agent = generate_agent_spec(account)

        account_id = account["account_id"]

        base_path = f"{ACCOUNTS_FOLDER}/{account_id}/v1"

        account_path = f"{base_path}/account_memo.json"
        agent_path = f"{base_path}/agent_spec.json"

        save_json(account, account_path)
        save_json(agent, agent_path)

        logging.info(f"Account created: {account_id}")
        print("Account created:", account_id)

        summary["accounts_processed"] += 1
        summary["v1_generated"] += 1

except Exception as e:
    logging.error(f"Error in demo pipeline: {e}")
    summary["errors"] += 1



try:
    for file in os.listdir(ONBOARD_FOLDER):

        path = os.path.join(ONBOARD_FOLDER, file)

        with open(path) as f:
            onboarding_text = f.read()

        accounts = os.listdir(ACCOUNTS_FOLDER)

        if not accounts:
            continue

        latest_account = sorted(accounts)[-1]

        v1_account_path = f"{ACCOUNTS_FOLDER}/{latest_account}/v1/account_memo.json"

        with open(v1_account_path) as f:
            old_account = json.load(f)

        updated_account = update_account(old_account, onboarding_text)

        agent_v2 = generate_agent_spec(updated_account)
        agent_v2["version"] = "v2"

        v2_base = f"{ACCOUNTS_FOLDER}/{latest_account}/v2"

        account_v2_path = f"{v2_base}/account_memo.json"
        agent_v2_path = f"{v2_base}/agent_spec.json"

        save_json(updated_account, account_v2_path)
        save_json(agent_v2, agent_v2_path)

        changes = create_changelog(old_account, updated_account)

        os.makedirs(v2_base, exist_ok=True)

        with open(f"{v2_base}/changes.md", "w") as f:
            f.write(changes)

        logging.info(f"Updated account to v2: {latest_account}")
        print("Updated account to v2:", latest_account)

        summary["v2_generated"] += 1

except Exception as e:
    logging.error(f"Error in onboarding pipeline: {e}")
    summary["errors"] += 1




os.makedirs("outputs", exist_ok=True)

with open("outputs/run_summary.json", "w") as f:
    json.dump(summary, f, indent=2)

logging.info("Pipeline finished")
logging.info(f"Run summary: {summary}")

print("Pipeline finished.")
print("Run summary saved to outputs/run_summary.json")