from typing import List, Literal, Optional

from pydantic import BaseModel


class ContentRequest(BaseModel):
    """
    Structured content brief received from the frontend or API client.
    """

    content_type: Literal[
        "blog_post",
        "landing_page",
        "social_post",
        "ad_copy",
        "product_description",
    ]

    goal: Optional[str] = None
    target_audience: Optional[str] = None
    product_info: Optional[str] = None
    what_it_does: Optional[str] = None
    main_benefits: Optional[str] = None
    usp: Optional[str] = None

    tone_of_voice: str = "professional"
    language: str = "en"
    length: Literal["short", "medium", "long"] = "medium"

    keywords: Optional[List[str]] = None
    platform: Optional[str] = None
    constraints: Optional[str] = None


class ContentMetadata(BaseModel):
    keywords_used: Optional[List[str]] = None
    word_count: Optional[int] = None
    estimated_reading_time_minutes: Optional[int] = None
    tone_used: Optional[str] = None


class ContentResponse(BaseModel):
    """
    Structured response returned after AI content generation.
    """

    title: str
    subtitle: str
    summary: str
    outline: List[str]
    body: str
    conclusion: str
    meta_description: Optional[str] = None
    metadata: Optional[ContentMetadata] = None
