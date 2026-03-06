def update_account(account, onboarding_text):

    text = onboarding_text.lower()

    updated_account = account.copy()

    if "24 hours" in text:
        updated_account["business_hours"] = {
            "days": "all",
            "start": "00:00",
            "end": "23:59",
            "timezone": "local"
        }

    if "servicetrade" in text:
        updated_account["integration_constraints"] = [
            "never create sprinkler jobs in ServiceTrade"
        ]

    if "emergency sprinkler" in text:
        updated_account["emergency_routing_rules"] = [
            "transfer immediately to technician"
        ]

    return updated_account