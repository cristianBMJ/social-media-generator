from fastapi import FastAPI

app = FastAPI(
    title="Social Media Content Generator",
    description="AI-powered social media content generation API",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Social Media Content Generator!"}