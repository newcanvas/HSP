import ctypes

class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):  # Временная сложность: O(n), пространственная: O(n) если был resize, O(1) без него.
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        new_spot = i
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        for i in range(self.count, new_spot, -1):
            self.array[i] = self.array[i - 1]
        self.array[new_spot] = itm
        self.count += 1

    def delete(self, i):  # Временная сложность: O(n), пространственная: O(n) если был resize, O(1) без него.
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        old_spot = i
        for i in range(old_spot, self.count-1):
            self.array[i] = self.array[i+1]
        self.array[self.count-1] = None
        self.count -= 1
        if self.count > 0 and self.capacity // self.count >= 2:
            new_capacity = int(self.capacity / 1.5)
            if new_capacity < 16:
                new_capacity = 16
            self.resize(new_capacity)

