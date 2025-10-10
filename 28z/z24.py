def MatrixTurn(Matrix: list, M: int, N: int, T: int):

    for step in range(T):
        og_matrix = [row[:] for row in Matrix]
        for lvl in range(M//2):
            for i in(lvl, M-1-lvl):
                row = list(Matrix[i][lvl:N-lvl])
                og_row = list(og_matrix[i][lvl:N-lvl])
                full_row = list(Matrix[i])
                for j in range(1,len(row)):
                    if i == lvl:
                        row[j] = og_row[j-1]
                    else:
                        row[-j-1] = og_row[-j]
                full_row[lvl:N-lvl] = row
                Matrix[i] = "".join(full_row)

            for a in range(lvl,M-lvl):
                row = list(Matrix[a][lvl:N-lvl])
                full_row = list(Matrix[a])
                if a == lvl:
                    row[0] = og_matrix[a+1][lvl]
                elif a == M-1-lvl:
                    row[-1] = og_matrix[a-1][-1-lvl]
                else:
                    row[lvl] = og_matrix[a+1][lvl]
                    row[-1] = og_matrix[a-1][-1-lvl]
                full_row[lvl:N-lvl] = row
                Matrix[a] = "".join(full_row)

