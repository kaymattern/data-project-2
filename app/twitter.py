#!/usr/bin/python

import tweepy
import os
import requests
import json

#keys and tokens
api_key = os.getenv('api_key')
api_key_secret = os.getenv('api_key_secret')
token = os.getenv('token')
token_secret = os.getenv('token_secret')
air_key = os.getenv('air_key')

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(token, token_secret)

#instance
api = tweepy.API(auth)


#get air quality data function
def get_data(city, state, country):
    output = requests.get(f'http://api.airvisual.com/v2/city?city={city}&state={state}&country={country}&key={air_key}')
    j = output.json()
    aqi = j['data']['current']['pollution']['aqius']
    if aqi > 300:
        condition = 'hazardous'
    elif aqi > 200:
        condition = 'very unhealthy'
    elif aqi > 150:
        condition = 'unhealthy'
    elif aqi > 100:
        condition = 'unhealthy for sensitive groups'
    elif aqi > 50:
        condition = 'moderate'
    else:
        condition = 'good'
    temp_celsius = j['data']['current']['weather']['tp']
    temp_f = round((temp_celsius * 5 / 9) + 32, 0)
    reply = f"The current temperature in {city}, {state} is {temp_f}, and the Air Quality Index is {aqi} which is a {condition} condition"
    return reply


# respond to mentions:
# figure out an easy way to format the tweets so we can parse the text easily
# maybe just have them type city: __ , state: __ , country: __ or something

#create class for the stream
class MyStreamListener(tweepy.StreamListener):

    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        text = tweet.text
        try:
             city = text.split('/')[1]
             state = text.split('/')[2]
             country = text.split('/')[3]
        except:
            pass

        #help message
        if text == "@AirQualityBot1 help":
            api.update_status(
                    status= "informative message...",
                    in_reply_to_status_id=tweet.id,
                    auto_populate_reply_metadata=True
                )
        else:
            # then tweet back with the output of the get_data fxn (the reply)
            try:
                api.update_status(
                        status= get_data(city, state, country),
                        in_reply_to_status_id=tweet.id,
                        auto_populate_reply_metadata=True
                    )
            except:
                api.update_status(
                        status= "Sorry, you gave me an invalid request :( Tweet 'help' to learn how to talk to me!",
                        in_reply_to_status_id=tweet.id,
                        auto_populate_reply_metadata=True
                    )

# start the stream
def bot():
    tweets_listener = MyStreamListener(api)
    stream = tweepy.Stream(auth = api.auth, listener = tweets_listener)
    stream.filter(track=["@AirQualityBot1"]) #track tweets that mention the bot

#call fxn to start the bot
#bot()

