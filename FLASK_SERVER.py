import logging
import os
import paho.mqtt.client as mqtt
from flask import Flask
from flask_ask import Ask, request, session, question, statement
import RPi.GPIO as GPIO
import os
import openai
import json
import urllib.request
import requests
import urllib
from urllib.request import urlopen
from datetime import datetime
import threading


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)


@ask.intent('led',mapping={'user_question':'query'})
def chatgpt(user_question,room):
    chat=user_question;
    first_client = mqtt.Client()
    first_client.connect('54.87.92.106',1883)
    if 'turn on' in chat.lower():
            first_client.publish("home/alexa","TURNING ON")
            return statement("turning on lights")

    elif 'turn  off' in chat.lower():
            first_client.publish("home/alexa","TURNING OFF")
            return statement("turning off lights")
    else:
         first_client.publish("home/alexa",chat)
         return statement("Text changes to {} in panel".format(chat))


@ask.intent("AMAZON.YesIntent")
def continue_chatgpt():
    return chatgpt(None, None)

@ask.intent("AMAZON.NoIntent")
def stop_chatgpt():
    return statement("Exiting the led Skill")

@ask.launch
def launch():
    speech_text = 'Welcome to Innovation chat Automation'
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)

 
@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can say hello to me!'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)


@ask.intent('AMAZON.StopIntent')
def stop():
    return statement ("Exiting the skill")

@ask.session_ended
def session_ended():
    return "{}", 200

    
def start_flask_server():
    app.run(debug=True)

if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
    
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)










