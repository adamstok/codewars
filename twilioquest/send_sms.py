import twilio_credentials
from twilio.rest import Client

account = twilio_credentials.account
token = twilio_credentials.token
client = Client(account, token)

message = client.messages.create(to=twilio_credentials.phone_number, from_="+18646488680", body="Hello world")


