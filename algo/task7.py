import random

max_level = 16
P = 0.5

class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None
        self.forward = [None] * max_level
        self.span = [0] * max_level


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.length = 0
        self.__ascending = asc
        self.__common_count = {}
        self.__sl_head = Node(None)
        self.__level = 1

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
        return 0

    def add(self, value):
        self.length += 1
        add_node = Node(value)
        if value not in self.__common_count:
            self.__common_count[value] = 0
        self.__common_count[value] += 1

        if self.head is None:
            self.head = add_node
            self.tail = add_node
        else:
            node2 = self.head
            while node2 is not None:
                result = self.compare(value, node2.value)
                if (self.__ascending and result <= 0) or (not self.__ascending and result >= 0):
                    break
                node2 = node2.next
            if node2 == self.head:
                self.head.prev = add_node
                add_node.next = self.head
                self.head = add_node
            elif node2 is None:
                self.tail.next = add_node
                add_node.prev = self.tail
                self.tail = add_node
            else:
                node2.prev.next = add_node
                add_node.prev = node2.prev
                add_node.next = node2
                node2.prev = add_node

        pos = 0
        cur = self.head
        while cur is not None and cur is not add_node:
            pos += 1
            cur = cur.next

        update = [self.__sl_head] * max_level
        rank = [0] * max_level
        cur = self.__sl_head
        for i in reversed(range(self.__level)):
            rank[i] = rank[i + 1] if i < self.__level - 1 else 0
            while cur.forward[i] is not None and rank[i] + cur.span[i] <= pos:
                rank[i] += cur.span[i]
                cur = cur.forward[i]
            update[i] = cur

        lvl = 1
        while random.random() < P and lvl < max_level:
            lvl += 1

        if lvl > self.__level:
            for i in range(self.__level, lvl):
                update[i] = self.__sl_head
                update[i].span[i] = self.length - 1
            self.__level = lvl

        add_node.forward = [None] * max_level
        add_node.span = [0] * max_level
        for i in range(lvl):
            add_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = add_node
            add_node.span[i] = update[i].span[i] - (pos - rank[i])
            update[i].span[i] = pos - rank[i] + 1
        for i in range(lvl, self.__level):
            update[i].span[i] += 1

    def find(self, val):
        if self.head is None:
            return None
        node2 = self.head
        while node2 is not None:
            result = self.compare(val, node2.value)
            if (self.__ascending and result == -1) or (not self.__ascending and result == 1):
                return None
            if result == 0:
                return node2
            node2 = node2.next
        return None

    def delete(self, val):
        if self.head is None:
            return
        if val in self.__common_count:
            self.__common_count[val] -= 1
        del_node = self.head
        while del_node is not None:
            if self.compare(val, del_node.value) == 0:
                break
            del_node = del_node.next
        if del_node is None:
            return

        pos = 0
        cur = self.head
        while cur is not None and cur is not del_node:
            pos += 1
            cur = cur.next

        update = [self.__sl_head] * max_level
        rank = [0] * max_level
        cur = self.__sl_head
        for i in reversed(range(self.__level)):
            rank[i] = rank[i + 1] if i < self.__level - 1 else 0
            while cur.forward[i] is not None and rank[i] + cur.span[i] <= pos:
                rank[i] += cur.span[i]
                cur = cur.forward[i]
            update[i] = cur

        for i in range(self.__level):
            if update[i].forward[i] is del_node:
                update[i].span[i] += del_node.span[i] - 1
                update[i].forward[i] = del_node.forward[i]
            else:
                update[i].span[i] -= 1

        while self.__level > 1 and self.__sl_head.forward[self.__level - 1] is None:
            self.__level -= 1

        if del_node == self.head and del_node == self.tail:
            self.head = None
            self.tail = None
        elif del_node == self.head:
            self.head.next.prev = None
            self.head = self.head.next
        elif del_node == self.tail:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            del_node.prev.next = del_node.next
            del_node.next.prev = del_node.prev
        self.length -= 1

    def get_by_index(self, index):
        if index < 0 or index >= self.length:
            return None
        cur = self.__sl_head
        traversed = 0
        for i in reversed(range(self.__level)):
            while cur.forward[i] is not None and traversed + cur.span[i] <= index:
                traversed += cur.span[i]
                cur = cur.forward[i]
        return cur.forward[0]

    def clean(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc
        self.length = 0
        self.__common_count = {}
        self.__sl_head = Node(None)
        self.__level = 1

    def len(self):
        return self.length

    def get_all(self):
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        if v1.strip() < v2.strip():
            return -1
        if v1.strip() > v2.strip():
            return 1
        return 0

'''
5. По сравнению с операцией в классе LinkedList сложность не изменилась, пространственная и временная сложности O(n). 
Увеличилась только цикломатическая сложность за счет добавления дополнительных условий.
'''

