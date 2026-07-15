import json
import logging

from backend.services.validation_service import validate_message

logger = logging.getLogger(__name__)


def _load_knowledge_base(filename: str) -> dict:
    """
    Load the troubleshooting knowledge base from a JSON file.
    """

    logger.info("Loading knowledge base from %s", filename)

    with open(filename, "r") as file:
        knowledge_base = json.load(file)

    logger.info("Loaded %d troubleshooting issues.", len(knowledge_base))

    return knowledge_base


knowledge_base = _load_knowledge_base(
    "backend/troubleshooting_knowledge_base.json"
)


def process_message(user_input: str) -> dict:
    """
    Process a user message and return a troubleshooting response.
    """

    logger.info("Processing user message.")

    validation = validate_message(user_input)

    if not validation.valid:
        logger.warning("Message validation failed.")

        return {
            "success": False,
            "message": validation.message
        }

    issue, details = _find_issue(user_input)

    if issue is None:
        logger.info("No matching issue found.")

        return {
            "success": False,
            "message": "I couldn't find a matching issue in my knowledge base."
        }

    logger.info("Matched issue: %s", issue)

    return {
        "success": True,
        "issue": issue,
        "solution": details["solution"],
        "diagnostic": _diagnose_issue(issue),
        "automation": _automate_fix(issue)
    }


def _find_issue(user_input: str):
    """
    Search the knowledge base for a matching issue.
    """

    logger.debug("Searching knowledge base.")

    for issue, details in knowledge_base.items():
        if details["symptom"].lower() in user_input.lower():
            return issue, details

    return None, None


def _diagnose_issue(issue: str):
    """
    Return additional troubleshooting guidance.
    """

    logger.debug("Running diagnostics for '%s'.", issue)

    if issue == "slow_internet":
        return (
            "Have you restarted your router? "
            "If not, please restart it and try again."
        )

    return None


def _automate_fix(issue: str):
    """
    Simulate an automated fix.
    """

    logger.debug("Attempting automated fix for '%s'.", issue)

    if issue == "slow_internet":
        return "Network settings have been reset."

    return None
