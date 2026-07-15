from backend.services.diagnosis_service import process_message


def test_process_valid_internet_issue():
    result = process_message("My internet is very slow.")

    assert result["success"] is True
    assert result["issue"] == "slow_internet"
    assert "router" in result["diagnostic"].lower()
    assert "network settings" in result["automation"].lower()


def test_process_password_issue():
    result = process_message("I forgot my password.")

    assert result["success"] is True
    assert result["issue"] == "forgot_password"
    assert result["solution"] is not None
    assert result["diagnostic"] is None
    assert result["automation"] is None


def test_unknown_issue():
    result = process_message("My cat ate my keyboard.")

    assert result["success"] is False
    assert result["message"] == (
        "I couldn't find a matching issue in my knowledge base."
    )


def test_empty_message():
    result = process_message("")

    assert result["success"] is False
    assert result["message"] == "Please describe your problem."


def test_short_message():
    result = process_message("Hi")

    assert result["success"] is False
    assert result["message"] == (
        "Could you provide a little more detail?"
    )


def test_long_message():
    result = process_message("A" * 1001)

    assert result["success"] is False
    assert result["message"] == "Your message is too long."
