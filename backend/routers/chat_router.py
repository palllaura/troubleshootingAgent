import logging

from fastapi import APIRouter

from backend.services.diagnosis_service import process_message

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.get("/")
def chat_test():
    logger.info("Health check endpoint called.")

    return {
        "response": "Chat router is working!"
    }


@router.post("/")
def chat(message: str):
    logger.info("Received chat request.")

    return process_message(message)
