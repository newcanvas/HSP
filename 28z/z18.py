def MisterRobot(N: int, data: list) -> bool:

    subset = data.copy()

    i = 0
    while i < N-2:
        sub = subset[i:i+3]
        if sub.index(min(sub)) != 0:
            while sub.index(min(sub)) != 0:
                sub = sub[1:] + sub[:1]
            subset[i:i+3] = sub
            i = 0
        i += 1

    return subset[-2] < subset[-1]

