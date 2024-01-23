import datetime


def get_latest_time(a):
    max = datetime.datetime()
    for obj in a:
        if obj.time > max:
            max = obj.time
