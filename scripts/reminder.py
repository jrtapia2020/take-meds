import time
import webbrowser

# Simple repeating reminder to serve as framework for text reminder

# TODO: Change to be able to call message.py rather than opening a web link
# TODO: Implement cron jobs as a replacement for scheduled loop
# TODO: Allow other command line prompts to be added while scheduled function is running


def scheduled() -> None:    # Opens up 'Reminder' by The Weeknd every day for a year
    for i in range(1000):
        print('This program ran on ' + time.ctime())
        webbrowser.open('https://www.youtube.com/watch?v=a40tAP5MC6M')
        time.sleep(86400)


def instant() -> None:
    print('This program ran on ' + time.ctime())
    webbrowser.open('https://www.youtube.com/watch?v=a40tAP5MC6M')
    # TODO: Ensure it gets back to normal schedule


def check():
    x = 'time last ran'
    return x


def next():
    y = 'time until next message'
    return y


def stop() -> None:
    z = 'stops all future messages until started again'
    print(z)
