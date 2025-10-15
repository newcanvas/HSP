import re

def white_walkers(village: str) -> bool:

    alls = []
    for i in range(len(village)):
        if re.match(r"\d|=", village[i]):
            alls.append(village[i])

    if len(alls) < 5:
        return False

    summ_list = []
    subs = []
    for i in range(len(alls)):
        if re.match(r"\d", alls[i]):
            summ_list.append(alls[i])
        elif len(summ_list) > 0:
            subs.append(alls[i])
        if len(summ_list) == 2:
            if int(summ_list[0]) + int(summ_list[1]) == 10:
                if subs != ['=', '=', '=']:
                    return False
                summ_list.pop(0)
                subs = []
                continue
            summ_list.pop(0)
            subs = []

    return True

