class BSTNode:
    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0

class BalancedBST:
    def __init__(self):
        self.Root = None

    def GenerateTree(self, a):
        a.sort()

        def build_tree(left, right, parent, level):
            if left > right:
                return None

            middle = (left + right) // 2
            node = BSTNode(a[middle], parent)
            node.Level = level

            node.LeftChild = build_tree(left, middle - 1, node, level + 1)
            node.RightChild = build_tree(middle + 1, right, node, level + 1)

            return node

        self.Root = build_tree(0, len(a) - 1, None, 0)

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
