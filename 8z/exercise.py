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

# 4. проверка, является ли строка палиндромом;

def tenet(string1):
    def index(left, right):
        if left >= right:
            return True
        if string1[left] != string1[right]:
            return False
        return index(left + 1, right - 1)
    return index(0, len(string1) - 1)

# 5. печать только чётных значений из списка;

def even_element(list1, index = None):
    if index == None:
        index = 0
    if index == len(list1):
        return
    if list1[index] % 2 == 0:
        print(list1[index])
    return even_element(list1, index+1)

# 6. печать элементов списка с чётными индексами;

def even_index(list1, index = None):
    if index == None:
        index = 0
    if index == len(list1):
        return
    if index % 2 == 0:
        print(list1[index])
    return even_index(list1, index+1)
