from twilio.rest import Client

account_sid = '--------------------------------------' 
auth_token = '-----------------------------------------' 

myPhone = '--------------' 
TwilioNumber = '-------------' 

client = Client(account_sid, auth_token)

client.messages.create(to="Receiver No---------",from_=TwilioNumber,body='abcdef')