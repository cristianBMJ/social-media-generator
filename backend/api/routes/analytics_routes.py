@app.get("/analytics/{post_id}")
def get_analytics(post_id: str):
    stats = twitter.get_tweet_engagement(post_id)
    return {"post_id": post_id, "stats": stats}