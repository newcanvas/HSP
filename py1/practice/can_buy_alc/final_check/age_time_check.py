import datetime
from can_buy_alc.first_check.age_check import age_check

def time_check():
    current_date_time = datetime.datetime.now()
    current_time = current_date_time.time()
    is22pm = current_time.replace(hour=22, minute=0, second=0, microsecond=0)
    is8am = current_time.replace(hour=8, minute=0, second=0, microsecond=0)
    if current_time >= is22pm or current_time < is8am:
        return False
    else:
        return True

def final_check(year, month, day):
    current_date_time = datetime.datetime.now()
    current_time = current_date_time.time()
    if time_check() and age_check(year, month, day):
        return True
    elif not time_check():
        return current_time
    else:
        return year

