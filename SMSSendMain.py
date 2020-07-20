from twilio.rest import Client

'''
This Code sends an SMS to the specified number using the twilio api
The Sender Number must be verified by the twilio
'''

account_sid = 'AC8f6d0b2e9f8f4eea1fad06a04fb417fe'
auth_token = 'fd0e7f54d2347fffe7e072010e9ee18f'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there!',
                              from_='+12029331571',
                              to='+918898844579'
                          )

print(message.sid)