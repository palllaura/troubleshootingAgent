from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

from backend.routers.chat_router import router as chat_router
app = FastAPI()

# Serve the frontend files
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Register routers
app.include_router(chat_router)


@app.get("/")
def root():
    """Serve the chatbot interface."""
    return FileResponse("frontend/index.html")
