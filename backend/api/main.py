# from fastapi import FastAPI

# app = FastAPI(
#     title="Social Media Content Generator",
#     description="AI-powered social media content generation API",
#     version="0.1.0",
# )

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Social Media Content Generator!"}

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import APIKeyHeader
from backend.ml.inference import ContentGenerator
from backend.api.routes.post_routes import router as post_router

# Initialize FastAPI app
app = FastAPI(
    title="Social Media Content Generator",
    description="API for generating and posting social media content using AI",
    version="0.1.0",
)

# Include the post router
app.include_router(post_router)

# Initialize the content generator
generator = ContentGenerator()

# API Key Authentication
api_key_header = APIKeyHeader(name="X-API-Key")

async def validate_api_key(api_key: str = Depends(api_key_header)):
    """
    Validate the API key provided in the request header.

    Parameters:
    - api_key: The API key provided in the `X-API-Key` header.

    Raises:
    - HTTPException: If the API key is invalid.
    """
    if api_key != "your-secret-key":
        raise HTTPException(status_code=403, detail="Invalid API Key")

# Define the /generate endpoint with API key authentication
@app.post("/generate", dependencies=[Depends(validate_api_key)])
def generate_content(prompt: str, max_length: int = 100):
    """
    Generate social media content based on a prompt.

    Parameters:
    - prompt: The input text to generate content from.
    - max_length: The maximum length of the generated content (default: 100).

    Returns:
    - A JSON object containing the generated text.
    """
    return {"generated_text": generator.generate(prompt, max_length)}