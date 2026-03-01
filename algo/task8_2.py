from random import randint


'''
Задание 8.
Задача 3.
Реализация динамической хэш таблицы, увеличивающейся в 2 раза при достижении 75% заполненности.
Временная сложность операции resize: O(n), пространственная: O(1).
'''
class HashTable2:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.capacity = 0

    def hash_fun(self, value):
        hash = sum(value.encode('utf-8'))
        index = hash % self.size
        return index

    def seek_slot(self, value):
        slot = self.hash_fun(value)
        if self.slots[slot] is None:
            return slot
        counter = set()
        while len(counter) < self.size:
            slot += self.step
            if slot > (self.size - 1):
                slot = slot - self.size
            if self.slots[slot] is None:
                return slot
            counter.add(slot)
            continue
        return None

    def put(self, value):
        if self.capacity / self.size > 0.75:
            self.resize(self.size * 2)
        slot = self.seek_slot(value)
        if slot is None:
            return None
        self.slots[slot] = value
        self.capacity += 1
        return slot

    def resize(self, new_size):
        new_slots = self.slots
        self.size = new_size
        self.slots = [None] * self.size
        for i in range(self.size // 2):
            if new_slots[i] is not None:
                slot = self.seek_slot(new_slots[i])
                self.slots[slot] = new_slots[i]

    def find(self, value):
        slot = self.hash_fun(value)
        if self.slots[slot] == value:
            return slot
        counter = set()
        while len(counter) < self.size:
            slot += self.step
            if slot > (self.size - 1):
                slot = slot - self.size
            if self.slots[slot] == value:
                return slot
            counter.add(slot)
            continue
        return None

'''
Задание 8.
Задача 4.
Реализация хэш таблицы, использующей несколько хэш функций.
Сложность вставки в среднем уменьшилась до O(1), распределение более расномерное и снижена вероятность коллизий. 
Но при большом массиве данных может увеличиться время за счет прохода по таблице в случае занятых обоих стартовых слотов.
'''
class HashTableTwoFun:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        hash = sum(value.encode('utf-8'))
        index = hash % self.size
        return index

    def hash_fun2(self, value):
        h = 0
        for ch in value:
            h = h * 31 + ord(ch)
        return h % self.size

    def seek_slot(self, value):
        hash_functions = [self.hash_fun, self.hash_fun2]
        for h_fun in hash_functions:
            slot = h_fun(value)
            if self.slots[slot] is None:
                return slot
        for h_fun in hash_functions:
            start_slot = h_fun(value)
            slot = start_slot
            visited = set()
            while len(visited) < self.size:
                slot += self.step
                if slot > self.size - 1:
                    slot -= self.size
                if self.slots[slot] is None:
                    return slot
                visited.add(slot)
        return None

    def put(self, value):
        slot = self.seek_slot(value)
        if slot is None:
            return None
        self.slots[slot] = value
        return slot

    def find(self, value):
        hash_functions = [self.hash_fun, self.hash_fun2]
        for h_fun in hash_functions:
            slot = h_fun(value)
            if self.slots[slot] == value:
                return slot
        for h_fun in hash_functions:
            start_slot = h_fun(value)
            slot = start_slot
            visited = set()
            while len(visited) < self.size:
                slot += self.step
                if slot > self.size - 1:
                    slot -= self.size
                if self.slots[slot] == value:
                    return slot
                visited.add(slot)
        return None

'''
Задание 8.
Задача 5.
Организация ddos атаки на изначальную таблицу.
В среднем случае временная сложность серии операций вставки составляет O(n).
В исправленном варианте сложность составит O(n) только в худшем случае.
'''

def generate_ddos_keys(size, target_mod):
    keys = []
    while len(keys) < size:
        rand = randint(0,99)
        value = f'key{rand}'
        if sum(value.encode('utf-8')) % size == target_mod:
            keys.append(value)
    return keys

class HashTableSalted:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def salt(self, value):
        value = f'{value}somesalt'
        return value

    def hash_fun(self, value):
        value = self.salt(value)
        hash = sum(value.encode('utf-8'))
        index = hash % self.size
        return index

    def seek_slot(self, value):
        slot = self.hash_fun(value)
        if self.slots[slot] is None:
            return slot
        counter = set()
        while len(counter) < self.size:
            slot += self.step
            if slot > (self.size - 1):
                slot = slot - self.size
            if self.slots[slot] is None:
                return slot
            counter.add(slot)
            continue
        return None

    def put(self, value):
        slot = self.seek_slot(value)
        if slot is None:
            return None
        self.slots[slot] = value
        return slot

    def find(self, value):
        slot = self.hash_fun(value)
        if self.slots[slot] == value:
            return slot
        counter = set()
        while len(counter) < self.size:
            slot += self.step
            if slot > (self.size - 1):
                slot = slot - self.size
            if self.slots[slot] == value:
                return slot
            counter.add(slot)
            continue
        return None

'''
Рефлексия по решению задач задания 6.

4. Проверка строки на палиндром.
Логика решения совпадает с эталонной.

5. Минимальный элемент деки за O(1).
Решили задачу менее оптимально, с помощью циклов в функциях добавления, проверяющих "минимальность" входного числа.
А при удалении, если удаляемое число находится в конце в списке минимальных, то оно тоже удаляется.

6. Двусторонняя очередь на базе динамического массива.
Насколько я поняла, логику все-таки смешала, так как логика деки и ресайз находятся на одном уровне.
'''
