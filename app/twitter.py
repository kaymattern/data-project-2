#play around with twitter api, then put code in one of the api's (main.py) endpoints (fxn)

import tweepy
import os

#keys and tokens
api_key = os.getenv('api_key')
api_key_secret = os.getenv('api_key_secret')
token = os.getenv('token')
token_secret = os.getenv('token_secret')
print(os.environ)
# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(token, token_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")