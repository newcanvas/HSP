from task2_2 import (IsIdentical, _is_identical_rec, IsSymmetric, _is_symmetric_rec, FindMaxSumPaths, _find_max_sum_paths, FindPathsByLengh,_find_paths_by_length)

class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


class BSTFind: # промежуточный результат поиска

    def __init__(self):
        self.Node = None # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо
        # добавить новый узел левым потомком

class BST:

    def __init__(self, node):
        self.Root = node # корень дерева, или None

    def FindNodeByKey(self, key) -> BSTFind:
        # ищем в дереве узел и сопутствующую информацию по ключу
        search_result = BSTFind()
        self._find_node_by_key(self.Root, key, search_result)
        return search_result  # возвращает BSTFind

    def _find_node_by_key(self, node, key, search_result) -> BSTFind:
        if node is None:
            return search_result

        search_result.Node = node

        if node.NodeKey == key:
            search_result.NodeHasKey = True
            return search_result

        if node.NodeKey > key:
            search_result.ToLeft = True
            self._find_node_by_key(node.LeftChild, key, search_result)

        if node.NodeKey < key:
            search_result.ToLeft = False
            self._find_node_by_key(node.RightChild, key, search_result)

        return search_result

    def AddKeyValue(self, key, val) -> bool:
        # добавляем ключ-значение в дерево

        if self.Root is None:
            self.Root = BSTNode(key, val, None)
            return True

        add_result = self.FindNodeByKey(key)

        if add_result.NodeHasKey:
            return False # если ключ уже есть

        if add_result.ToLeft:
            add_result.Node.LeftChild = BSTNode(key, val, add_result.Node)
            return True

        add_result.Node.RightChild = BSTNode(key, val, add_result.Node)
        return True


    def FinMinMax(self, FromNode, FindMax) -> BSTNode:
        # ищем максимальный/минимальный ключ в поддереве
        min_node = FromNode
        max_node = FromNode

        if FindMax:
            return self._find_max_node_rec(FromNode, FromNode)

        return self._find_min_node_rec(FromNode, FromNode)

    def _find_max_node_rec(self, FromNode, MaxNode) -> BSTNode:
        if FromNode is None:
            return MaxNode

        if FromNode.NodeKey > MaxNode.NodeKey:
            MaxNode = FromNode

        return self._find_max_node_rec(FromNode.RightChild, MaxNode)

    def _find_min_node_rec(self, FromNode, MinNode) -> BSTNode:
        if FromNode is None:
            return MinNode

        if FromNode.NodeKey < MinNode.NodeKey:
            MinNode = FromNode

        return self._find_min_node_rec(FromNode.LeftChild, MinNode)

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        delete_result = self.FindNodeByKey(key)

        if not delete_result.NodeHasKey:
            return False # если узел не найден

        delete_node = delete_result.Node

        if delete_node.LeftChild is not None:
            new_node = delete_node.LeftChild
        else:
            new_node = delete_node.RightChild

        if delete_node.Parent.LeftChild is delete_node:
            delete_node.LeftChild = new_node
        else:
            delete_node.Parent.RightChild = new_node

        return True

    def Count(self) -> int:
        return self._count_rec(self.Root)

    def _count_rec(self, node) -> int:
        if node is None:
            return 0

        return 1 + self._count_rec(node.LeftChild) + self._count_rec(node.RightChild)

    IsIdentical = IsIdentical
    _is_identical_rec = _is_identical_rec

    IsSymmetric = IsSymmetric
    _is_symmetric_rec = _is_symmetric_rec

    FindMaxSumPaths = FindMaxSumPaths
    _find_max_sum_paths = _find_max_sum_paths

    FindPathsByLengh = FindPathsByLengh
    _find_paths_by_length = _find_paths_by_length

