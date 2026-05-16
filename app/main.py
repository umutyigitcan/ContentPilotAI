from fastapi import FastAPI


backend = FastAPI(
    title="ContentPilotAI API",
    version="1.0.0",
    description="Structured AI-powered content generation backend for ContentPilotAI.",
)


@backend.get("/")
def home():
    return {
        "message": "ContentPilotAI backend is running.",
    }
