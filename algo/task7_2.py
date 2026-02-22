from task7 import OrderedList, Node

'''
Задание 7.
Задача 8.
Метод, удаляющий все дубликаты из списка.
Временная сложность: O(n), пространственная: O(1).
'''
def delete_double(self):
    if self.head is None:
        return
    node2 = self.head
    while node2.next is not None:
        result = self.compare(node2.value, node2.next.value)
        if result != 0:
            node2 = node2.next
            continue
        if node2.next == self.tail:
            node2.next = None
            self.tail = node2
            self.length -= 1
            return
        node2.next = node2.next.next
        node2.next.prev = node2
        self.length -= 1
        continue
    return

OrderedList.delete_double = delete_double

'''
Задание 7.
Задача 9.
Алгоритм слияния двух упорядоченных  списков в один.
Временная сложность: O(n+m), пространственная: O(1).
'''
def merge_ordered_lists(list1, list2, asc):
    final_list = OrderedList(asc)
    node1 = list1.head
    node2 = list2.head
    if node1 is None and node2 is None:
        return final_list
    if list1._OrderedList__ascending != list2._OrderedList__ascending:
        raise ValueError('Order must not be changed.')
    dummy = Node(-999)
    final_list.head = dummy
    final_list.tail = dummy

    while node1 is not None or node2 is not None:
        if node1 is None:
            final_list.tail.next = node2
            node2.prev = final_list.tail
            final_list.tail = node2
            node2 = node2.next
            final_list.length += 1
            continue
        if node2 is None:
            final_list.tail.next = node1
            node1.prev = final_list.tail
            final_list.tail = node1
            node1 = node1.next
            final_list.length += 1
            continue
        if node2.value <= node1.value:
            final_list.tail.next = node2
            node2.prev = final_list.tail
            final_list.tail = node2
            node2 = node2.next
            final_list.length += 1
            continue
        final_list.tail.next = node1
        node1.prev = final_list.tail
        final_list.tail = node1
        node1 = node1.next
        final_list.length += 1

    final_list.head = final_list.head.next
    final_list.head.prev = None

    return final_list

OrderedList.merge_ordered_lists = merge_ordered_lists

'''
Задание 7.
Задача 10.
Метод проверки наличия подсписка.
Временная сложность: O(n*m), пространственная: O(1).
'''
def find_sublist(self, sublist):
    if sublist.head is None:
        return True
    if self.head is None:
        return False
    node1 = self.head
    node1 = self.head
    while node1 is not None:
        start = node1
        node2 = sublist.head
        while start is not None and node2 is not None and \
              self.compare(start.value, node2.value) == 0:
            start = start.next
            node2 = node2.next
        if node2 is None:
            return True
        node1 = node1.next
    return False

OrderedList.find_sublist = find_sublist

'''
Задание 7.
Задача 11.
Метод, возвращающий наиболее часто повторяющееся значение.
Временная сложность: O(n), пространственная: O(1).
'''

def most_common(self):
    if self.head is None:
        return None
    return max(self._OrderedList__common_count, key=self._OrderedList__common_count.get)

OrderedList.most_common = most_common

'''
Задание 7.
Задача 12.
Реализация обращения к элементам списка по индексу за O(log(n)).
Временная сложность: O(log(n)), пространственная: O(1).
Реализация в основном файле.
'''

