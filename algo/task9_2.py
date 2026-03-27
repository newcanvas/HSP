from task7 import OrderedList
from task9 import NativeDictionary

'''
Задание 9.
Задача 5.
Реализация словаря с использованием упорядоченного списка по ключу.
Сложность операции вставки O(n).
Сложность операции удаления O(n).
Сложность операции поиска O(log n).
'''

class OrderedNativeDictionary:
    def __init__(self, size, asc=True):
        self.dict = NativeDictionary(size)
        self.keys = OrderedList(asc)

    def put(self, key, value):
        if not self.dict.is_key(key):
            self.keys.add(key)
        self.dict.put(key, value)

    def get(self, key):
        return self.dict.get(key)

    def delete(self, key):
        if not self.dict.is_key(key):
            return
        self.keys.delete(key)
        self.dict.remove(key)

    def is_key(self, key):
        return self.dict.is_key(key)

    def get_by_index(self, index):
        node = self.keys.get_by_index(index)
        if node is None:
            return None
        return (node.value, self.dict.get(node.value))

'''
Задание 9.
Задача 6.
Реализация словаря с помощью битовых операций.
Сложность операции вставки O(1).
Сложность операции удаления O(1).
'''

class BitNativeDictionary:
    def __init__(self, bit_length):
        self.bit_length = bit_length
        self.size = 1 << bit_length
        self.values = [None] * self.size
        self.mask = 0

    def to_index(self, key):
        return int(key, 2)

    def put(self, key, value):
        i = self.to_index(key)
        self.mask |= 1 << i
        self.values[i] = value

    def get(self, key):
        i = self.to_index(key)
        if not self.mask >> i & 1:
            return None
        return self.values[i]

    def delete(self, key):
        i = self.to_index(key)
        if not self.mask >> i & 1:
            return
        self.mask &= ~(1 << i)
        self.values[i] = None

    def is_key(self, key):
        i = self.to_index(key)
        return bool(self.mask >> i & 1)

    def len(self):
        return bin(self.mask).count('1')

'''
Рефлексия по решению задач задания 7.

9. Слияние двух упорядоченных списков в один.
Логика решения совпадает с эталонной.

10. Проверка наличия заданного упорядоченного под-списка в текущем списке.
Общий алгоритм поиска совпадает с приведенными шагами для поиска, но не учла прерывание поиска в ситуации, когда оставшаяся часть списка короче подсписка.

11. Ищем наиболее часто встречающееся значение в списке.
Немного переусложнила и добавила поле подсчета в основное тело класса.

12. Индекс заданного элемента в списке за O(log N).
Тут очень сильно переусложнила, зацепилась за skip list и именно через него и сделала. 
Но очень много пришлось дополнительно гуглить и смотреть материала, и все равно не довольна реализацией. 
'''
