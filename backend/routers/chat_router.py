from fastapi import APIRouter

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.get("/")
def chat_test():
    return {
        "response": "Chat router is working!"
    }
