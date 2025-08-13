def odometer(oksana: list) -> int:
    total = 0
    for i in range(len(oksana)):
        hours = 0
        if i == 0:
            hours = oksana[i+1]
            total += oksana[i] * hours
        elif i % 2 == 0:
            hours = oksana[i+1] - oksana[i-1]
            total += oksana[i] * hours

    return total


