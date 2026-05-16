from fastapi import FastAPI

from app.config import settings


backend = FastAPI(
    title="ContentPilotAI API",
    version="1.0.0",
    description="Structured AI-powered content generation backend for ContentPilotAI.",
)


@backend.get("/")
def home():
    return {
        "message": "ContentPilotAI backend is running.",
        "model": settings.openai_model,
    }
