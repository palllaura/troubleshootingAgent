from fastapi import APIRouter

from backend.services.diagnosis_service import find_issue

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.get("/")
def chat_test():
    return {
        "response": "Chat router is working!"
    }


@router.post("/")
def chat(message: str):

    issue, details = find_issue(message)

    if issue is None:
        return {
            "response": "No matching issue found."
        }

    return {
        "response": details["solution"]
    }
