import unittest
from task6 import BalancedBST, BSTNode
from task6_2 import IsBalanced, IsBalanced2

BalancedBST.IsBalanced =  IsBalanced
BalancedBST.IsBalanced2 = IsBalanced2


class TestBalancedBST(unittest.TestCase):

    def test_generate_tree_empty_array(self):
        tree = BalancedBST()
        tree.GenerateTree([])

        self.assertEqual(tree.Root, None)

    def test_generate_tree_one_element(self):
        tree = BalancedBST()
        tree.GenerateTree([5])

        self.assertEqual(tree.Root.NodeKey, 5)
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(tree.Root.Level, 0)
        self.assertEqual(tree.Root.LeftChild, None)
        self.assertEqual(tree.Root.RightChild, None)

    def test_generate_tree_sorted_array(self):
        tree = BalancedBST()
        tree.GenerateTree([1, 2, 3, 4, 5, 6, 7])

        self.assertEqual(tree.Root.NodeKey, 4)
        self.assertEqual(tree.Root.LeftChild.NodeKey, 2)
        self.assertEqual(tree.Root.RightChild.NodeKey, 6)

        self.assertEqual(tree.Root.LeftChild.Parent, tree.Root)
        self.assertEqual(tree.Root.RightChild.Parent, tree.Root)

        self.assertEqual(tree.Root.LeftChild.Level, 1)
        self.assertEqual(tree.Root.RightChild.Level, 1)
        self.assertEqual(tree.Root.LeftChild.LeftChild.Level, 2)

    def test_generate_tree_unsorted_array(self):
        tree = BalancedBST()
        tree.GenerateTree([7, 1, 5, 3, 2])

        self.assertEqual(tree.Root.NodeKey, 3)
        self.assertEqual(tree.Root.LeftChild.NodeKey, 1)
        self.assertEqual(tree.Root.RightChild.NodeKey, 5)

        self.assertEqual(tree.Root.LeftChild.RightChild.NodeKey, 2)
        self.assertEqual(tree.Root.RightChild.RightChild.NodeKey, 7)

class TestIsBalanced(unittest.TestCase):

    def test_empty_tree(self):
        tree = BalancedBST()
        self.assertEqual(tree.IsBalanced(None), True)

    def test_correct_tree(self):
        tree = BalancedBST()
        root = BSTNode(10, None)
        root.LeftChild = BSTNode(5, root)
        root.RightChild = BSTNode(15, root)

        self.assertEqual(tree.IsBalanced(root), True)

    def test_left_child_greater_than_parent(self):
        tree = BalancedBST()
        root = BSTNode(10, None)
        root.LeftChild = BSTNode(12, root)

        self.assertEqual(tree.IsBalanced(root), False)


class TestIsBalanced2(unittest.TestCase):

    def test_empty_tree(self):
        tree = BalancedBST()
        self.assertEqual(tree.IsBalanced2(None), True)

    def test_one_node(self):
        tree = BalancedBST()
        root = BSTNode(10, None)

        self.assertEqual(tree.IsBalanced2(root), True)

    def test_balanced_tree(self):
        tree = BalancedBST()
        root = BSTNode(10, None)
        root.LeftChild = BSTNode(5, root)
        root.RightChild = BSTNode(15, root)
        root.LeftChild.LeftChild = BSTNode(3, root.LeftChild)
        root.LeftChild.RightChild = BSTNode(7, root.LeftChild)
        root.RightChild.RightChild = BSTNode(20, root.RightChild)

        self.assertEqual(tree.IsBalanced2(root), True)

    def test_unbalanced_subtree(self):
        tree = BalancedBST()
        root = BSTNode(10, None)
        root.LeftChild = BSTNode(5, root)
        root.RightChild = BSTNode(15, root)
        root.LeftChild.LeftChild = BSTNode(3, root.LeftChild)
        root.LeftChild.LeftChild.LeftChild = BSTNode(
            2, root.LeftChild.LeftChild
        )

        self.assertEqual(tree.IsBalanced2(root), False)

if __name__ == '__main__':
    unittest.main()
