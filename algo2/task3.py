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

    def WideAllNodes(self) -> tuple:
        all_nodes_wide = []
        if self.Root is not None:
            self._wide_all_nodes_rec([self.Root], all_nodes_wide)
        return tuple(all_nodes_wide)

    def _wide_all_nodes_rec(self, nodes, all_nodes_wide) -> list:
        if not nodes:
            return all_nodes_wide

        next_nodes = []

        for node in nodes:
            if node is None:
                continue

            all_nodes_wide.append(node)

            if node.LeftChild is not None:
                next_nodes.append(node.LeftChild)

            if node.RightChild is not None:
                next_nodes.append(node.RightChild)

        self._wide_all_nodes_rec(next_nodes, all_nodes_wide)

        return all_nodes_wide

    def DeepAllNodes(self, order) -> tuple:
        all_nodes_deep = []
        self._deep_all_nodes_rec(self.Root, order, all_nodes_deep)
        return tuple(all_nodes_deep)

    def _deep_all_nodes_rec(self, node, order, all_nodes_deep) -> list:
        if node is None:
            return all_nodes_deep

        if order == 2:
            all_nodes_deep.append(node)

        self._deep_all_nodes_rec(node.LeftChild, order, all_nodes_deep)

        if order == 0:
            all_nodes_deep.append(node)

        self._deep_all_nodes_rec(node.RightChild, order, all_nodes_deep)

        if order == 1:
            all_nodes_deep.append(node)

        return all_nodes_deep

 