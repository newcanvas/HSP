from task1 import SimpleTree, SimpleTreeNode

'''
Задание 9.
Задача 2.
Метод, который балансирует чётное двоичное дерево.
Временная сложность: O(N), пространственная: O(N).
'''
def BalanceEvenTree(self):
    if self.Root is None:
        return None

    ordered_values = []

    def inorder(node) -> None:
        if node is None:
            return

        if len(node.Children) > 0:
            inorder(node.Children[0])

        ordered_values.append(node.NodeValue)

        if len(node.Children) > 1:
            inorder(node.Children[1])

    inorder(self.Root)

    def build(left, right, parent):
        if left > right:
            return None

        size = right - left + 1
        middle = left + size // 2
        node = SimpleTreeNode(ordered_values[middle], parent)

        for child in (build(left, middle - 1, node), build(middle + 1, right, node)):
            if child is not None:
                node.Children.append(child)

        return node

    self.Root = build(0, len(ordered_values) - 1, None)

    return self.Root

SimpleTree.BalanceEvenTree = BalanceEvenTree

'''
Задание 9.
Задача 3.
Метод, который для любого заданного подузла дерева определяет общее количество
чётных поддеревьев внутри него.
Временная сложность: O(N), пространственная: O(N).
'''
def CountEvenSubtrees(self, node) -> int:
    if node is None:
        return 0

    def visit(current):
        size = 1
        count = 0

        for child in current.Children:
            child_size, child_count = visit(child)
            size += child_size
            count += child_count

        if size % 2 == 0:
            count += 1

        return size, count

    result = visit(node)

    return result[1]

SimpleTree.CountEvenSubtrees = CountEvenSubtrees

'''
Рефлексия.
4. Идея совпадает с эталонной и в среднем быстрее полного
перебора, но в худшем случае всё равно O(N): заранее посчитанных максимумов для
произвольных поддиапазонов в куче нет.

5. Обход по массиву совпадает с эталонным алгоритмом, но вариант на хэш-таблице не использовала.

6. При объединении я извлекала элементы из кучи-параметра напрямую, из-за чего она
менялась в процессе. По рекомендации стоило сначала сделать копию структуры и сливать уже её,
чтобы не изменять переданную кучу.
'''

