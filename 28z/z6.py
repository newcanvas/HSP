def PatternUnlock(N: int, hits: list) -> str:
    
    diag = [{6,2}, {2,9}, {2,7}, {2,4}, {1,5}, {5,3}, {3,8}, {8,1}]

    summ = 0
    for i in range(N-1):
        pair = {hits[i], hits[i+1]}
        if pair in diag:
            summ += 1.414215
        else: summ += 1

    summ = f"{summ:.5f}"
    final = summ.replace(".", "").replace("0", "")
    return final


