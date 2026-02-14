class Node:

    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        self._min_deque = []

    def addFront(self, item):
        item = Node(item)
        if self.head is None:
            self.tail = item
        else:
            self.head.prev = item
        item.next = self.head
        self.head = item
        self.count += 1
        if isinstance(item.value, int):
            while self._min_deque and self._min_deque[-1] > item.value:
                self._min_deque.pop()
            self._min_deque.append(item.value)

    def addTail(self, item):
        item = Node(item)
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        item.prev = self.tail
        self.tail = item
        self.count += 1
        if isinstance(item.value, int):
            while self._min_deque and self._min_deque[-1] > item.value:
                self._min_deque.pop()
            self._min_deque.append(item.value)

    def removeFront(self):
        if self.head is None:
            return None
        first = self.head.value
        self.count -= 1
        if self.head.next is None:
            self.head = None
            self.tail = None
            return first
        self.head = self.head.next
        self.head.prev = None
        if self._min_deque and first == self._min_deque[0]:
            self._min_deque.pop(0)
        return first

    def removeTail(self):
        if self.head is None:
            return None
        last = self.tail.value
        self.count -= 1
        if self.head.next is None:
            self.head = None
            self.tail = None
            return last
        self.tail = self.tail.prev
        self.tail.next = None
        if self._min_deque and last == self._min_deque[0]:
            self._min_deque.pop(0)
        return last

    def size(self):
        return self.count

'''
# 7.1.
В моей реализации с помощью двунаправленного связного списка мера сложности для addHead/removeHead и addTail/removeTail не будет отличаться.
Сдвига не происходит ни в одном из методов, но все они выполняются за O(n) за счет pop() для поиска минимального значения. Если убрать этот функционал, то сложность O(n).
'''

