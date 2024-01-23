import datetime
import pytz



utc=pytz.UTC

def get_latest_time(a):
    max = datetime.datetime(2000,1,1)
    for obj in a:
        if obj.time > max:
            max = obj.time
    return max
