import datetime



def get_latest_time(a):
    max = datetime.datetime(2000)
    for obj in a:
        if obj.time > max:
            max = obj.time
    return max
