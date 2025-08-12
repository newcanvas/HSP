def squirrel(N: int) -> int:
    F = 1
    for i in range(2, N+1):
        F = F * i

    first_d = int(str(F)[0])
    return first_d


