from scripts import message, logger
from crontab import CronTab


# ------------------------------
# Commands for run.py
# ------------------------------
def scheduled() -> None:
    message_sid = message.send_text()
    logger.log(message_sid)


def instant() -> None:
    message_sid = message.send_text()
    logger.log(message_sid)


def check():
    """
    Displays the last time the scheduled message was sent.
    """
    schedule = job.schedule()
    prev = schedule.get_prev()
    print(prev)


def upcoming():
    """
    Displays when the next scheduled message will be sent.
    """
    schedule = job.schedule()
    next = schedule.get_next()
    print(f'The next scheduled message will be sent on: {next}')


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
# uncommenting line below will write to crontab when reminder.py is ran
job.hour.on(18)
job.minute.on(0)
# cron.write()

