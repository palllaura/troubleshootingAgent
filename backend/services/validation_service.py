from backend.models.validation_result import ValidationResult


def validate_message(message: str) -> ValidationResult:

    if not message.strip():
        return ValidationResult(
            valid=False,
            message="Please describe your problem."
        )

    if len(message) < 3:
        return ValidationResult(
            valid=False,
            message="Could you provide a little more detail?"
        )

    if len(message) > 1000:
        return ValidationResult(
            valid=False,
            message="Your message is too long."
        )

    return ValidationResult(valid=True)
