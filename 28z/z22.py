def SherlockValidString(s: str) -> bool:

    counter = {}
    for i in set(s):
        number = s.count(i)
        if number not in counter:
            counter[number] = [i]
        else:
            counter[number].append(i)

    if len(counter) == 1:
        return True
    if len(counter) > 2:
        return False
    if len(counter[max(counter)]) > 1 and len(counter[min(counter)]) > 1:
        return False
    if min(counter) + 1 == max(counter) or max(counter) - 1 == min(counter):
        return True

    return False

