import datetime
import pytz



tz = pytz.timezone('America/New_York')

def get_latest_time(a):
    max = datetime.datetime(2000,1,1,tzinfo=tz)
    for obj in a:
        if obj.time > max:
            max = obj.time
    return max
