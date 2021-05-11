# DS 3002 - Data Science Systems

## Data Project 2 - Twitter Bot
Welcome to our Air Quality Twitter bot! 

## Overview
The purpose of our project was to build a Twitter bot that would respond to a user's tweet with Air Quality and temperature information for the specified city. We created a Python script that gets data from an API and parses that data to return useful information the the user. The Twitter account handle is @AirQualityBot1.

## Instructions
1. Send a tweet to our Twitter handle (@AirQualityBot1) specifying a city, state, and country to receive information about. You should include the information in the following format: /City/State/CountryAbbreviation/. Make sure you capitalize the city and state and the entire country abbreviation. Here is an example tweet: "@AirQualityBot1 /Charlottesville/Virginia/USA/"
2. If you receive an error message in response, that means you did not enter the city, state and country abbreviation in the correct format. Please send another tweet ensuring that you are using the correct format – don't forget to capitalize!
3. If you forget how to talk to the bot, send a tweet to the account saying 'help'. You will get a reply to your tweet with instructions on how to communicate with the bot. Here is an example tweet: "@AirQualityBot1 help"

## Process
A simple fastapi application was containerized in order to be deployed to AWS Lightsail as a container service. The fastapi we wrote has an endpoint "/start" that when visited will start up the bot--tweet away. If desired, the bot can be shut down by visiting the "/stop" endpoint.