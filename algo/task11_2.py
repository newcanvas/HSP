from task11 import BloomFilter

'''
Задание 11.
Задача 2.
Реализация слияния двух фильтров Блюма.
Вероятность ложноположительного ответа увеличивается.
'''

def merge_filters(self, other):
    new_filter = BloomFilter(self.size)
    new_filter.bits = self.bits | other.bits
    return new_filter

'''
Задание 11.
Задача 3.
Реализация фильтра Блюма, допускающая удаление.
'''

class CountingBloomFilter:

    def __init__(self, size):
        self.size = size
        self.bits = [0] * size

    def hash1(self, s):
        h = 0
        for c in s:
            h = (h * 17 + ord(c)) % self.size
        return h

    def hash2(self, s):
        h = 0
        for c in s:
            h = (h * 223 + ord(c)) % self.size
        return h

    def add(self, s):
        i1 = self.hash1(s)
        i2 = self.hash2(s)

        self.bits[i1] += 1
        self.bits[i2] += 1

    def is_value(self, s):
        i1 = self.hash1(s)
        i2 = self.hash2(s)

        return self.bits[i1] > 0 and self.bits[i2] > 0

    def remove(self, s):
        i1 = self.hash1(s)
        i2 = self.hash2(s)

        if self.bits[i1] > 0:
            self.bits[i1] -= 1
        if self.bits[i2] > 0:
            self.bits[i2] -= 1

'''
Задание 11.
Задача 4.
Реализация восстановления исходного множества.
'''

def recover(bf, candidates):
    recovered = []

    for s in candidates:
        if bf.is_value(s):
            recovered.append(s)

    return recovered

'''
Рефлексия по решению задач задания 9.

5. Словарь с использованием упорядоченного списка по ключу.
В целом, решение частично соответсует эталонному, но у меня получилась скорее комбинация словаря и списка. Стоило сделать бОльший упор на индексную связку ключей и значений.

'''
