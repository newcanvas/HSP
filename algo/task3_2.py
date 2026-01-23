import ctypes
from task3 import DynArray


'''
Задание 3.
Задача 5.
Реализация банковского метода.
'''

class DynArray_2:
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)
        self.bank = 0

    def __len__(self):
        return self.count

    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('i out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        if self.bank < self.count:
            raise RuntimeError('Not enough tokens')
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.bank -= self.count
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        self.bank += 2
        if self.count == self.capacity:
            self.resize(self.capacity * 2)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('i out of bounds')
        new_spot = i
        self.bank += 2
        if self.count == self.capacity:
            self.resize(self.capacity * 2)
        for i in range(self.count, new_spot, -1):
            self.array[i] = self.array[i - 1]
        self.array[new_spot] = itm
        self.count += 1

    '''
    Задание 3.
    Задача 6.
    Конструктор динамических массивов.
    '''

class MultiDynArray:
    def __init__(self, level):
        if not level:
            raise ValueError('level must have at least one dimension')
        self.dim = len(level)
        self.level = list(level)
        self.array = self.make_array(level, 0)

    def make_array(self, level, depth):
        arr = DynArray()
        size = level[0]

        if len(level) == 1:
            for i in range(size):
                arr.append(None)
        else:
            for i in range(size):
                arr.append(self.make_array(level[1:], depth + 1))
        return arr

    def __getitem__(self, indices):
        if len(indices) != self.dim:
            raise IndexError('Incorrect number of indices')
        current = self.array
        for i in range(len(indices)):
            idx = indices[i]
            if idx < 0 or idx >= len(current):
                raise IndexError('Index out of bounds')
            if i == self.dim - 1:
                return current[idx]
            current = current[idx]
        return None

    def __setitem__(self, indices, value):
        if len(indices) != self.dim:
            raise IndexError('Incorrect number of indices')
        current = self.array
        for i in range(len(indices)):
            idx = indices[i]
            if idx < 0:
                raise IndexError('Index out of bounds')
            while idx >= len(current):
                if i == self.dim - 1:
                    current.append(None)
                else:
                    current.append(self.make_array(self.level[i + 1:], i + 1))
            if i == self.dim - 1:
                current.array[idx] = value
            else:
                current = current[idx]

