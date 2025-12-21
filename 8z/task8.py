def army_communication_matrix(n: int, matrix: list) -> str:
    best_sum = float('-inf')
    best_x = -1
    best_y = -1
    best_m = -1

    for m in range(2, n):
        for y in range(n - m + 1):
            row_sums = [0] * n
            for i in range(n):
                row_sum = 0
                for j in range(y, y + m):
                    row_sum += matrix[i][j]
                row_sums[i] = row_sum

            for x in range(n - m + 1):
                current_sum = 0
                for r in range(x, x + m):
                    current_sum += row_sums[r]

                if current_sum > best_sum:
                    best_sum = current_sum
                    best_x, best_y, best_m = x, y, m

    return f"{best_y} {best_x} {best_m}"

