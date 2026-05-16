import json

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.content_service import generate_structured_content
from app.schemas import ContentRequest, ContentResponse


backend = FastAPI(
    title="ContentPilotAI API",
    version="1.0.0",
    description="Structured AI-powered content generation backend for ContentPilotAI.",
)


backend.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
    try:
        return generate_structured_content(payload)

    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500,
            detail="Failed to parse model JSON response.",
        )

    except ValueError as error:
        raise HTTPException(
            status_code=500,
            detail=f"Response validation error: {str(error)}",
        )

    except Exception as error:
        raise HTTPException(
            status_code=502,
            detail=f"Upstream LLM error: {str(error)}",
        )
