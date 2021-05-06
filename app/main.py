#!/usr/bin/python

from fastapi import FastAPI
import requests
import os
import json
import tweepy

#instantiate the twitter api:
#keys and tokens
api_key = os.getenv('api_key')
api_key_secret = os.getenv('api_key_secret')
token = os.getenv('token')
token_secret = os.getenv('token_secret')

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(token, token_secret)

#instance
api = tweepy.API(auth)

#instantiate fastapi
app = FastAPI()

#zone apex
@app.get("/")
def read_root():
    return {"Hello": "Welcome to our twitter bot",
            "Instructions": "...",
            "more": "..."}


#post example

#to post a tweet with our account:
#api.update_status("...")




@app.post("/items/{item_id}")
def add_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name}
