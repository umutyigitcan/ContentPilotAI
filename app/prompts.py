from app.schemas import ContentRequest


def build_system_message() -> str:
    """
    Build the system prompt that forces the model to return structured JSON.
    """
    return (
        "You are ContentPilotAI, a senior marketing copywriter AI that generates high-quality, "
        "conversion-focused content based on a structured brief.\n\n"
        "You MUST respond ONLY with valid JSON. Do not include explanations, markdown, or code fences.\n"
        "Use the following exact JSON schema:\n\n"
        "{\n"
        '  "title": "string",\n'
        '  "subtitle": "string",\n'
        '  "summary": "string",\n'
        '  "outline": ["string", "..."],\n'
        '  "body": "string",\n'
        '  "conclusion": "string",\n'
        '  "meta_description": "string",\n'
        '  "metadata": {\n'
        '    "keywords_used": ["string", "..."],\n'
        '    "word_count": 123,\n'
        '    "estimated_reading_time_minutes": 3,\n'
        '    "tone_used": "string"\n'
        "  }\n"
        "}\n\n"
        "The JSON must be syntactically valid and directly parsable by Python json.loads()."
    )


def build_user_message(req: ContentRequest) -> str:
    """
    Convert a structured content brief into a clear prompt for the model.
    """
    keywords = ", ".join(req.keywords) if req.keywords else "None"

    return (
        "Use the following brief to generate the content:\n\n"
        f"Content type: {req.content_type}\n"
        f"Goal: {req.goal}\n"
        f"Target audience: {req.target_audience}\n"
        f"Product or service info: {req.product_info}\n"
        f"What it does: {req.what_it_does}\n"
        f"Main benefits: {req.main_benefits}\n"
        f"Unique selling proposition: {req.usp}\n"
        f"Tone of voice: {req.tone_of_voice}\n"
        f"Language: {req.language}\n"
        f"Length: {req.length}\n"
        f"Requested keywords: {keywords}\n"
        f"Platform: {req.platform}\n"
        f"Constraints or things to avoid: {req.constraints}\n"
    )
