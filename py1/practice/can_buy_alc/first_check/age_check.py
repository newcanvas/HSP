from datetime import date


def age_check(year, month, day):
    db = date(year, month, day)
    today = date.today()
    current_age = today.year - db.year
    if current_age >= 18:
        return True
    else:
        return False
