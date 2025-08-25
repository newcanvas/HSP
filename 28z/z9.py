from math import sqrt

def TheRabbitsFoot(s: str, encode: bool) -> str:

    if encode:
        text = s.replace(" ", "")
        N = len(text)
        square = list(f"{sqrt(N):.2f}")
        rows, columns = int(square[0]), int(square[-2])

        while rows * columns < N:
            rows += 1

        matrix = []
        num = 0
        for i in range(rows):
            code = []
            for j in range(columns):
                if num < N:
                    code.append(text[num])
                    num += 1
            matrix.append(code)
    else:
        row_strings = s.split(' ')

        matrix = []
        for i in range(len(row_strings)):
            list1 = []
            for j in range(len(row_strings[i])):
                list1.append(row_strings[i][j])
            matrix.append(list1)

    str1 = ''
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if len(matrix[j]) < i+1:
                continue
            str1 += matrix[j][i]
        if i != len(matrix)-1 and encode:
            str1 += ' '

    return str1
x = TheRabbitsFoot('отдай мою кроличью лапку', True)
print(x)
