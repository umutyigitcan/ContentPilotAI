from app.ai_client import get_generation_model, get_openai_client
from app.prompts import build_system_message, build_user_message
from app.schemas import ContentRequest


def generate_raw_content(payload: ContentRequest) -> str:
    """
    Generate raw content from OpenAI based on the structured content brief.
    """
    client = get_openai_client()

    completion = client.chat.completions.create(
        model=get_generation_model(),
        temperature=0.3,
        messages=[
            {"role": "system", "content": build_system_message()},
            {"role": "user", "content": build_user_message(payload)},
        ],
    )

    return completion.choices[0].message.content or ""
