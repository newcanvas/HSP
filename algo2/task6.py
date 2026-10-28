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
        a = sorted(a)

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
