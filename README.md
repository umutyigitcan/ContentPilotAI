# ContentPilotAI

ContentPilotAI is a structured AI content generation backend built with FastAPI, OpenAI, and Pydantic.

It generates marketing content from structured briefs and returns clean JSON responses that can be used by web apps, dashboards, or automation workflows.

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

## Local Development

Install dependencies:

pip install -r requirements.txt

Run the API:

uvicorn app.main:backend --reload

Health check:

GET /

## Environment Variables

Create a `.env` file based on `.env.example`.

Required variables:

OPENAI_API_KEY
OPENAI_MODEL

## Status

ContentPilotAI is currently under development.
