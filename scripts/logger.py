from datetime import datetime
import csv
import os.path


def log(message_sid):
    file_exists = os.path.isfile('sent_texts.csv')
    if not file_exists:
        with open('sent_texts.csv', 'w', newline='') as fp:
            writer = csv.writer(fp)
            writer.writerow(['Date Time', 'Twilio Message ID'])
            writer.writerow([datetime.now(), message_sid])
    else:
        with open('sent_texts.csv', 'a', newline='') as fp:
            writer = csv.writer(fp)
            writer.writerow([datetime.now(), message_sid])
