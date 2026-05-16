from openai import OpenAI

from app.config import settings


def get_openai_client() -> OpenAI:
    """
    Create an OpenAI client using the configured API key.
    """
    settings.validate_openai_settings()

    return OpenAI(api_key=settings.openai_api_key)


def get_generation_model() -> str:
    """
    Return the configured model for content generation.
    """
    return settings.openai_model
