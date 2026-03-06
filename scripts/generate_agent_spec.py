def generate_agent_spec(account):

    agent = {

        "agent_name": account["company_name"] + " Voice Agent",

        "voice_style": "professional and calm",

        "version": "v1",

        "variables": {
            "business_hours": account["business_hours"],
            "emergency_definition": account["emergency_definition"]
        },

        "call_transfer_protocol": "Transfer call to technician. If transfer fails inform caller a technician will call back.",

        "fallback_protocol": "If transfer fails collect caller details and assure quick follow-up.",

        "system_prompt": f"""
You are a voice assistant for {account['company_name']}.

BUSINESS HOURS FLOW
1 Greet the caller
2 Ask purpose of call
3 Collect caller name
4 Collect phone number
5 Route or transfer the call
6 If transfer fails explain next steps
7 Ask if they need anything else
8 Close the call politely

AFTER HOURS FLOW
1 Greet the caller
2 Ask if the situation is an emergency
3 If emergency collect name phone number and address immediately
4 Attempt transfer to technician
5 If transfer fails assure quick follow up
6 If not emergency collect details for next business day
7 Ask if anything else is needed
8 Close call politely
"""
    }

    return agent