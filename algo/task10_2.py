from __future__ import annotations
from typing import Any

from task10 import PowerSet

'''
Задание 10.
Задача 4.
Метод, реализующий декартово произведение множеств.
Временная сложность: O(n * m), пространственная: O(1).
'''

def decart(self, set2: PowerSet) -> list:
    dec = []
    for i in self.dict:
        for j in set2.dict:
            dec.append((i, j))
    return dec

PowerSet.decart = decart

'''
Задание 10.
Задача 5.
Функция, находящая пересечение трех и более множеств.
Временная сложность: O(n * m), пространственная: O(n).
'''

def FindMultiIntersection(ps_list: list) -> PowerSet:
    base = ps_list[0].intersection(ps_list[1])
    for i in range(2, len(ps_list)):
        base = base.intersection(ps_list[i])
    return base

'''
Задание 10.
Задача 6.
Реализация мульти-множества (Bag).
Временная сложность операции добавления: O(1), пространственная: O(1).
Временная сложность операции удаления: O(n), пространственная: O(1).
Временная сложность получения всех элементов с их множествами: O(1), пространственная: O(1).
'''

class Bag:

    def __init__(self) -> None:
        self.pow_set = []
        self.dict = {}

    def get(self, value: Any) -> bool:
        return value in self.dict

    def put(self, value: Any) -> None:
        self.pow_set.append(value)
        if value not in self.dict:
            self.dict[value] = 1
            return
        self.dict[value] += 1
        return

    def remove(self, value: Any) -> bool:
        result = self.get(value)
        if result:
            self.pow_set.remove(value)
            self.dict[value] -= 1
        if value in self.dict and self.dict[value] == 0:
            del self.dict[value]
        return result

    def get_all(self):
        return self.dict

'''
Рефлексия по решению задач задания 8.

3. Динамическая хэш-таблица.
Логика решения соответствует эталонной.

5. ddos хэш-таблицы и соль.
Использовала статическую соль, потому что не смогла реализовать надежное решение для обратного поиска позиции в таблице. 
В рефлексии, конечно, этот вопрос закрывается: нужно было просто хранить значение и соль отдельно.

'''
