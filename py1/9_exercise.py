from datetime import date, datetime
import logging

logging.basicConfig(level = logging.DEBUG)

def age_check(year, month, day):
    logging.info('Проверка возраста')
    db = date(year, month, day)
    today = date.today()
    current_age = today.year - db.year
    assert current_age < 120
    if current_age >= 18:
        return True
    else:
        return False
    
def time_check():
    logging.info('Проверка времени')
    current_date_time = datetime.now()
    current_time = current_date_time.time()
    is22pm = current_time.replace(hour=23, minute=0, second=0, microsecond=0)
    is8am = current_time.replace(hour=8, minute=0, second=0, microsecond=0)
    if current_time >= is22pm or current_time < is8am:
        return False
    else:
        return True

def final_check(year, month, day):
    logging.info('Общая проверка')
    current_date_time = datetime.now()
    current_time = current_date_time.time()
    if time_check() and age_check(year, month, day):
        return True
    elif not time_check():
        return current_time
    else:
        assert year > 0
        return year

customer_num = int(input("Количество покупателей: "))
assert customer_num > 0

for i in range(customer_num):
    year = int(input("Какого года рождения? "))
    month = int(input("А месяц по счету? "))
    assert month <= 12 
    assert month > 0
    day = int(input("Дата-то какая? "))
    assert day <= 31
    assert month > 0
    if final_check(year, month, day) == 1:
        print("Оплата картой или наличкой?")
    elif final_check(year, month, day) == year:
        print(f"Какого ты года? {year}? Маленький еще, приходи после 18, а лучше не пей вообще.")
    else:
        current_date_time = datetime.now()
        print(f"Уже {current_date_time.hour}:{current_date_time.minute}, приходи завтра")
