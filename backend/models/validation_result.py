from pydantic import BaseModel


class ValidationResult(BaseModel):
    valid: bool
    message: str | None = None
