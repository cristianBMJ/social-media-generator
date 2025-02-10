from fastapi import APIRouter, HTTPException, Depends
from backend.api.utils.social_apis import TwitterAPI
from pydantic import BaseModel

router = APIRouter()
twitter = TwitterAPI()

class ContentRequest(BaseModel):
    content: str

@router.post("/post")
async def post_to_twitter(content_request: ContentRequest):
    try:
        tweet_id = twitter.post(content_request.content)
        return {"status": "success", "tweet_id": tweet_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))