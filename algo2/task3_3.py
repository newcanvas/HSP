import unittest

from task3 import BST, BSTNode
from task3_2 import InvertTree, MaxSumLevel, RestoreTree


def create_tree():
    root = BSTNode(10, 10, None)
    tree = BST(root)

    tree.AddKeyValue(5, 5)
    tree.AddKeyValue(15, 15)
    tree.AddKeyValue(3, 3)
    tree.AddKeyValue(7, 7)
    tree.AddKeyValue(12, 12)
    tree.AddKeyValue(20, 20)

    return tree


def create_left_tree():
    root = BSTNode(10, 10, None)
    tree = BST(root)

    tree.AddKeyValue(5, 5)
    tree.AddKeyValue(3, 3)

    return tree


def create_right_tree():
    root = BSTNode(10, 10, None)
    tree = BST(root)

    tree.AddKeyValue(15, 15)
    tree.AddKeyValue(20, 20)

    return tree


def create_unbalanced_tree():
    root = BSTNode(10, 10, None)
    tree = BST(root)

    tree.AddKeyValue(5, 5)
    tree.AddKeyValue(7, 7)

    return tree


def node_keys(nodes):
    return [node.NodeKey for node in nodes]


class BSTTests(unittest.TestCase):

    # 1. WideAllNodes

    def test_wide_all_nodes(self):
        tree = create_tree()

        result = tree.WideAllNodes()

        self.assertIsInstance(result, tuple)
        self.assertEqual(node_keys(result), [10, 5, 15, 3, 7, 12, 20])
        self.assertIs(result[0], tree.Root)
        self.assertIs(result[1], tree.Root.LeftChild)
        self.assertIs(result[2], tree.Root.RightChild)

    def test_wide_empty_tree(self):
        tree = BST(None)

        result = tree.WideAllNodes()

        self.assertEqual(result, ())

    def test_wide_one_node(self):
        root = BSTNode(10, 10, None)
        tree = BST(root)

        result = tree.WideAllNodes()

        self.assertEqual(result, (root,))

    def test_wide_left_tree(self):
        tree = create_left_tree()

        result = tree.WideAllNodes()

        self.assertEqual(node_keys(result), [10, 5, 3])
        self.assertIsNone(tree.Root.RightChild)

    def test_wide_right_tree(self):
        tree = create_right_tree()

        result = tree.WideAllNodes()

        self.assertEqual(node_keys(result), [10, 15, 20])
        self.assertIsNone(tree.Root.LeftChild)

    def test_wide_unbalanced_tree(self):
        tree = create_unbalanced_tree()

        result = tree.WideAllNodes()

        self.assertEqual(node_keys(result), [10, 5, 7])
        self.assertIsNone(tree.Root.RightChild)
        self.assertIsNone(tree.Root.LeftChild.LeftChild)
        self.assertEqual(tree.Root.LeftChild.RightChild.NodeKey, 7)

    def test_wide_only_right_child_on_second_level(self):
        root = BSTNode(10, 10, None)
        tree = BST(root)
        tree.AddKeyValue(15, 15)
        tree.AddKeyValue(12, 12)

        result = tree.WideAllNodes()

        self.assertEqual(node_keys(result), [10, 15, 12])

    # 2. DeepAllNodes

    def test_deep_in_order(self):
        tree = create_tree()

        result = tree.DeepAllNodes(0)

        self.assertIsInstance(result, tuple)
        self.assertEqual(node_keys(result), [3, 5, 7, 10, 12, 15, 20])
        self.assertIs(result[3], tree.Root)

    def test_deep_post_order(self):
        tree = create_tree()

        result = tree.DeepAllNodes(1)

        self.assertEqual(node_keys(result), [3, 7, 5, 12, 20, 15, 10])
        self.assertIs(result[-1], tree.Root)

    def test_deep_pre_order(self):
        tree = create_tree()

        result = tree.DeepAllNodes(2)

        self.assertEqual(node_keys(result), [10, 5, 3, 7, 15, 12, 20])
        self.assertIs(result[0], tree.Root)

    def test_deep_empty_tree(self):
        tree = BST(None)

        self.assertEqual(tree.DeepAllNodes(0), ())
        self.assertEqual(tree.DeepAllNodes(1), ())
        self.assertEqual(tree.DeepAllNodes(2), ())

    def test_deep_one_node(self):
        root = BSTNode(10, 10, None)
        tree = BST(root)

        self.assertEqual(tree.DeepAllNodes(0), (root,))
        self.assertEqual(tree.DeepAllNodes(1), (root,))
        self.assertEqual(tree.DeepAllNodes(2), (root,))

    def test_deep_left_tree(self):
        tree = create_left_tree()

        self.assertEqual(node_keys(tree.DeepAllNodes(0)), [3, 5, 10])
        self.assertEqual(node_keys(tree.DeepAllNodes(1)), [3, 5, 10])
        self.assertEqual(node_keys(tree.DeepAllNodes(2)), [10, 5, 3])

    def test_deep_right_tree(self):
        tree = create_right_tree()

        self.assertEqual(node_keys(tree.DeepAllNodes(0)), [10, 15, 20])
        self.assertEqual(node_keys(tree.DeepAllNodes(1)), [20, 15, 10])
        self.assertEqual(node_keys(tree.DeepAllNodes(2)), [10, 15, 20])

    def test_deep_unbalanced_tree(self):
        tree = create_unbalanced_tree()

        self.assertEqual(node_keys(tree.DeepAllNodes(0)), [5, 7, 10])
        self.assertEqual(node_keys(tree.DeepAllNodes(1)), [7, 5, 10])
        self.assertEqual(node_keys(tree.DeepAllNodes(2)), [10, 5, 7])

    def test_deep_in_order_is_sorted_for_bst(self):
        tree = create_tree()
        keys = node_keys(tree.DeepAllNodes(0))

        self.assertEqual(keys, sorted(keys))

    # 3. InvertTree

    def test_invert_tree(self):
        tree = create_tree()

        InvertTree(tree)

        self.assertEqual(node_keys(tree.WideAllNodes()), [10, 15, 5, 20, 12, 7, 3])
        self.assertEqual(node_keys(tree.DeepAllNodes(0)), [20, 15, 12, 10, 7, 5, 3])
        self.assertEqual(node_keys(tree.DeepAllNodes(2)), [10, 15, 20, 12, 5, 7, 3])
        self.assertEqual(tree.Root.LeftChild.NodeKey, 15)
        self.assertEqual(tree.Root.RightChild.NodeKey, 5)
        self.assertEqual(tree.Root.LeftChild.Parent, tree.Root)
        self.assertEqual(tree.Root.RightChild.Parent, tree.Root)

    def test_invert_twice_restores_tree(self):
        tree = create_tree()
        original_wide = node_keys(tree.WideAllNodes())
        original_in = node_keys(tree.DeepAllNodes(0))
        original_pre = node_keys(tree.DeepAllNodes(2))

        InvertTree(tree)
        InvertTree(tree)

        self.assertEqual(node_keys(tree.WideAllNodes()), original_wide)
        self.assertEqual(node_keys(tree.DeepAllNodes(0)), original_in)
        self.assertEqual(node_keys(tree.DeepAllNodes(2)), original_pre)
        self.assertEqual(tree.Root.LeftChild.NodeKey, 5)
        self.assertEqual(tree.Root.RightChild.NodeKey, 15)

    def test_invert_empty_tree(self):
        tree = BST(None)

        InvertTree(tree)

        self.assertIsNone(tree.Root)

    def test_invert_one_node(self):
        root = BSTNode(10, 10, None)
        tree = BST(root)

        InvertTree(tree)

        self.assertIs(tree.Root, root)
        self.assertIsNone(tree.Root.LeftChild)
        self.assertIsNone(tree.Root.RightChild)

    def test_invert_left_tree_becomes_right(self):
        tree = create_left_tree()

        InvertTree(tree)

        self.assertIsNone(tree.Root.LeftChild)
        self.assertEqual(tree.Root.RightChild.NodeKey, 5)
        self.assertIsNone(tree.Root.RightChild.LeftChild)
        self.assertEqual(tree.Root.RightChild.RightChild.NodeKey, 3)
        self.assertEqual(node_keys(tree.WideAllNodes()), [10, 5, 3])
        self.assertEqual(node_keys(tree.DeepAllNodes(0)), [10, 5, 3])

    def test_invert_unbalanced_tree(self):
        tree = create_unbalanced_tree()

        InvertTree(tree)

        self.assertIsNone(tree.Root.LeftChild)
        self.assertEqual(tree.Root.RightChild.NodeKey, 5)
        self.assertEqual(tree.Root.RightChild.LeftChild.NodeKey, 7)
        self.assertIsNone(tree.Root.RightChild.RightChild)
        self.assertEqual(tree.Root.RightChild.LeftChild.Parent.NodeKey, 5)

    def test_invert_keeps_keys_and_values(self):
        tree = create_tree()
        original = {(node.NodeKey, node.NodeValue) for node in tree.WideAllNodes()}

        InvertTree(tree)

        self.assertEqual({(node.NodeKey, node.NodeValue) for node in tree.WideAllNodes()}, original)

    # 4. MaxSumLevel

    def test_max_sum_level(self):
        tree = create_tree()

        result = tree.MaxSumLevel()

        self.assertEqual(result, 2)

    def test_max_sum_empty_tree(self):
        tree = BST(None)

        result = tree.MaxSumLevel()

        self.assertEqual(result, 0)

    def test_max_sum_one_node(self):
        root = BSTNode(10, 10, None)
        tree = BST(root)

        result = tree.MaxSumLevel()

        self.assertEqual(result, 0)

    def test_max_sum_root_level_wins(self):
        root = BSTNode(100, 100, None)
        tree = BST(root)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(15, 15)

        result = tree.MaxSumLevel()

        self.assertEqual(result, 0)

    def test_max_sum_middle_level_wins(self):
        root = BSTNode(1, 1, None)
        tree = BST(root)

        left = BSTNode(50, 50, root)
        right = BSTNode(50, 50, root)
        root.LeftChild = left
        root.RightChild = right
        left.LeftChild = BSTNode(3, 3, left)
        right.RightChild = BSTNode(3, 3, right)

        result = tree.MaxSumLevel()

        self.assertEqual(result, 1)

    def test_max_sum_equal_levels_returns_first(self):
        root = BSTNode(6, 6, None)
        tree = BST(root)

        left = BSTNode(3, 3, root)
        right = BSTNode(3, 3, root)
        root.LeftChild = left
        root.RightChild = right
        left.LeftChild = BSTNode(6, 6, left)

        result = tree.MaxSumLevel()

        self.assertEqual(result, 0)

    def test_max_sum_negative_values(self):
        root = BSTNode(-20, -20, None)
        tree = BST(root)

        left = BSTNode(-1, -1, root)
        right = BSTNode(-1, -1, root)
        root.LeftChild = left
        root.RightChild = right

        result = tree.MaxSumLevel()

        self.assertEqual(result, 1)

    def test_max_sum_all_negative_root_wins(self):
        root = BSTNode(-1, -1, None)
        tree = BST(root)

        left = BSTNode(-10, -10, root)
        right = BSTNode(-2, -2, root)
        root.LeftChild = left
        root.RightChild = right

        result = tree.MaxSumLevel()

        self.assertEqual(result, 0)

    def test_max_sum_left_tree(self):
        tree = create_left_tree()

        result = tree.MaxSumLevel()

        self.assertEqual(result, 0)

    def test_max_sum_last_level_single_large_node(self):
        root = BSTNode(1, 1, None)
        tree = BST(root)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(3, 100)

        result = tree.MaxSumLevel()

        self.assertEqual(result, 2)

    def test_max_sum_zero_values(self):
        root = BSTNode(0, 0, None)
        tree = BST(root)

        left = BSTNode(0, 0, root)
        right = BSTNode(0, 0, root)
        root.LeftChild = left
        root.RightChild = right

        result = tree.MaxSumLevel()

        self.assertEqual(result, 0)

    # 5. RestoreTree

    def test_restore_tree(self):
        tree = RestoreTree([10, 5, 3, 7, 15, 12, 20], [3, 5, 7, 10, 12, 15, 20])

        self.assertEqual(node_keys(tree.DeepAllNodes(2)), [10, 5, 3, 7, 15, 12, 20])
        self.assertEqual(node_keys(tree.DeepAllNodes(0)), [3, 5, 7, 10, 12, 15, 20])
        self.assertEqual(node_keys(tree.WideAllNodes()), [10, 5, 15, 3, 7, 12, 20])
        self.assertIsNone(tree.Root.Parent)
        self.assertEqual(tree.Root.LeftChild.Parent, tree.Root)
        self.assertEqual(tree.Root.RightChild.Parent, tree.Root)
        self.assertEqual(tree.Root.LeftChild.LeftChild.Parent.NodeKey, 5)
        self.assertEqual(tree.Root.NodeValue, 10)

    def test_restore_empty_tree(self):
        tree = RestoreTree([], [])

        self.assertIsNone(tree.Root)
        self.assertEqual(tree.WideAllNodes(), ())
        self.assertEqual(tree.DeepAllNodes(0), ())

    def test_restore_one_node(self):
        tree = RestoreTree([10], [10])

        self.assertEqual(tree.Root.NodeKey, 10)
        self.assertEqual(tree.Root.NodeValue, 10)
        self.assertIsNone(tree.Root.Parent)
        self.assertIsNone(tree.Root.LeftChild)
        self.assertIsNone(tree.Root.RightChild)
        self.assertEqual(node_keys(tree.WideAllNodes()), [10])

    def test_restore_left_tree(self):
        tree = RestoreTree([10, 5, 3], [3, 5, 10])

        self.assertEqual(node_keys(tree.DeepAllNodes(2)), [10, 5, 3])
        self.assertEqual(node_keys(tree.DeepAllNodes(0)), [3, 5, 10])
        self.assertIsNone(tree.Root.RightChild)
        self.assertEqual(tree.Root.LeftChild.NodeKey, 5)
        self.assertEqual(tree.Root.LeftChild.LeftChild.NodeKey, 3)
        self.assertEqual(tree.Root.LeftChild.LeftChild.Parent.NodeKey, 5)

    def test_restore_right_tree(self):
        tree = RestoreTree([10, 15, 20], [10, 15, 20])

        self.assertEqual(node_keys(tree.DeepAllNodes(2)), [10, 15, 20])
        self.assertEqual(node_keys(tree.DeepAllNodes(0)), [10, 15, 20])
        self.assertIsNone(tree.Root.LeftChild)
        self.assertEqual(tree.Root.RightChild.NodeKey, 15)
        self.assertEqual(tree.Root.RightChild.RightChild.NodeKey, 20)
        self.assertEqual(tree.Root.RightChild.RightChild.Parent.NodeKey, 15)

    def test_restore_two_nodes_left(self):
        tree = RestoreTree([10, 5], [5, 10])

        self.assertEqual(tree.Root.NodeKey, 10)
        self.assertEqual(tree.Root.LeftChild.NodeKey, 5)
        self.assertIsNone(tree.Root.RightChild)
        self.assertEqual(tree.Root.LeftChild.Parent, tree.Root)

    def test_restore_two_nodes_right(self):
        tree = RestoreTree([10, 15], [10, 15])

        self.assertEqual(tree.Root.NodeKey, 10)
        self.assertIsNone(tree.Root.LeftChild)
        self.assertEqual(tree.Root.RightChild.NodeKey, 15)
        self.assertEqual(tree.Root.RightChild.Parent, tree.Root)

    def test_restore_round_trip(self):
        original = create_tree()
        prefix = node_keys(original.DeepAllNodes(2))
        infix = node_keys(original.DeepAllNodes(0))

        restored = RestoreTree(prefix, infix)

        self.assertEqual(node_keys(restored.DeepAllNodes(2)), prefix)
        self.assertEqual(node_keys(restored.DeepAllNodes(0)), infix)
        self.assertEqual(node_keys(restored.DeepAllNodes(1)), node_keys(original.DeepAllNodes(1)))
        self.assertEqual(node_keys(restored.WideAllNodes()), node_keys(original.WideAllNodes()))

    def test_restore_unbalanced_tree(self):
        original = create_unbalanced_tree()
        prefix = node_keys(original.DeepAllNodes(2))
        infix = node_keys(original.DeepAllNodes(0))

        restored = RestoreTree(prefix, infix)

        self.assertEqual(node_keys(restored.WideAllNodes()), [10, 5, 7])
        self.assertIsNone(restored.Root.RightChild)
        self.assertIsNone(restored.Root.LeftChild.LeftChild)
        self.assertEqual(restored.Root.LeftChild.RightChild.NodeKey, 7)
        self.assertEqual(restored.Root.LeftChild.RightChild.Parent.NodeKey, 5)

    def test_restore_non_bst_shape(self):
        tree = RestoreTree([1, 2, 3], [2, 1, 3])

        self.assertEqual(tree.Root.NodeKey, 1)
        self.assertEqual(tree.Root.LeftChild.NodeKey, 2)
        self.assertEqual(tree.Root.RightChild.NodeKey, 3)
        self.assertIsNone(tree.Root.LeftChild.LeftChild)
        self.assertIsNone(tree.Root.LeftChild.RightChild)
        self.assertEqual(node_keys(tree.WideAllNodes()), [1, 2, 3])
        self.assertEqual(node_keys(tree.DeepAllNodes(0)), [2, 1, 3])


if __name__ == '__main__':
    unittest.main()
