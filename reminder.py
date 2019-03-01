import time
import webbrowser

# Simple repeating reminder to serve as framework for text reminder

# TODO: Change to be able to call message.py rather than opening a web link
# TODO: Implement a run.py command to run the function sending the text
# TODO: implement cron jobs as a replacement for this loop

# opens up song by Ariana Grande every day for a year


def reminder() -> None:
    print('This program ran on ' + time.ctime())
    time.sleep(86400)
    webbrowser.open('https://www.youtube.com/watch?v=LH4Y1ZUUx2g')


for i in range(365):
    reminder()
