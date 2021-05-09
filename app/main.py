#!/usr/bin/python

from fastapi import FastAPI

from twitter import bot

#instantiate fastapi
app = FastAPI()

#zone apex
@app.get("/")
def read_root():
    return {"Hello": "Welcome to our twitter bot",
            "Instructions": "...", #fill
            "more": "..."}

#run the main function
@app.get("/airqualitybot/startbot")
def start_bot():
    bot()
    return {"Success": "The bot is up and running!"}

#create endpoint to stop the bot: