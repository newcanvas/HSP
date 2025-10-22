def Keymaker(k: int) -> str:

    doors = []
    for i in range(k):
        doors.append(False)

    for i in range(k):
        for j in range(k):
            if (j+1) % (i+1) == 0:
                doors[j] = not doors[j]

    result = "".join(list(map(str, map(int, doors))))

    return result

