def UFO(N: int, data: list, octal: bool) -> list:

    result = []
    if octal:
        base = 8
    else:
        base = 16

    for i in range(N):
        summ = 0
        power = len(str(data[i]))-1
        for j in range(len(str(data[i]))):
            summ += int(str(data[i])[j]) * base**power
            power -= 1
        result.append(summ)

    return result

