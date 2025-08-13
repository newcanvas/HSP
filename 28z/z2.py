def odometer(oksana: list) -> int:
    total = 0
    for i in range(len(oksana)):
        if i % 2 == 0:
            total += oksana[i]

    return total


