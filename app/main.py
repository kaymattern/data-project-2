#!/usr/bin/python

from fastapi import FastAPI

from twitter import check_mentions
from twitter import main
from twitter import get_data

#instantiate fastapi
app = FastAPI()

#zone apex
@app.get("/")
def read_root():
    return {"Hello": "Welcome to our twitter bot",
            "Instructions": "...",
            "more": "..."}

#run the main function
@app.get("/airqualitybot/run")
def start_bot():
    main()
