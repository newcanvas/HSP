import re

def TankRush(H1: int, W1: int, S1: str, H2: int, W2: int, S2: str) -> bool:

    if W2 > W1:
        return False

    s1_list = S1.split(' ')
    s2_list = S2.split(' ')

    for i in s2_list:
        if i not in S1:
            return False

    starts = []
    for i in s2_list:
        sub_start = []
        for j in s1_list:
            for m in re.finditer(f"(?={i})", j):
                sub_start.append(m.start())
        starts.append(sub_start)

    result = set(starts[0])
    for s in starts[1:]:
        result.intersection_update(s)

    if len(result) == 0:
        return False
    return True

