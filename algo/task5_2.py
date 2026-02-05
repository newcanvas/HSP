from task5 import Node

'''
Задание 5.
Задача 3.
Функция, вращающая очередь на N элементов по кругу.
Временная сложность: O(n), пространственная: O(1).
'''

def rotateQueue(queue, N):
    if queue.count == 0:
        return None
    for i in range(N):
        queue.enqueue(Node(queue.dequeue()))
    return queue

'''
Задание 5.
Задача 4.
Реализация очереди с помощью двух стеков.
'''

class Stack:
    def __init__(self):
        self.count = 0
        self.stack = []

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.stack[i]

    def size(self):
        return self.count

    def pop(self):
        if self.count == 0:
            return None
        self.count -= 1
        return self.stack.pop(-1)

    def push(self, value):
        self.count += 1
        self.stack.append(value)

    def peek(self):
        if self.count == 0:
            return None
        return self.stack[-1]

class Queue_2():
    def __init__(self):
        self.count = 0
        self.first_stack = Stack()
        self.second_stack = Stack()

    def size(self):
        return self.count

    def enqueue(self, value):
        self.first_stack.push(value)
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            return None
        for i in range(self.count):
            self.second_stack.push(self.first_stack.pop())
        first = self.second_stack[self.count-1]
        self.second_stack.pop()
        self.count -= 1
        for i in range(self.count):
            self.first_stack.push(self.second_stack.pop())
        return first

'''
Задание 5.
Задача 5.
Функция, которая обращает все элементы в очереди в обратном порядке.
Временная сложность: O(n), пространственная: O(n).
'''
def reverseQueue(queue):
    if queue.size() == 0:
        return None
    stack = Stack()
    while queue.size() > 0:
        stack.push(queue.dequeue())
    while stack.size() > 0:
        queue.enqueue(Node(stack.pop()))
    return queue

'''
Задание 5.
Задача 6.
Реализация круговой очереди статическим массивом фиксированного размера.
'''
class Queue_3():
    def __init__(self):
        self.qu = [0,0,0,0,0]
        self.space = 5
        self.count = 0
        self.en = 0
        self.de = 0

    def size(self):
        return self.count

    def enqueue(self, value):
        if self.count == self.space:
            raise Exception("Not enough space.")
        self.qu[self.en] = value
        self.count += 1
        if self.en == (self.space - 1):
            self.en = 0
        else:
            self.en += 1

    def dequeue(self):
        if self.count == 0:
            return None
        first = self.qu[self.de]
        self.count -= 1
        if self.de == (self.space - 1):
            self.de = 0
        else:
            self.de += 1
        return first

'''
Рефлексия по решению задач задания 3.

6. Динамический массив на основе банковского метода.
Общая логика для методов вставки и реаллокации начисления схожа с эталонной.
Не добавила метод delete, сейчас не могу представить почему, но логика из-за этого недостаточная.

7. Многомерный динамический массив.
Очень сильно переусложнила логику добавления, эталонное решение гораздо более элегантное и понятное.
'''
