#!/usr/bin/python

import flask

from twitter import bot

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#zone apex
@app.route('/', methods=['GET'])
def read_root():
    return {"Hello": "Welcome to our twitter bot",
            "Instructions": "...", #fill
            "more": "..."}

@app.route('/start', methods=['GET'])
def start_bot():
    bot()
    return {"Success": "The bot is up and running!"}

# #create endpoint to stop the bot:

if __name__ == '__main__':
    app.run('0.0.0.0','8080')