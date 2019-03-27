# TODO: Edit check and upcoming commands

from scripts import message
from crontab import CronTab


# ------------------------------
# Commands for run.py
# ------------------------------
def scheduled() -> None:
    message.send_text()


def instant() -> None:
    message.send_text()


def check():
    """
    Displays the last time the scheduled message was sent.
    """
    x = 'time last ran'
    return x


def upcoming():
    """
    Displays the amount of time until the next scheduled message will be sent.
    """
    y = 'time until next message'
    return y


def enable() -> None:
    """
    Enables current cron job.
    """
    job.enable()
    print('Scheduled message is enabled.')


def disable() -> None:
    """
    Disables cron job that is currently set.
    """
    job.enable(False)
    print('Scheduled message disabled. The scheduled text will no longer be sent until it is enabled.')


# ------------------------------
# Cron job schedule
# ------------------------------
cron = CronTab(user=True)                     # change below to personal file location
job = cron.new(command='/usr/local/bin/python3.7 /Users/raul/Desktop/take-meds/run.py')
# set time below to desired time of running
# uncommenting lines below will write to crontab when reminder.py is ran
# job.hour.on(18)
# job.minute.on(0)
# cron.write()

