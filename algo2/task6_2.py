'''
Задание 6.
Задача 2.
Метод проверки, действительно ли дерево получилось правильным.
Временная сложность О(N), пространственная O(h).
'''

def IsBalanced(self, root_node):
    def height(node):
        if node is None:
            return 0

        left_height = height(node.LeftChild)
        if left_height == -1:
            return -1

        right_height = height(node.RightChild)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    return height(root_node) != -1

'''
Задание 6.
Задача 2.
Метод проверки, действительно ли дерево получилось правильным с тремя условиями.
Временная сложность О(N^2), пространственная O(h).
'''

def IsBalanced2(self, root_node):
    if root_node is None:
        return True

    def height(node):
        if node is None:
            return 0

        return 1 + max(
            height(node.LeftChild),
            height(node.RightChild)
        )

    left_height = height(root_node.LeftChild)
    right_height = height(root_node.RightChild)

    if left_height - right_height > 1:
        return False

    if right_height - left_height > 1:
        return False

    return (
        self.IsBalanced2(root_node.LeftChild)
        and self.IsBalanced2(root_node.RightChild)
    )

'''
Рефлексия.
2. Общий алгоритм соответствует эталонному.

3. Общий алгоритм соответствует эталонному.
'''
