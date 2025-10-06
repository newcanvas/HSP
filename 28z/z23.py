def TreeOfLife(H: int, W: int, N: int, tree: list) -> list:

    all_lists = []
    for i in range(H):
        all_lists.append(list(tree[i]))

    for i in range(H):
        for j in range(W):
            if all_lists[i][j] == '.':
                all_lists[i][j] = 0
            else:
                all_lists[i][j] = 1

    for year in range(N):
        for a in range(H):
            for b in range(W):
                all_lists[a][b] += 1

        current_year = [row[:] for row in all_lists]

        if year % 2 != 0:
            for a in range(H):
                for b in range(W):
                    if current_year[a][b] > 2:
                        all_lists[a][b] = 0
                        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                            ni, nj = a + dx, b + dy
                            if 0 <= ni < H and 0 <= nj < W:
                                all_lists[ni][nj] = 0

    final = []
    for h in range(H):
        for w in range(W):
            if all_lists[h][w] == 0:
                all_lists[h][w] = '.'
            else:
                all_lists[h][w] = '+'
        new_string = "".join(all_lists[h])
        final.append(new_string)

    return final

