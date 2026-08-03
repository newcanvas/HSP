import unittest

from task1 import SimpleTree, SimpleTreeNode
from task1_2 import SimpleTreeNodeWithLevel, AddLevels 

class DivTests(unittest.TestCase):

    def test_add_child(self):
        root = SimpleTreeNode(8, None)
        tree = SimpleTree(root)
        node1 = SimpleTreeNode(8, root)
        tree.AddChild(root, node1)
        self.assertEqual(root.Children, [node1])
        self.assertEqual(node1.Parent, root)

    def test_remove_node(self):
        root = SimpleTreeNode(8, None)
        tree = SimpleTree(root)
        node1 = SimpleTreeNode(8, root)
        tree.AddChild(root, node1)
        tree.DeleteNode(node1)
        self.assertEqual(root.Children, [])
        self.assertEqual(node1.Parent, None)

    def test_get_all_nodes(self):
        root = SimpleTreeNode(8, None)
        tree = SimpleTree(root)
        node1 = SimpleTreeNode(8, root)
        tree.AddChild(root, node1)
        node2 = SimpleTreeNode(2, node1)
        tree.AddChild(node1, node2)
        node3 = SimpleTreeNode(3, node2)
        tree.AddChild(node2, node3)
        node4 = SimpleTreeNode(4, node2)
        tree.AddChild(node2, node4)
        self.assertEqual(set(tree.GetAllNodes()), {root, node1, node2, node3, node4})
    
    def test_get_by_value(self):
        root = SimpleTreeNode(8, None)
        tree = SimpleTree(root)
        node1 = SimpleTreeNode(8, root)
        tree.AddChild(root, node1)
        node2 = SimpleTreeNode(2, node1)
        tree.AddChild(node1, node2)
        node3 = SimpleTreeNode(3, node2)
        tree.AddChild(node2, node3)
        node4 = SimpleTreeNode(4, node2)
        tree.AddChild(node2, node4)
        self.assertEqual(set(tree.FindNodesByValue(8)), {root, node1})

    def test_move_tree(self):
        root = SimpleTreeNode(8, None)
        tree = SimpleTree(root)
        node1 = SimpleTreeNode(8, root)
        tree.AddChild(root, node1)
        node2 = SimpleTreeNode(2, node1)
        tree.AddChild(node1, node2)
        node3 = SimpleTreeNode(3, node2)
        tree.AddChild(node2, node3)
        node4 = SimpleTreeNode(4, node2)
        tree.AddChild(node2, node4)
        tree.MoveNode(node2, root)
        self.assertEqual(node2.Parent, root)
        self.assertEqual(set(root.Children), {node1, node2})
        self.assertEqual(node1.Children, [])

    def test_count_all_nodes(self):
        root = SimpleTreeNode(8, None)
        tree = SimpleTree(root)
        node1 = SimpleTreeNode(8, root)
        tree.AddChild(root, node1)
        node2 = SimpleTreeNode(2, node1)
        tree.AddChild(node1, node2)
        node3 = SimpleTreeNode(3, node2)
        tree.AddChild(node2, node3)
        node4 = SimpleTreeNode(4, node2)
        tree.AddChild(node2, node4)
        self.assertEqual(tree.Count(), 5)

    def test_count_all_leaves(self):
        root = SimpleTreeNode(8, None)
        tree = SimpleTree(root)
        node1 = SimpleTreeNode(8, root)
        tree.AddChild(root, node1)
        node2 = SimpleTreeNode(2, node1)
        tree.AddChild(node1, node2)
        node3 = SimpleTreeNode(3, node2)
        tree.AddChild(node2, node3)
        node4 = SimpleTreeNode(4, node2)
        tree.AddChild(node2, node4)
        self.assertEqual(tree.LeafCount(), 2)

    # 1.

    def test_root_level(self):
        root = SimpleTreeNode(8, None)

        AddLevels(root)

        self.assertEqual(root.Level, 0)


    def test_levels_in_deep_tree(self):
        root = SimpleTreeNode(8, None)
        tree = SimpleTree(root)

        node1 = SimpleTreeNode(1, root)
        tree.AddChild(root, node1)

        node2 = SimpleTreeNode(2, node1)
        tree.AddChild(node1, node2)

        node3 = SimpleTreeNode(3, node2)
        tree.AddChild(node2, node3)

        AddLevels(root)

        self.assertEqual(root.Level, 0)
        self.assertEqual(node1.Level, 1)
        self.assertEqual(node2.Level, 2)
        self.assertEqual(node3.Level, 3)


    def test_children_have_same_level(self):
        root = SimpleTreeNode(8, None)
        tree = SimpleTree(root)

        node1 = SimpleTreeNode(1, root)
        node2 = SimpleTreeNode(2, root)

        tree.AddChild(root, node1)
        tree.AddChild(root, node2)

        AddLevels(root)

        self.assertEqual(node1.Level, 1)
        self.assertEqual(node2.Level, 1)


    def test_empty_tree(self):
        root = None

        AddLevels(root)

        self.assertIsNone(root)

    # 2.

    def test_root_node_has_zero_level(self):
        root = SimpleTreeNodeWithLevel(8, None, 0)

        self.assertEqual(root.NodeValue, 8)
        self.assertEqual(root.Parent, None)
        self.assertEqual(root.Level, 0)
        self.assertEqual(root.Children, [])


    def test_child_node_has_parent_and_level(self):
        root = SimpleTreeNodeWithLevel(8, None, 0)
        child = SimpleTreeNodeWithLevel(2, root, root.Level + 1)

        self.assertEqual(child.Parent, root)
        self.assertEqual(child.Level, 1)


    def test_deep_tree_levels(self):
        root = SimpleTreeNodeWithLevel(8, None, 0)
        node1 = SimpleTreeNodeWithLevel(1, root, root.Level + 1)
        node2 = SimpleTreeNodeWithLevel(2, node1, node1.Level + 1)
        node3 = SimpleTreeNodeWithLevel(3, node2, node2.Level + 1)

        self.assertEqual(root.Level, 0)
        self.assertEqual(node1.Level, 1)
        self.assertEqual(node2.Level, 2)
        self.assertEqual(node3.Level, 3)


    def test_two_children_have_same_level(self):
        root = SimpleTreeNodeWithLevel(8, None, 0)

        child1 = SimpleTreeNodeWithLevel(1, root, root.Level + 1)
        child2 = SimpleTreeNodeWithLevel(2, root, root.Level + 1)

        self.assertEqual(child1.Level, child2.Level)
        self.assertEqual(child1.Level, 1)



if __name__ == '__main__':
    unittest.main()
