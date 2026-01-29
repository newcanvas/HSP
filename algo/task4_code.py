# NB: в этом файле только код для автоматической проверки, остальные ответы на задания без звездочки в файле task4_text.py

import ctypes

class Stack:
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.stack = self.make_stack(self.capacity)
        self.min_stack = []
        self.summ = 0

    def make_stack(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.stack[i]

    def resize(self, new_capacity):
        new_array = self.make_stack(new_capacity)
        for i in range(self.count):
            new_array[i] = self.stack[i]
        self.stack = new_array
        self.capacity = new_capacity

    def size(self):
        return self.count

    def pop(self):
        if self.count == 0:
            self.min_stack = []
            return None
        first = self.stack[0]
        if isinstance(self.stack[0], (int, bool)):
            self.summ -= first
        for i in range(self.count-1):
            self.stack[i] = self.stack[i+1]
        self.count -= 1
        if self.count > 0 and self.capacity // self.count >= 2:
            new_capacity = int(self.capacity / 1.5)
            if new_capacity < 16:
                new_capacity = 16
            self.resize(new_capacity)
        if self.count > 0 and isinstance(self.stack[0], (int, bool)):
            if self.stack[0] == self.min_stack[-1]:
                self.min_stack.pop()
        return first

    def push(self, value):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        for i in range(self.count, 0, -1):
            self.stack[i] = self.stack[i - 1]
        self.stack[0] = value
        self.count += 1
        if isinstance(self.stack[0], (int, bool)):
            self.summ += value
            if not self.min_stack or value <= self.min_stack[-1]:
                self.min_stack.append(value)

    def peek(self):
        if self.count == 0:
            return None
        return self.stack[0]

