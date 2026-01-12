class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class Dummy_Node:
    def __init__(self, v):
        self.value = v
        self.dummy = True
        self.prev = None
        self.next = None

class LinkedList2_1:  

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

    def len(self):
        node = self.head
        list_len = 0
        while node is not None:
            list_len += 1
            node = node.next
        return list_len

    '''
    Задание 2.
    Задача 2.10.
    Метод, переворачивающая двусторонний связный список.
    Временная сложность: O(1), пространственная: O(n).
    '''

    def flip_list(self):
        if self.head is None:
            return self
        node = self.head
        while node is not None:
            node.next, node.prev = node.prev, node.next
            node = node.prev
        self.head, self.tail = self.tail, self.head
        return self
    
    '''
    Задание 2.
    Задача 2.11.
    Булев метод, возвращающий наличие циклов, замкнутых по кругу, внутри списка.
    Временная сложность: O(1), пространственная: O(n).
    '''

    def find_loop(self):
        if self.head is None:
            return False
        
        first = self.head
        second = self.head

        while second is not None and second.next is not None:
            first = first.next
            second = second.next.next
            if first == second:
                return True
        return False
        
    '''
    Задание 2.
    Задача 2.12.
    Метод, сортирующий список.
    Временная сложность: O(1), пространственная: O(n^2).
    '''

    def sort_list(self):
        if self.head is None:
            return

        end_position = self.tail

        while end_position is not self.head:
            position = self.head
            while position is not end_position:
                if position.value > position.next.value:
                    position.value, position.next.value = position.next.value, position.value
                position = position.next
            end_position = end_position.prev
        return self

    '''
    Задание 2.
    Задача 2.13., 2.14.
    Метод, объединяющий два списка в третий. Изначальные списки нужно отсортировать, финальный сортировать нельзя. 
    Реализация с использованием dummy узла.
    Временная сложность: O(1), пространственная: O(n+m).
    '''

    def merge_lists(list1, list2):
        if list1.head is None and list2.head is None:
            return
        if list1.head is None:
            return list2.sort_list()
        if list2.head is None:
            return list1.sort_list()
            
        final_list = LinkedList2_1()
        list1.sort_list()
        list2.sort_list()
        node1 = list1.head
        node2 = list2.head
        dummy = Node(-999)
        final_list.head = dummy
        final_list.tail = dummy
            
        while node1 is not None or node2 is not None:
            if node1 is None:
                final_list.tail.next = node2
                node2.prev = final_list.tail
                final_list.tail = node2
                node2 = node2.next
                continue

            if node2 is None:
                final_list.tail.next = node1
                node1.prev = final_list.tail
                final_list.tail = node1
                node1 = node1.next
                continue

            if node2.value <= node1.value:
                final_list.tail.next = node2
                node2.prev = final_list.tail
                final_list.tail = node2
                node2 = node2.next
            else:
                final_list.tail.next = node1
                node1.prev = final_list.tail
                final_list.tail = node1
                node1 = node1.next

        final_list.head = final_list.head.next
        final_list.head.prev = None

        list1.head = None
        list1.tail = None
        list2.head = None
        list2.tail = None
    
        return final_list
