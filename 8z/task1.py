import re

def white_walker_2(village: str) -> bool:
    safe = False
    counter = 0
    first_d = 0
    if len(village) < 5:
        return False
    for i in range(len(village)):
        if village[i] == '=':
            counter += 1
            continue
        if re.match(r"\d", village[i]):
            if int(first_d) + int(village[i]) == 10:
                if counter == 3:
                    safe = True
                else:
                    safe = False
            first_d = village[i]
            counter = 0
            continue
        else:
            continue
    return safe
