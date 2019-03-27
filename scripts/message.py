# Using Twilio service to send SMS text to targeted phone numbers
from twilio.rest import Client


# TODO: Add personal data in commented sections
def send_text():
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = ''    # Individual sid
    auth_token = ''     # Individual token
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body='',
                         from_='',  # Twilio phone number
                         to=''      # Recipient phone number
                     )
    print(f'Message sent successfully. SID: {message.sid}')
    return message.sid
