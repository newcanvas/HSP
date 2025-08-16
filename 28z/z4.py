def MadMax(N: int, Tele: list) -> list:
    sorts = Tele.copy()
    new_list = []
    for i in range(N):
        if i < N // 2:
            new_list.append(min(sorts))
            sorts.remove(min(sorts))
        else:
            new_list.append(max(sorts))
            sorts.remove(max(sorts))
    return new_list


