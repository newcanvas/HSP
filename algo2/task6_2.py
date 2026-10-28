'''
Задание 6.
Задача 2.
Метод проверки, действительно ли дерево получилось правильным.
Временная сложность О(N), пространственная O(h).
'''

def IsBalanced(self, root_node):
        if root_node is None:
            return True

        if root_node.LeftChild is not None:
            if root_node.LeftChild.NodeKey >= root_node.NodeKey:
                return False

        if root_node.RightChild is not None:
            if root_node.RightChild.NodeKey < root_node.NodeKey:
                return False

        return (self.IsBalanced(root_node.LeftChild)
                and self.IsBalanced(root_node.RightChild))

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
        self.IsBalanced(root_node.LeftChild)
        and self.IsBalanced(root_node.RightChild)
    )

'''
Рефлексия.
2. Общий алгоритм соответствует эталонному.

3. Общий алгоритм соответствует эталонному.
'''
