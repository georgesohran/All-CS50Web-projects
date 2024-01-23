import datetime
import pytz


utc=pytz.UTC

def get_latest_time(a):
    max_time = datetime.datetime(2000,1,1,tzinfo=utc)
    for obj in a:
        time = obj.time.replace(tzinfo=utc)
        if time > max_time:
            max_time = obj.time
    return max
