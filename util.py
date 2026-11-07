import datetime

def timestamp():
    x = datetime.datetime.now()
    time = x.strftime("%x %X")
    return time