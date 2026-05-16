import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    """
    Runtime configuration for ContentPilotAI.
    """

    def __init__(self) -> None:
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.openai_model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    def validate_openai_settings(self) -> None:
        if not self.openai_api_key:
            raise RuntimeError("OPENAI_API_KEY is not set in environment variables.")


settings = Settings()
