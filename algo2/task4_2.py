import unittest

from task4 import aBST
from task4_3 import FindMinCommon, WideAllNodes


aBST.FindMinCommon =  FindMinCommon
aBST.WideAllNodes = WideAllNodes


class TestABST(unittest.TestCase):

    # FindKeyIndex

    def test_find_existing_key(self):
        tree = aBST(2)
        tree.Tree = [10, 5, 15, 3, 7, 12, 20]

        result = tree.FindKeyIndex(7)

        self.assertEqual(result, 4)

    def test_find_absent_key_with_empty_slot(self):
        tree = aBST(2)
        tree.Tree = [10, 5, 15, 3, None, 12, 20]

        result = tree.FindKeyIndex(7)

        self.assertEqual(result, -4)

    def test_find_absent_key_in_full_tree(self):
        tree = aBST(2)
        tree.Tree = [10, 5, 15, 3, 7, 12, 20]

        result = tree.FindKeyIndex(8)

        self.assertIsNone(result)

    def test_find_deep_existing_key(self):
        tree = aBST(3)
        tree.Tree = [
            10,
            5, 15,
            3, 7, 12, 20,
            1, None, None, None, None, None, None, None
        ]

        result = tree.FindKeyIndex(1)

        self.assertEqual(result, 7)

    def test_find_key_in_empty_tree(self):
        tree = aBST(2)

        result = tree.FindKeyIndex(10)

        self.assertEqual(result, 0)

    def test_find_key_in_depth_zero_tree(self):
        tree = aBST(0)

        result = tree.FindKeyIndex(10)

        self.assertEqual(result, 0)


    # AddKey

    def test_add_key_to_empty_tree(self):
        tree = aBST(2)

        result = tree.AddKey(10)

        self.assertEqual(result, 0)
        self.assertEqual(tree.Tree[0], 10)

    def test_add_key_to_correct_position(self):
        tree = aBST(2)
        tree.Tree = [10, 5, 15, None, None, None, None]

        result = tree.AddKey(7)

        self.assertEqual(result, 4)
        self.assertEqual(tree.Tree[4], 7)

    def test_add_existing_key(self):
        tree = aBST(2)
        tree.Tree = [10, 5, 15, 3, 7, 12, 20]

        result = tree.AddKey(7)

        self.assertEqual(result, 4)
        self.assertEqual(tree.Tree, [10, 5, 15, 3, 7, 12, 20])

    def test_add_key_when_tree_is_full(self):
        tree = aBST(2)
        tree.Tree = [10, 5, 15, 3, 7, 12, 20]

        result = tree.AddKey(8)

        self.assertEqual(result, -1)

    def test_add_key_beyond_array_to_left(self):
        tree = aBST(2)
        tree.Tree = [10, 5, 15, 3, 7, 12, 20]

        result = tree.AddKey(1)

        self.assertEqual(result, -1)

    def test_add_key_beyond_array_to_right(self):
        tree = aBST(2)
        tree.Tree = [10, 5, 15, 3, 7, 12, 20]

        result = tree.AddKey(25)

        self.assertEqual(result, -1)

    # FindMinCommon

    def test_common_parent_for_two_children(self):
        tree = aBST(2)
        tree.Tree = [10, 5, 15, 3, 7, 12, 20]

        result = tree.FindMinCommon(3, 7)

        self.assertEqual(result, 5)

    def test_common_parent_for_different_subtrees(self):
        tree = aBST(2)
        tree.Tree = [10, 5, 15, 3, 7, 12, 20]

        result = tree.FindMinCommon(3, 12)

        self.assertEqual(result, 10)

    def test_common_parent_for_node_and_descendant(self):
        tree = aBST(2)
        tree.Tree = [10, 5, 15, 3, 7, 12, 20]

        result = tree.FindMinCommon(5, 3)

        self.assertEqual(result, 10)

    def test_common_parent_in_right_subtree(self):
        tree = aBST(2)
        tree.Tree = [10, 5, 15, 3, 7, 12, 20]

        result = tree.FindMinCommon(12, 20)

        self.assertEqual(result, 15)

    # WideAllNodes

    def test_wide_all_nodes_complete_tree(self):
        tree = aBST(2)
        tree.Tree = [10, 5, 15, 3, 7, 12, 20]

        result = tree.WideAllNodes()

        self.assertEqual(result, [10, 5, 15, 3, 7, 12, 20])

    def test_wide_all_nodes_with_none(self):
        tree = aBST(2)
        tree.Tree = [10, 5, 15, None, 7, 12, None]

        result = tree.WideAllNodes()

        self.assertEqual(result, [10, 5, 15, 7, 12])

    def test_wide_all_nodes_only_root(self):
        tree = aBST(0)
        tree.Tree = [10]

        result = tree.WideAllNodes()

        self.assertEqual(result, [10])

    def test_wide_all_nodes_empty_tree(self):
        tree = aBST(2)
        tree.Tree = [None, None, None, None, None, None, None]

        result = tree.WideAllNodes()

        self.assertEqual(result, [])

    def test_wide_all_nodes_right_subtree(self):
        tree = aBST(2)
        tree.Tree = [10, None, 15, None, None, 12, 20]

        result = tree.WideAllNodes()

        self.assertEqual(result, [10, 15, 12, 20])


if __name__ == '__main__':
    unittest.main()
