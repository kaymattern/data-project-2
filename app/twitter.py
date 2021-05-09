#!/usr/bin/python

import tweepy
import os
import requests
import json

#keys and tokens
api_key = 'EipqCuBOepknJZTpvBWIn5o3w' #os.getenv('api_key')
api_key_secret = '5vxpfKuHjmJE1bl9vPUrmxB6xZhN17V4TDfjcu7jjFtbBeZqyx' #os.getenv('api_key_secret')
token = '1390393237366509574-fio1YEruOgyYKH9KOwxO7bnCpmX78M' #os.getenv('token')
token_secret = 'Y5AU5rTL6MobnHnxdv2ubuGQZJISF3as8yqrTJOuAMHaq' #os.getenv('token_secret')
air_key = '7efc258f-8936-4475-bf29-bc42c287a008' #os.getenv('air_key')

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(token, token_secret)

#instance
api = tweepy.API(auth)


#AIR QUALITY API

#test data
city = 'Los Angeles'
state = 'California'
country = 'USA'

#for specified city
output = requests.get(f'http://api.airvisual.com/v2/city?city={city}&state={state}&country={country}&key={air_key}')

#API response
j = output.json()
#print(j)

#what metrics we'll return to the user:
# aqius : air quality index for the US
aqi = j['data']['current']['pollution']['aqius']
# 0-50 : good
# 51-100 : moderate
# 101-150 : unhealthy for sensitive groups
# 151-200 : Unhealthy
# 201-300 : Very Unhealthy
# 301+ : Hazardous
# ^^ return the condition back to user based on what the AQI value is

# tp : temperature in celcius - convert to farenheit (find equation online)
temp_celsius = j['data']['current']['weather']['tp']
#convert to faren

#then tweet something like: 
# "The current temperature in {city}, {state} is {tp_faren} degrees Farenheit, and the Air Quality Index is {aqi} which is a {condition} condition."

#get air quality data function
def get_data(city, state, country):
    output = requests.get(f'http://api.airvisual.com/v2/city?city={city}&state={state}&country={country}&key={air_key}')
    j = output.json()
    aqi = j['data']['current']['pollution']['aqius']
    # find condition (if else)
    # condition = ...
    temp_celsius = j['data']['current']['weather']['tp']
    # convert to farenheit
    # temp_f
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
        # parse text - extract city, state, and country

        # city = ...
        # state = ...
        # country = ...

        # then tweet back with the output of the get_data fxn (the reply)
        api.update_status(
                status= "test", #get_data(city, state, country),
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

