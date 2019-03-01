from twilio.rest import Client

# Using Twilio service to send test SMS text messages to myself

# TODO: Change to my wife's phone number

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACd96a309d2beb4203b877b8d31bb46950'
auth_token = 'bcd91e23c082845f707ac282bcabee01'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="This test message works!",
                     from_='+12015716417',
                     to='+16026421037'
                 )

print(message.sid)
