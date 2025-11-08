# 1. возведение числа N в степень M;

def expo(N, M):
    if N == 1:
        return N * M
    return expo((N - 1), M) * M

# 2. вычисление суммы цифр числа;

def summ(N):
    if N == 0:
        return N
    return summ(N // 10) + N % 10

#  3. расчёт длины списка, для которого разрешена только операция удаления первого элемента pop(0) (и получение длины конечно);

def summ_list(list1):
    if len(list1) == 0:
        return 0
    list1.pop(0)
    return 1 + summ_list(list1)

def summ_list_2(list1):
    try:
        list1.pop(0)
        return 1 + summ_list_2(list1)
    except IndexError:
        return 0
