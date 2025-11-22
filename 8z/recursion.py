# 1. возведение числа N в степень M;

def expo(N: int, M: int) -> int:
    if N == 1:
        return N * M
    return expo((N - 1), M) * M

# 2. вычисление суммы цифр числа;

def summ(N: int) -> int:
    if N == 0:
        return N
    return summ(N // 10) + N % 10

#  3. расчёт длины списка, для которого разрешена только операция удаления первого элемента pop(0) (и получение длины конечно);

def summ_list(list1: list) -> int:
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

def tenet(string1: str) -> bool:
  return index(string1, 0, len(string1) - 1)  
    
def index(string1, left, right):
    if left >= right:
        return True
    if string1[left] != string1[right]:
        return False
    return index(string1, left + 1, right - 1)

# 5. печать только чётных значений из списка;

def even_element(list1: list) -> None:
    return even_element_rec(list1, 0)

def even_element_rec(list1, i):
    if i == len(list1):
        return
    if list1[i] % 2 == 0:
        print(list1[i])
    return  even_element_rec(list1, i+1)

# 6. печать элементов списка с чётными индексами;

def even_index(list1: list) -> None:
    return even_index_rec(list1, 0)

def even_index_rec(list1, i):
    if i >= len(list1):
        return
    print(list1[i])
    return even_index_rec(list1, i+2)

# 7. нахождение второго максимального числа в списке (с учётом, что максимальных может быть несколько, если они равны).

def second_max(list1: list) -> float:
    if len(list1) <= 1:
        return None
    max1 = max(list1)
    if list1.index(max(list1)) == 0:
        max2 = list1[1]
    else:
        max2 = list1[0]
    return second_max_rec(list1, 0, max1, max2)
    
def second_max_rec(list1, i, max1, max2):
    if i == len(list1):
        return max2
    if i != list1.index(max(list1)) and list1[i] > max2:
       max2 = list1[i]
    return second_max_rec(list1, i+1, max1, max2)

# 8. поиск всех файлов в заданном каталоге, включая файлы, расположенные в подкаталогах произвольной вложенности.

import os

def find_files(path: str) -> list:
    files = []
    for level in os.listdir(path):
        full = os.path.join(path, level)
        if os.path.isfile(full):
            files.append(full)
        elif os.path.isdir(full):
            files.extend(find_files(full))
    return files
