def TankRush(H1: int, W1: int, S1: str, H2: int, W2: int, S2: str) -> bool:

    if W2 > W1:
        return False

    s1_list = S1.split(' ')
    s2_list = S2.split(' ')

    match = 0
    for i in s2_list:
        for j in s1_list:
            if i in j:
                match += 1
                break

    if match == len(s2_list):
        return True
    return False

