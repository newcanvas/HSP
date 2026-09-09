'''
Задание 4.
Задача 1.
Проверка реализации добавлений и поиска сделана в файле task4_2.py
'''

'''
Задание 4.
Задача 2.
Поиск наименьшего общего предка (LCA).
Временная сложность: O(h^2), пространственная: O(h).
Удобство использования индеков заключается в том, что для поиска индекса следующего нужного узла можно использовать формулу, и не усложнять структуру хранением отдельных сущностей родитель/ребенок.
'''
def FindMinCommon(self, key1, key2):

    index_key1 = self.Tree.index(key1)
    index_key2 = self.Tree.index(key2)

    ancestors1 = []
    ancestors2 = []

    for i in range(len(self.Tree) - 1):
        if index_key1 == 0:
            break

        index_key1 = (index_key1 - 1) // 2
        ancestors1.append(self.Tree[index_key1])

    for i in range(len(self.Tree) - 1):
        if index_key2 == 0:
            break

        index_key2 = (index_key2 - 1) // 2
        ancestors2.append(self.Tree[index_key2])

    for ancestor in ancestors1:
        if ancestor in ancestors2:
            return ancestor

    return None

'''
Задание 4.
Задача 3.
Метод обхода дерева в ширину, оптимизированный его за счёт прямого доступа к элементам массива.
Временная сложность: O(n), пространственная: O(n).
'''
def WideAllNodes(self):

    result = []

    for node in self.Tree:
        if node is not None:
            result.append(node)

    return result

'''
Рефлексия.
3. Общая идея решения соответствует эталонной. Но посмотрела пару обучающих роликов дополнительно, чтобы до нее дойти.

4. Общая идея решения соответствует эталонной. 

'''
