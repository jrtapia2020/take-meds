# TODO: Edit check, upcoming, stop commands

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
    x = 'time last ran'
    return x


def upcoming():
    y = 'time until next message'
    return y


def stop() -> None:
    z = 'stops all future messages until started again'
    print(z)


# ------------------------------
# Cron job schedule
# ------------------------------
cron = CronTab(user=True)                     # change below to personal file location
job = cron.new(command='/usr/local/bin/python3.7 /Users/raul/Desktop/take-meds/run.py')
job.hour.on(12)
job.minute.on(0)
# cron.write()
# uncommenting line above will write to crontab when reminder.py is ran
