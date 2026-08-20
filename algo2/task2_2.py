from task2 import BST

'''
Задание 2.
Задача 1.
Метод, который сравнивает дерево с деревом-параметром.
Временная сложность: O(N), пространственная: O(N).
'''
def IsIdentical(self, tree) -> bool:
    return self._is_identical_rec(self.Root, tree.Root)

def _is_identical_rec(self, node1, node2)-> bool:
    if node1 is None and node2 is None:
        return True

    if node1 is None or node2 is None:
        return False

    if node1.NodeKey != node2.NodeKey:
        return False

    if node1.NodeValue != node2.NodeValue:
        return False

    left_result = self._is_identical_rec(node1.LeftChild, node2.LeftChild)

    if not left_result:
        return False

    right_result = self._is_identical_rec(node1.RightChild, node2.RightChild)

    if not right_result:
        return False

    return True

BST.IsIdentical = IsIdentical
BST._is_identical_rec = _is_identical_rec

'''
Задание 2.
Задача 2.
Метод, который нахождит все пути от корня к листьям, длина которых равна заданной величине.
Временная сложность: O(N), пространственная: O(N).
'''
def FindPathsByLength(self, length) -> list:
    paths = []
    self._find_paths_by_length(self.Root, length, [], paths)
    return paths


def _find_paths_by_length(self, node, length, path, paths) -> list:
    if node is None:
        return

    path.append(node.NodeKey)

    if node.LeftChild is None and node.RightChild is None:
        if len(path) == length:
            paths.append(path.copy())

    self._find_paths_by_length(node.LeftChild, length, path, paths)
    self._find_paths_by_length(node.RightChild, length, path, paths)

    path.pop()

BST.FindPathsByLength = FindPathsByLength
BST._find_paths_by_length = _find_paths_by_length

'''
Задание 2.
Задача 3.
Метод, который находит все пути от корня к листьям, чтобы сумма значений узлов на этом пути была максимальной.
Временная сложность: O(N), пространственная: O(N).
'''

def FindMaxSumPaths(self) -> list:
    if self.Root is None:
        return []

    paths = []
    max_sum = [self.Root.NodeValue]

    self._find_max_sum_paths(self.Root, [], 0, max_sum, paths)

    return paths

def _find_max_sum_paths(self, node, path, current_sum, max_sum, paths):
    if node is None:
        return

    path.append(node.NodeKey)
    current_sum += node.NodeValue

    if node.LeftChild is None and node.RightChild is None:
        if current_sum > max_sum[0]:
            max_sum[0] = current_sum
            paths.clear()
            paths.append(path.copy())

        elif current_sum == max_sum[0]:
            paths.append(path.copy())

    self._find_max_sum_paths(node.LeftChild, path, current_sum, max_sum, paths)
    self._find_max_sum_paths(node.RightChild, path, current_sum, max_sum, paths)

    path.pop()

BST.FindMaxSumPaths = FindMaxSumPaths
BST._find_max_sum_paths = _find_max_sum_paths

'''
Задание 2.
Задача 4.
Метод, который проверяет, симметрично ли дерево относительно своего корня.
Временная сложность: O(N), пространственная: O(N).
'''
def IsSymmetric(self) -> bool:
    if self.Root is None:
        return True

    return self._is_symmetric_rec(self.Root.LeftChild, self.Root.RightChild)

def _is_symmetric_rec(self, node1, node2) -> bool:
    if node1 is None and node2 is None:
        return True

    if node1 is None or node2 is None:
        return False

    if node1.NodeKey != node2.NodeKey:
        return False

    if not self._is_symmetric_rec(node1.LeftChild, node2.RightChild):
        return False

    if not self._is_symmetric_rec(node1.RightChild, node2.LeftChild):
        return False

    return True

BST.IsSymmetric = IsSymmetric
BST._is_symmetric_rec = _is_symmetric_rec
