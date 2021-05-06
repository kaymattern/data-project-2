#play around with twitter api, then put code in one of the api's (main.py) endpoints (fxn)

import tweepy
import os
import requests
import time

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
print(j)

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

#air quality function
def get_data(city, state, country):
    output = requests.get(f'http://api.airvisual.com/v2/city?city={city}&state={state}&country={country}&key={air_key}')
    j = output.json()
    aqi = j['data']['current']['pollution']['aqius']
    temp_celsius = j['data']['current']['weather']['tp']
    print(f"The current temperature in {city}, {state} is {temp_celsius}, and the Air Quality Index is {aqi} which is a ... condition")


#respond to mentions:
def check_mentions(api, keywords, since_id):
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            api.update_status(
                status="testing...",
                in_reply_to_status_id=tweet.id,
                auto_populate_reply_metadata=True
            )
    return new_since_id

def main():
    since_id = 1
    while True:
        since_id = check_mentions(api, ["help", "support"], since_id)
        time.sleep(10)

if __name__ == "__main__":
    main()