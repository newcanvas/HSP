import unittest

from task1 import SimpleTree, SimpleTreeNode
from task9 import EvenTrees
from task9_2 import BalanceEvenTree, CountEvenSubtrees

SimpleTree.EvenTrees = EvenTrees
SimpleTree.BalanceEvenTree = BalanceEvenTree
SimpleTree.CountEvenSubtrees = CountEvenSubtrees


def build(value, *children):
    node = SimpleTreeNode(value, None)
    for child in children:
        child.Parent = node
        node.Children.append(child)
    return node


def left_child(node):
    if len(node.Children) > 0:
        return node.Children[0]
    return None


def right_child(node):
    if len(node.Children) > 1:
        return node.Children[1]
    return None


def inorder_values(node):
    if node is None:
        return []
    return (
        inorder_values(left_child(node))
        + [node.NodeValue]
        + inorder_values(right_child(node))
    )


def height(node):
    if node is None:
        return 0
    child_heights = [height(child) for child in node.Children]
    return 1 + (max(child_heights) if child_heights else 0)


def is_balanced(node):
    if node is None:
        return True
    if abs(height(left_child(node)) - height(right_child(node))) > 1:
        return False
    return is_balanced(left_child(node)) and is_balanced(right_child(node))


class TestEvenTrees(unittest.TestCase):

    def test_empty_tree(self):
        tree = SimpleTree(None)

        self.assertEqual(tree.EvenTrees(), [])

    def test_single_node(self):
        tree = SimpleTree(build(1))

        self.assertEqual(tree.EvenTrees(), [])

    def test_child_subtree_is_odd(self):
        tree = SimpleTree(build(1, build(2)))

        self.assertEqual(tree.EvenTrees(), [])

    def test_star_has_no_cuts(self):
        tree = SimpleTree(build(1, build(2), build(3), build(4)))

        self.assertEqual(tree.EvenTrees(), [])

    def test_cuts_only_even_subtrees(self):
        node1 = build(1, build(3, build(4)), build(6, build(7)))
        tree = SimpleTree(build(0, node1))

        result = tree.EvenTrees()

        self.assertEqual([node.NodeValue for node in result], [1, 3, 1, 6])

    def test_result_pairs_are_parent_and_child(self):
        node3 = build(3, build(4))
        node6 = build(6, build(7))
        node1 = build(1, node3, node6)
        tree = SimpleTree(build(0, node1))

        result = tree.EvenTrees()

        self.assertIs(result[0], node1)
        self.assertIs(result[1], node3)
        self.assertIs(result[2], node1)
        self.assertIs(result[3], node6)
        self.assertIs(result[1].Parent, result[0])
        self.assertIs(result[3].Parent, result[2])

    def test_path_of_four(self):
        tree = SimpleTree(build(1, build(2, build(3, build(4)))))

        result = tree.EvenTrees()

        self.assertEqual([node.NodeValue for node in result], [2, 3])

    def test_several_even_branches(self):
        root = build(
            1,
            build(2, build(3)),
            build(4, build(5)),
            build(6),
        )
        tree = SimpleTree(root)

        result = tree.EvenTrees()

        self.assertEqual([node.NodeValue for node in result], [1, 2, 1, 4])


class TestBalanceEvenTree(unittest.TestCase):

    def test_empty_tree(self):
        tree = SimpleTree(None)

        result = tree.BalanceEvenTree()

        self.assertIsNone(result)
        self.assertIsNone(tree.Root)

    def test_single_node(self):
        tree = SimpleTree(build(1))

        tree.BalanceEvenTree()

        self.assertEqual(tree.Root.NodeValue, 1)
        self.assertTrue(is_balanced(tree.Root))

    def test_left_chain_becomes_balanced(self):
        tree = SimpleTree(build(1, build(2, build(3, build(4)))))

        self.assertFalse(is_balanced(tree.Root))

        tree.BalanceEvenTree()

        self.assertTrue(is_balanced(tree.Root))

    def test_keeps_all_values(self):
        tree = SimpleTree(build(1, build(2, build(3, build(4, build(5, build(6)))))))

        tree.BalanceEvenTree()

        self.assertEqual(sorted(inorder_values(tree.Root)), [1, 2, 3, 4, 5, 6])

    def test_inorder_is_preserved(self):
        tree = SimpleTree(build(1, build(2, build(3, build(4)))))
        before = inorder_values(tree.Root)

        tree.BalanceEvenTree()

        self.assertEqual(inorder_values(tree.Root), before)

    def test_already_balanced_stays_balanced(self):
        tree = SimpleTree(build(2, build(1), build(3)))

        tree.BalanceEvenTree()

        self.assertTrue(is_balanced(tree.Root))
        self.assertEqual(inorder_values(tree.Root), [1, 2, 3])

    def test_parent_links_are_correct(self):
        tree = SimpleTree(build(1, build(2, build(3, build(4, build(5))))))

        tree.BalanceEvenTree()

        self.assertIsNone(tree.Root.Parent)
        for node in tree.GetAllNodes():
            for child in node.Children:
                self.assertIs(child.Parent, node)


class TestCountEvenSubtrees(unittest.TestCase):

    def test_none_node(self):
        tree = SimpleTree(build(1))

        self.assertEqual(tree.CountEvenSubtrees(None), 0)

    def test_leaf(self):
        leaf = build(3)
        tree = SimpleTree(build(1, leaf))

        self.assertEqual(tree.CountEvenSubtrees(leaf), 0)

    def test_count_includes_given_node(self):
        tree = SimpleTree(build(1, build(2)))

        self.assertEqual(tree.CountEvenSubtrees(tree.Root), 1)

    def test_node_with_odd_subtree_counts_inner_evens(self):
        node3 = build(3)
        node2 = build(2, node3)
        node5 = build(5)
        node4 = build(4, node5)
        root = build(1, node2, node4)
        tree = SimpleTree(root)

        self.assertEqual(tree.CountEvenSubtrees(root), 2)

    def test_subnode_count(self):
        node3 = build(3)
        node2 = build(2, node3)
        node5 = build(5)
        node4 = build(4, node5)
        root = build(1, node2, node4)
        tree = SimpleTree(root)

        self.assertEqual(tree.CountEvenSubtrees(node2), 1)
        self.assertEqual(tree.CountEvenSubtrees(node4), 1)
        self.assertEqual(tree.CountEvenSubtrees(node3), 0)

    def test_nested_even_subtrees(self):
        inner = build(2, build(4))
        root = build(1, inner, build(3))
        tree = SimpleTree(root)

        self.assertEqual(tree.CountEvenSubtrees(root), 2)
        self.assertEqual(tree.CountEvenSubtrees(inner), 1)

    def test_chain_of_four(self):
        tree = SimpleTree(build(1, build(2, build(3, build(4)))))

        self.assertEqual(tree.CountEvenSubtrees(tree.Root), 2)


if __name__ == '__main__':
    unittest.main()
