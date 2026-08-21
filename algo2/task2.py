class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:

    def __init__(self):
        self.Node = None

        self.NodeHasKey = False
        self.ToLeft = False

class BST:

    def __init__(self, node):
        self.Root = node

    def FindNodeByKey(self, key) -> BSTFind:
        search_result = BSTFind()
        self._find_node_by_key(self.Root, key, search_result)
        return search_result

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

        if self.Root is None:
            self.Root = BSTNode(key, val, None)
            return True

        add_result = self.FindNodeByKey(key)

        if add_result.NodeHasKey:
            return False

        if add_result.ToLeft:
            add_result.Node.LeftChild = BSTNode(key, val, add_result.Node)
            return True

        add_result.Node.RightChild = BSTNode(key, val, add_result.Node)
        return True


    def FinMinMax(self, FromNode, FindMax) -> BSTNode:
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
        delete_result = self.FindNodeByKey(key)

        if not delete_result.NodeHasKey:
            return False

        delete_node = delete_result.Node

        if delete_node.LeftChild is not None and delete_node.RightChild is not None:
            successor = self.FinMinMax(delete_node.RightChild, False)
            delete_node.NodeKey = successor.NodeKey
            delete_node.NodeValue = successor.NodeValue
            delete_node = successor

        if delete_node.LeftChild is not None:
            new_node = delete_node.LeftChild
        else:
            new_node = delete_node.RightChild

        if new_node is not None:
            new_node.Parent = delete_node.Parent

        if delete_node.Parent is None:
            self.Root = new_node
            return True

        if delete_node.Parent.LeftChild is delete_node:
            delete_node.Parent.LeftChild = new_node
        else:
            delete_node.Parent.RightChild = new_node

        return True

    def Count(self) -> int:
        return self._count_rec(self.Root)

    def _count_rec(self, node) -> int:
        if node is None:
            return 0

        return 1 + self._count_rec(node.LeftChild) + self._count_rec(node.RightChild)

