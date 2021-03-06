#!/usr/bin/python

#import flask
from fastapi import FastAPI
from twitter import bot
from twitter import stop

app = FastAPI()

@app.get("/")  # zone apex
def read_root():
    return {"Hello": "Welcome to our Twitter bot!",
            "Instructions": "Use the endpoint '/start' to start the bot. Use endpoint 'stop' to stop"}

@app.get("/start")
def start_bot():
    bot()
    return {"Success": "The bot is up and running!"}

@app.get("/stop")
def stop_bot():
    stop()
    return {"Bot terminated": "The bot went to sleep"}


# flask app:

# app = flask.Flask(__name__)
# app.config["DEBUG"] = True

# #zone apex
# @app.route('/', methods=['GET'])
# def read_root():
#     return {"Hello": "Welcome to our Twitter bot!",
#             "Instructions": "Use the endpoint '/start' to start the bot. Use endpoint 'stop' to stop"}

# @app.route('/start', methods=['GET'])
# def start_bot():
#     bot()
#     return {"Success": "The bot is up and running!"}

# @app.route('/stop', methods=['GET'])
# def stop_bot():
#     stop()
#     return {"Bot terminated": "The bot went to sleep"}

# if __name__ == '__main__':
#     app.run(host = '0.0.0.0', port = '5000')