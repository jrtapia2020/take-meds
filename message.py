from twilio.rest import Client

# Using Twilio service to send test SMS text messages to myself

# TODO: Change to my wife's phone number

# Your Account Sid and Auth Token from twilio.com/console
account_sid = ''    # Individual sid
auth_token = ''     # Individual token
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="This test message works!",
                     from_='',  # Twilio phone number
                     to=''      # Desired destination
                 )

print(message.sid)
