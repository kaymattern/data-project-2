#!/usr/bin/python3

from fastapi import FastAPI

app = FastAPI()

#zone apex
@app.get("/")
def read_root():
    return {"Hello": "Welcome to twitter bot"}


#post example
@app.post("/items/{item_id}")
def add_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name}