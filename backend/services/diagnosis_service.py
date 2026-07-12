import json
from validation_service import validate_message


def load_knowledge_base(filename):
    with open(filename, "r") as file:
        return json.load(file)


knowledge_base = load_knowledge_base(
    "backend/troubleshooting_knowledge_base.json"
)


def validate_issue(user_input):
    validation = validate_message(user_input)

    if not validation.valid:
        return {
            "response": validation.message
        }


def find_issue(user_input):
    for issue, details in knowledge_base.items():
        if details["symptom"].lower() in user_input.lower():
            return issue, details

    return None, None


def diagnose_issue(issue):
    if issue == "slow_internet":
        return (
            "Have you restarted your router? "
            "If not, please restart it and try again."
        )

    return None


def automate_fix(issue):
    if issue == "slow_internet":
        return "Network settings have been reset."

    return "Automation is not available for this issue."
