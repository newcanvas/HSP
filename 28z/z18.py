def MisterRobot(N: int, data: list) -> bool:

    iteration = 0
    for i in range(N):
        for j in range(i+1, N):
            if data[i] > data[j]:
                iteration += 1

    return iteration % 2 == 0

