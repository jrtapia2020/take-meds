import time
import webbrowser

# Simple repeating reminder to serve as framework for text reminder

# TODO: Change to be able to call message.py rather than opening a web link
# TODO: implement cron jobs as a replacement for this loop

# Opens up 'Reminder' by The Weeknd every day for a year


def reminder() -> None:
    for i in range(366):
        print('This program ran on ' + time.ctime())
        webbrowser.open('https://www.youtube.com/watch?v=a40tAP5MC6M')
        time.sleep(86400)
