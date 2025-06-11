# 5.1. и 5.2.
import datetime
from can_buy_alc.final_check.age_time_check import final_check

customer_num = int(input("Количество покупателей: "))

for i in range(customer_num):
    year = int(input("Какого года рождения? "))
    month = int(input("А месяц по счету? "))
    day = int(input("Дата-то какая? "))
    if final_check(year, month, day) == 1:
        print("Оплата картой или наличкой?")
    elif final_check(year, month, day) == year:
        print(f"Какого ты года? {year}? Маленький еще, приходи после 18, а лучше не пей вообще.")
    else:
        current_date_time = datetime.datetime.now()
        print(f"Уже {current_date_time.hour}:{current_date_time.minute}, приходи завтра")

