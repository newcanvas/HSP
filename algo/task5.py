class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, item): # Временная сложность: O(1), пространственная: O(1).
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        self.count += 1

    def dequeue(self):  # Временная сложность: O(1), пространственная: O(1).
        if self.head is None:
            return None
        first = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.count -= 1
        return first

    def size(self):
        return self.count

