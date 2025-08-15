def ConquestCampaign(N: int, M: int, L: int, battalion: list) -> int:
    day = 1
    field = []
    for i in range(len(battalion)):
        if i % 2 == 0:
            square = [battalion[i], battalion[i+1]]
            if square not in field:
                field.append(square)
    while len(field) < N * M:
        for i in range(len(field)):
            new_sqare = [field[i][0] + 1, field[i][1]]
            if field[i][0] + 1 <= N and new_sqare not in field:
                field.append(new_sqare)
            new_sqare = [field[i][0] - 1, field[i][1]]
            if field[i][0] - 1 > 0 and new_sqare not in field:
                field.append(new_sqare)
            new_sqare = [field[i][0], field[i][1] + 1]
            if field[i][1] + 1 <= M and new_sqare not in field:
                field.append(new_sqare)
            new_sqare = [field[i][0], field[i][1] - 1]
            if field[i][1] - 1 > 0 and new_sqare not in field:
                field.append(new_sqare)
        day += 1

    return day


