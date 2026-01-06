class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

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
            return
        node = self.head
        prev = None
        while node is not None:
            if node.value == val:
                if prev is None:
                    self.head = node.next
                else:
                    prev.next = node.next
                if node is self.tail:
                    self.tail = prev
                if not all:
                    return
                node = node.next
            else:
                prev = node
                node = node.next

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
            newNode.next = self.head
            self.head = newNode
            if self.tail is None:
                self.tail = newNode
            return

        node = self.head
        while node is not None:
            if node is afterNode:
                newNode.next = node.next
                node.next = newNode
                if node is self.tail:
                    self.tail = newNode
                return
            node = node.next


