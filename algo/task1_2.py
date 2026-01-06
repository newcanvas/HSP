'''
Задание 1.
Задача 1.8.
Функция, выводящая список сумм элементов двух связных списков одной длины.
Временная сложность: O(n), пространственная: O(n).
'''

def list_summ(s_list1, s_list2):
    if s_list1.len() != s_list2.len():
        return
    summ_list = []
    if s_list1.len() == 0:
        return summ_list
    node1 = s_list1.head
    node2 = s_list2.head
    while node1 is not None:
        summ = node1.value + node2.value
        summ_list.append(summ)
        node1 = node1.next
        node2 = node2.next
    return summ_list

