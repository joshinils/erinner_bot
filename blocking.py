#!/usr/bin/env python3

"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second
intervals.
"""
# https://github.com/agronholm/apscheduler/blob/3.x/examples/schedulers/background.py

import os
import sys
# import time
from datetime import datetime

import pytz
from apscheduler.schedulers.background import BackgroundScheduler


def tick() -> None:
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = BackgroundScheduler(timezone=pytz.timezone("Europe/Berlin"))
    foo = scheduler.get_job(job_id="foo")
    # NoneType
    # print(foo.id)

    job = scheduler.add_job(tick, 'interval', seconds=3, id="userid/8")
    job = scheduler.add_job(tick, 'interval', seconds=3, id="userid/8")
    print(job.id)
    job.pause()
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    sys.modules[__name__].tick()
    exit()

    # try:
    #     # This is here to simulate application activity (which keeps the main thread alive).
    #     while True:
    #         time.sleep(2)
    # except (KeyboardInterrupt, SystemExit):
    #     # Not strictly necessary if daemonic mode is enabled but should be done if possible
    #     scheduler.shutdown()
