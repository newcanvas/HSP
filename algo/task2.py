class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        node_list = []
        while node is not None:
            if node.value == val:
                node_list.append(node)
            node = node.next
        return node_list

    def delete(self, val, all=False):
        if self.head is None:
            return self
        node = self.head
        while node is not None:
            if node.value == val:
                if node is self.head:
                    if node.next is None:
                        self.head = None
                        self.tail = None
                    else:
                        self.head = node.next
                        self.head.prev = None
                elif node is self.tail:
                    self.tail = node.prev
                    node.prev.next = None
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                if not all:
                    return self
                node = node.next
            else:
                node = node.next
        return self

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        list_len = 0
        while node is not None:
            list_len += 1
            node = node.next
        return list_len

    def insert(self, afterNode, newNode):
        if afterNode is None:
            if self.head is None:
                self.head = newNode
                self.tail = newNode
                return self
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            return self

        node = self.head
        while node is not None:
            if node is afterNode:
                newNode.next = node.next
                node.next = newNode
                node.prev = afterNode
                if node is self.tail:
                    self.tail = newNode
                    node.prev = afterNode
                return self
            node = node.next

    def add_in_head(self, newNode):
        if self.head is None:
            self.tail = newNode
            newNode.prev = None
            newNode.next = None
        else:
            self.head.prev = newNode
            newNode.next = self.head
        self.head = newNode

