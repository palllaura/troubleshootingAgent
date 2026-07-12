import logging

from backend.models.validation_result import ValidationResult

logger = logging.getLogger(__name__)


def validate_message(message: str) -> ValidationResult:
    logger.info("Validating user message.")

    if not message.strip():
        logger.warning("Validation failed: empty message.")
        return ValidationResult(
            valid=False,
            message="Please describe your problem."
        )

    if len(message) < 3:
        logger.warning("Validation failed: message too short.")
        return ValidationResult(
            valid=False,
            message="Could you provide a little more detail?"
        )

    if len(message) > 1000:
        logger.warning("Validation failed: message too long.")
        return ValidationResult(
            valid=False,
            message="Your message is too long."
        )

    logger.info("Message validation successful.")

    return ValidationResult(valid=True)