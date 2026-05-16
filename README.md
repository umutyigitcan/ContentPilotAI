# ContentPilotAI

ContentPilotAI is a structured AI content generation backend built with FastAPI, OpenAI, and Pydantic.

It generates marketing content from structured briefs and returns clean JSON responses that can be used by web apps, dashboards, content tools, or automation workflows.

## Features

- Structured content brief input
- AI-powered marketing content generation
- Supports multiple content formats
- JSON-only model response design
- Pydantic request and response validation
- OpenAI model configuration through environment variables
- FastAPI endpoint for content generation
- CORS support for frontend integration
- Controlled error handling for LLM and validation failures

## Supported Content Types

- Blog posts
- Landing pages
- Social posts
- Ad copy
- Product descriptions

## Tech Stack

- Python
- FastAPI
- OpenAI API
- Pydantic
- Uvicorn
- python-dotenv

## Project Structure

ContentPilotAI/
  app/
    __init__.py
    main.py
    config.py
    schemas.py
    prompts.py
    ai_client.py
    content_service.py
  .env.example
  .gitignore
  requirements.txt
  README.md

## Setup

Clone the repository:

git clone https://github.com/umutyigitcan/ContentPilotAI.git
cd ContentPilotAI

Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Create a `.env` file:

cp .env.example .env

Fill in your environment variables:

OPENAI_API_KEY=
OPENAI_MODEL=gpt-4o-mini

## Running the API

Start the FastAPI server:

uvicorn app.main:backend --reload

The API will be available at:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs

## API Endpoints

### Health Check

GET /

Returns API status and configured model.

### Produce Content

POST /produce-content

Generates structured marketing content from a content brief.

Example request:

{
  "content_type": "landing_page",
  "goal": "Generate leads for an AI automation service",
  "target_audience": "Small e-commerce business owners",
  "product_info": "AI-powered customer support automation",
  "what_it_does": "Automates repetitive customer messages and support workflows",
  "main_benefits": "Saves time, improves response speed, reduces manual workload",
  "usp": "Fast setup and structured automation workflows",
  "tone_of_voice": "professional",
  "language": "en",
  "length": "medium",
  "keywords": ["AI automation", "customer support", "e-commerce"],
  "platform": "website",
  "constraints": "Avoid exaggerated claims"
}

Example response:

{
  "title": "AI Customer Support Automation for E-commerce Teams",
  "subtitle": "Respond faster, reduce repetitive work, and improve customer experience.",
  "summary": "A short overview of the generated content.",
  "outline": [
    "Problem",
    "Solution",
    "Benefits",
    "Call to action"
  ],
  "body": "Generated content body...",
  "conclusion": "Generated conclusion...",
  "meta_description": "SEO-friendly meta description.",
  "metadata": {
    "keywords_used": ["AI automation", "customer support"],
    "word_count": 350,
    "estimated_reading_time_minutes": 2,
    "tone_used": "professional"
  }
}

## Error Handling

The API returns controlled errors for:

- Missing OpenAI configuration
- Upstream LLM failures
- Invalid JSON returned by the model
- Response schema validation errors

## Security Notes

Do not commit real API keys, passwords, or `.env` files.

Use `.env.example` only as a configuration template.

## Status

ContentPilotAI is portfolio-ready and can be extended with authentication, database persistence, content history, and a frontend dashboard.
