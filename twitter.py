import requests
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session
import tweepy
import os
from os import path
import json

dir = os.path.dirname(__file__)
load_dotenv()

class Twitter:
    def __init__(self):
        self.consumer_key = os.environ['API_KEY']
        self.consumer_secret = os.environ['API_SECRET_KEY']
        self.access_token = os.environ['ACCESS_TOKEN']
        self.access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
    
    def setOAuth(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        return api
    
    def postTweet(self, payload):
        oauth = self.setOAuth()
        response = oauth.update_status(payload)
        if response:
            response_data = {
                "status": "success",
                "message": "Tweet posted successfully",
                "tweet_id": response.id_str,
                "tweet_text": response.text,
            }
        else:
            error_message = "Failed to post tweet"
            response_data = {
                "status": "error",
                "message": error_message,
            }
        return json.dumps(response_data)
    



