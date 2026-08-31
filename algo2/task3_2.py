from task3 import BST, BSTNode

'''
Задание 3.
Задача 1.
Алгоритм инвертирования дерева.
Временная сложность: O(N), пространственная: O(N).
'''

def InvertTree(tree) -> None:
    _invert_tree_rec(tree.Root)


def _invert_tree_rec(node) -> None:
    if node is None:
        return

    node.LeftChild, node.RightChild = node.RightChild, node.LeftChild

    _invert_tree_rec(node.LeftChild)
    _invert_tree_rec(node.RightChild)


'''
Задание 3.
Задача 2.
Метод, который находит уровень в текущем дереве, сумма значений узлов на котором максимальна.
Временная сложность: O(N), пространственная: O(N).
'''

def MaxSumLevel(self) -> int:
        if self.Root is None:
            return 0

        max_sum = self.Root.NodeValue
        max_level = 0
        current_level = [self.Root]
        level = 0

        while current_level:
            current_sum = 0
            next_level = []

            for node in current_level:
                current_sum += node.NodeValue

                if node.LeftChild is not None:
                    next_level.append(node.LeftChild)

                if node.RightChild is not None:
                    next_level.append(node.RightChild)

            if current_sum > max_sum:
                max_sum = current_sum
                max_level = level

            current_level = next_level
            level += 1

        return max_level

BST.MaxSumLevel = MaxSumLevel

'''
Задание 3.
Задача 2.
Функция для восстановления оригинального дерева.
Временная сложность: O(N), пространственная: O(N).
'''
def RestoreTree(prefix, infix) -> BST:
    if not prefix:
        return BST(None)

    root_key = prefix[0]
    root_index = infix.index(root_key)

    root = BSTNode(root_key, root_key, None)

    left_prefix = prefix[1:root_index + 1]
    right_prefix = prefix[root_index + 1:]

    left_infix = infix[:root_index]
    right_infix = infix[root_index + 1:]

    root.LeftChild = _restore_tree_rec(left_prefix, left_infix, root)

    root.RightChild = _restore_tree_rec(right_prefix, right_infix, root)

    return BST(root)


def _restore_tree_rec(prefix, infix, parent) -> BSTNode:
    if not prefix:
        return None

    root_key = prefix[0]
    root_index = infix.index(root_key)

    root = BSTNode(root_key, root_key, parent)

    left_prefix = prefix[1:root_index + 1]
    right_prefix = prefix[root_index + 1:]

    left_infix = infix[:root_index]
    right_infix = infix[root_index + 1:]

    root.LeftChild = _restore_tree_rec(left_prefix,left_infix,root)

    root.RightChild = _restore_tree_rec(right_prefix, right_infix, root)

    return root

