from flask import Flask
from flask import request
from twilio.rest import Client
import os

app = Flask(__name__)

acc_id = os.environ.get('account')
auth_token = os.environ.get('token')
client = Client(acc_id, auth_token)
TWILIO_NUMBER = 'whatsapp:+14155238886'

def process_msg(msg):
    response = ""
    if msg == "Hi":
        response = "Hello master, I am your stock market bot. What can I do for you?"
    else:
        response = "Please type \"Hi\" to get started."
    return response

def send_msg(msg, recipient):
    client.messages.create(
        from_=TWILIO_NUMBER,
        body=msg,
        to=recipient
    )

@app.route("/", methods=["POST"])
def webhook():
    f=request.form
    msg = f['Body']
    sender = f['From']
    response = process_msg(msg)
    send_msg(response, sender)
    return"OK", 200


