import tweepy
from dotenv import load_dotenv
import os

class TwitterAPI:
    def __init__(self):
        load_dotenv()
        
        api_key = os.getenv("TWITTER_API_KEY")
        api_secret = os.getenv("TWITTER_API_SECRET")
        access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        access_secret = os.getenv("TWITTER_ACCESS_SECRET")
        
        if not all([api_key, api_secret, access_token, access_secret]):
            raise ValueError("Missing Twitter API credentials in environment variables")
            
        auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
        self.client = tweepy.API(auth)

    def post(self, content: str) -> str:
        try:
            tweet = self.client.update_status(content)
            return tweet.id_str
        except tweepy.TweepError as e:
            raise Exception(f"Failed to post tweet: {str(e)}")