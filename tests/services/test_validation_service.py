from backend.services.validation_service import validate_message


def test_empty_message():
    result = validate_message("")
    assert result.valid is False
    assert result.message == "Please describe your problem."


def test_valid_message():
    result = validate_message("My printer isn't working.")
    assert result.valid is True


def test_short_message():
    result = validate_message("hi")
    assert result.valid is False


def test_long_message():
    result = validate_message("a" * 1001)
    assert result.valid is False

