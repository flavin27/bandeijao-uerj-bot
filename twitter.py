import requests
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session
import os
import json

dir = os.path.dirname(__file__)
load_dotenv()

class Twitter:
    def __init__(self):
        self.consumer_key = os.getenv("API_KEY")
        self.consumer_secret = os.getenv("API_SECRET_KEY")
        self.access_token = os.getenv("ACCESS_TOKEN")
        self.access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
        self.bearer_token = os.getenv("BEARER_TOKEN")
    
    def setOAuth(self):
        api = OAuth1Session(
            self.consumer_key,
            client_secret=self.consumer_secret,
            resource_owner_key=self.access_token,
            resource_owner_secret=self.access_token_secret,
        )
        return api
    
    def postTweet(self, payload):
        oauth = self.setOAuth()
        response = oauth.post(
            url= "https://api.twitter.com/2/tweets",
            json=payload,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer ${self.bearer_token}"
            }
        )
        if response.status_code != 201:
            error_message = "Request returned an error: {} {}".format(response.status_code, response.text)
            error_response = {
                "status": "error",
                "message": error_message,
                # Outras informações relevantes
            }
            return json.dumps(error_response)

        success_response = {
            "status": "success",
            "message": "Tweet posted successfully",
            # Outras informações relevantes
        }
        return json.dumps(success_response)
    



