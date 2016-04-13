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
    account_sid = "ACe0e25dca235a802b4370c69231768fcb"
    #Your authorization token goes here
    auth_token = "558dd9091fef9f98765355f55d451a3c"
    client = TwilioRestClient(account_sid, auth_token)
    #to = "number to which SMS should be sent",from_="your twilio number"
    message = client.messages.create(body=body,to="+919086225038",from_="+16699001403")
    print message.sid

while True:
    cric = CricbuzzParser()  
    match = cric.getXml() 
    details = cric.handleMatches(match)
    score_details = details[0]['Team']+"\n" + details[0]["Batting team"] + " : " + details[0]['Batting Team Overs']+" Overs - " + details[0]['Batting Team Runs']+"/" +details[0]['Batting Team Wickets'] + "\n" + details[0]['Match Status']
    print score_details
    #os.system('notify-send '+ score_details)
    #sendmessage(score_details)
    #sendscore(score_details)
    #print " sent at:%s "%(time.ctime())
    time.sleep(20)
