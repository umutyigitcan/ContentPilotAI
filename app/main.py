from fastapi import FastAPI

from app.config import settings
from app.content_service import generate_structured_content
from app.schemas import ContentRequest, ContentResponse


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


@backend.post("/produce-content", response_model=ContentResponse)
async def produce_content(payload: ContentRequest):
    """
    Generate structured marketing content from a content brief.
    """
    return generate_structured_content(payload)
