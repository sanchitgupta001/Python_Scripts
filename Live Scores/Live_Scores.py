from twilio.rest import TwilioRestClient
from lxml import html
from cricbuzz import * 
import requests
import time
import json
import subprocess
import os

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return

def sendscore(body):
    #Your account_sid goes here
    account_sid = "ACe0e25dca235a802b4370c692********" # Your account_sid for twilio account
    #Your authorization token goes here
    auth_token = "558dd9091fef9f98765355f5********" # Your auth_token for twiliio account
    client = TwilioRestClient(account_sid, auth_token)
    #to = "number to which SMS should be sent",from_="your twilio number"
    message = client.messages.create(body=body,to=Number1,from_=Number2) # Number1 and Number2 are contact numbers of the sender and recepients respectively
    print message.sid

while True:
    cric = CricbuzzParser()  
    match = cric.getXml() 
    details = cric.handleMatches(match)
    score_details = details[0]['Team']+"\n" + details[0]["Batting team"] + " : " + details[0]['Batting Team Overs']+" Overs - " + details[0]['Batting Team Runs']+"/" +details[0]['Batting Team Wickets'] + "\n" + details[0]['Match Status']
    print score_details
    os.system('notify-send '+ score_details)
    #sendmessage(score_details)   # Uncomment this for screen notifications on ubuntu
    #sendscore(score_details)  # Uncomment this for enabling message sending service
    #print " sent at:%s "%(time.ctime())
    time.sleep(20)
