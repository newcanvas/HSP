'''
Задание 7.
Задача 4.
Метод поиска максимального элемента в заданном диапазоне значений.
Временная сложность О(N), пространственная O(N).
'''

def FindMaxInRange(self, low, high):
    result = -1
    size = len(self.HeapArray)
    stack = [0]

    while stack:
        index = stack.pop()

        if index >= size or self.HeapArray[index] is None:
            continue

        key = self.HeapArray[index]

        if key < low:
            continue

        if key <= high:
            result = max(result, key)
            continue

        stack.append(2 * index + 1)
        stack.append(2 * index + 2)

    return result

'''
Задание 7.
Задача 5.
Метод поиска элемента меньше заданного значения.
Временная сложность О(N/2), пространственная O(1).
'''

def FindLess(self, value):
    count = self._count()

    for index in range(count // 2, count):
        if self.HeapArray[index] < value:
            return self.HeapArray[index]

    return -1

'''
Задание 7.
Задача 5.
Метод поиска всех элементов больше заданного значения.
Временная сложность О(num), пространственная O(num). Num - количество найденных элементов.
'''

def FindAllGreater(self, value):
    result = []
    size = len(self.HeapArray)
    stack = [0]

    while stack:
        index = stack.pop()

        if index >= size or self.HeapArray[index] is None:
            continue

        if self.HeapArray[index] <= value:
            continue

        result.append(self.HeapArray[index])
        stack.append(2 * index + 1)
        stack.append(2 * index + 2)

    return result

'''
Задание 7.
Задача 6.
Метод объединения текущей кучи с кучей-параметром.
Временная сложность О(log(N + M)), пространственная O(N + M).
'''

def Merge(self, other):
    key = other.GetMax()

    while key != -1:
        if not self.Add(key):
            self.HeapArray.extend([None] * (len(self.HeapArray) + 1))
            self.Add(key)

        key = other.GetMax()

'''
Рефлексия.
2. Оценку сложности поиска дала верную, но не учла практическую сторону: насколько актуальна память и насколько дерево заполнено.
Для (почти) полного дерева массив лучше, так как эффективнее использует кэши.

3. Мое решенее менее удачное. Я каждый раз заново сортирую значения и перестраивю всё дерево, это O(N log N) на одно удаление. В эталонном решении удаление локальноеб из-за чего для сбалансированного дерева это O(log N).
'''
