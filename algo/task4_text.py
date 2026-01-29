# 1.

import ctypes

class Stack_tail:
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.stack = self.make_stack(self.capacity)

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
            return None
        last = self.stack[self.count-1]
        self.stack[self.count-1] = None
        self.count -= 1
        if self.count > 0 and self.capacity // self.count >= 2:
            new_capacity = int(self.capacity / 1.5)
            if new_capacity < 16:
                new_capacity = 16
            self.resize(new_capacity)
        return last
        

    def push(self, value):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.count += 1
        self.stack[self.count-1] = value

    def peek(self):
        if self.count == 0:
            return None
        return self.stack[self.count-1]
    
'''
# 2.
Для реализации стека с добавлением в хвост:
pop(): временная сложность: O(n), пространственная: O(n) если был resize, O(1) без него.
push(): временная сложность: O(n), пространственная: O(n) если был resize, O(1) без него.

# 3.
Данный цикл будет удалять по два крайних элемента (из головы или хвоста, в зависимости от реализации) на каждой итерации цикла и выводить их в консоль. 
Это будет происходить до тех пор, пока в стеке есть элементы. Если они закончатся на первой операции удаления, в консоль будет выведено None.

# 4.
Для реализации стека с добавлением в голову:
pop(): временная сложность: O(n), пространственная: O(n).
push(): временная сложность: O(n), пространственная: O(n).
'''

