import ctypes

from task6 import Deque
from task4_code import Stack

'''
Задание 6.
Задача 7.3.
Функция, проверяющая, является ли строка палиндромом, с помощью deque.
Временная сложность: O(n), пространственная: O(n).
'''

def isStringPalindrome(string1: str) -> bool:
    test_deque = Deque()
    for i in string1:
        test_deque.addFront(i)
    for i in range(test_deque.count // 2):
        if test_deque.removeFront() != test_deque.removeTail():
            return False
    return True

'''
Задание 6.
Задача 7.4.
Метод, возвращающий минимальное значение в деке.
Временная сложность: O(1), пространственная: O(1).
'''
def returnMin(self):
    if self.size() == 0:
        return None
    return self._min_deque[0]

Deque.returnMin = returnMin

'''
Задание 6.
Задача 7.5.
Реализация деки с помощью динамического массива.
'''

class DynDeque:

    def __init__(self):
        self.capacity = 16
        self.deque = self.make_deque(self.capacity)
        self.head = 0
        self.tail = 0
        self.count = 0

    def make_deque(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.deque[(self.head + i) % self.capacity]

    def resize(self, new_capacity):
        new_deque = self.make_deque(new_capacity)
        for i in range(self.count):
            new_deque[i] = self.deque[(self.head + i) % self.capacity]
        self.deque = new_deque
        self.head = 0
        self.tail = self.count
        self.capacity = new_capacity

    def addFront(self, item):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.head = (self.head - 1) % self.capacity
        self.deque[self.head] = item
        self.count += 1

    def addTail(self, item):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.deque[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.count += 1

    def removeFront(self):
        if self.count == 0:
            return None
        first = self.deque[self.head]
        self.deque[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        if self.capacity > 16 and self.count > 0 and self.count <= self.capacity // 2:
            self.resize(max(16, self.capacity // 2))
        return first

    def removeTail(self):
        if self.count == 0:
            return None
        self.tail = (self.tail - 1) % self.capacity
        last = self.deque[self.tail]
        self.deque[self.tail] = None
        self.count -= 1
        if self.capacity > 16 and self.count > 0 and self.count <= self.capacity // 2:
            self.resize(max(16, self.capacity // 2))
        return last

    def size(self):
        return self.count

'''
Задание 6.
Задача 7.6.
Функция, проверяющая, является ли строка сбалансированной.
Временная сложность: O(n), пространственная: O(n).
'''

def isBalanced(string1: str) -> bool:
    if string1 == '':
        return None
    test_stack = Stack()
    match = {')':'(', ']':'[', '}':'{'}
    for i in string1:
        if i not in '([{)]}':
            continue
        if i in '([{':
            test_stack.push(i)
        elif test_stack.size() == 0:
            return False
        elif i in ')]}' and test_stack.peek() == match[i]:
            test_stack.pop()
    return test_stack.size() == 0

'''
Рефлексия по решению задач задания 4.

4., 5.
Логика решения совпадает с эталонной. Для типов скобок сразу использовала словварь. 

6.
Логика решения совпадает с эталонной. 

7.
Логика решения совпадает с эталонной, за исключением того, что переменная со средним была не приватной. Учла этот нюанс в текущем уроке.

8.
В своем решении записала аргументы в одной строке, из-за чего не учитывается момент порядка вычисления. До лямбда функции сама бы пока точно не додумалась.
'''
