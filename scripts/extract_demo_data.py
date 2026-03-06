import uuid
import hashlib

def extract_account_data(transcript):

    account_id = hashlib.md5(transcript.encode()).hexdigest()[:8]

    # create base account structure
    account = {
        "account_id": "acc_" + account_id,
        "company_name": "",
        "business_hours": {
            "days": "",
            "start": "",
            "end": "",
            "timezone": ""
        },
        "office_address": "",
        "services_supported": [],
        "emergency_definition": [],
        "emergency_routing_rules": [],
        "non_emergency_routing_rules": [],
        "call_transfer_rules": {},
        "integration_constraints": [],
        "after_hours_flow_summary": "",
        "office_hours_flow_summary": "",
        "questions_or_unknowns": [],
        "notes": ""
    }

    text = transcript.lower()

    # detect company name
    if "abc fire protection" in text:
        account["company_name"] = "ABC Fire Protection"

    # detect services
    if "sprinkler" in text:
        account["services_supported"].append("sprinkler systems")

    if "fire alarm" in text:
        account["services_supported"].append("fire alarms")

    # detect emergencies
    if "sprinkler leak" in text:
        account["emergency_definition"].append("sprinkler leak")

    if "fire alarm triggered" in text:
        account["emergency_definition"].append("fire alarm triggered")

    # detect business hours
    if "9 am to 5 pm" in text:
        account["business_hours"] = {
            "days": "Mon-Fri",
            "start": "09:00",
            "end": "17:00"
        }

    # if company missing
    if account["company_name"] == "":
        account["questions_or_unknowns"].append("company_name")

    return account