import unittest

from task5 import GenerateBBSTArray
from task5_3 import DeleteNode


def inorder(tree, index=0):
    if index >= len(tree) or tree[index] is None:
        return []

    return inorder(tree, 2 * index + 1) + [tree[index]] + inorder(tree, 2 * index + 2)


def height(tree, index=0):
    if index >= len(tree) or tree[index] is None:
        return 0

    return 1 + max(height(tree, 2 * index + 1), height(tree, 2 * index + 2))


def is_balanced(tree, index=0):
    if index >= len(tree) or tree[index] is None:
        return True

    left = 2 * index + 1
    right = 2 * index + 2
    left_height = height(tree, left)
    right_height = height(tree, right)

    return (
        abs(left_height - right_height) <= 1
        and is_balanced(tree, left)
        and is_balanced(tree, right)
    )


def values(tree):
    return [node for node in tree if node is not None]


class GenerateBBSTArrayTests(unittest.TestCase):

    def test_empty(self):
        result = GenerateBBSTArray([])

        self.assertEqual(result, [])

    def test_one_node(self):
        result = GenerateBBSTArray([10])

        self.assertEqual(result, [10])
        self.assertEqual(inorder(result), [10])
        self.assertTrue(is_balanced(result))

    def test_three_nodes(self):
        result = GenerateBBSTArray([1, 2, 3])

        self.assertEqual(result, [2, 1, 3])
        self.assertEqual(inorder(result), [1, 2, 3])
        self.assertTrue(is_balanced(result))

    def test_perfect_tree(self):
        result = GenerateBBSTArray([1, 2, 3, 4, 5, 6, 7])

        self.assertEqual(result, [4, 2, 6, 1, 3, 5, 7])
        self.assertEqual(inorder(result), [1, 2, 3, 4, 5, 6, 7])
        self.assertTrue(is_balanced(result))

    def test_perfect_tree_of_fifteen(self):
        result = GenerateBBSTArray(list(range(1, 16)))

        self.assertEqual(result, [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])
        self.assertEqual(inorder(result), list(range(1, 16)))
        self.assertTrue(is_balanced(result))
        self.assertEqual(height(result), 4)

    def test_unsorted_input(self):
        result = GenerateBBSTArray([7, 1, 5, 3, 6, 2, 4])

        self.assertEqual(result, [4, 2, 6, 1, 3, 5, 7])
        self.assertEqual(inorder(result), [1, 2, 3, 4, 5, 6, 7])
        self.assertTrue(is_balanced(result))

    def test_reverse_sorted_input(self):
        result = GenerateBBSTArray([7, 6, 5, 4, 3, 2, 1])

        self.assertEqual(result, [4, 2, 6, 1, 3, 5, 7])
        self.assertEqual(inorder(result), [1, 2, 3, 4, 5, 6, 7])

    def test_negative_keys(self):
        result = GenerateBBSTArray([-3, -1, 0, 2, 5, 8, 10])

        self.assertEqual(result, [2, -1, 8, -3, 0, 5, 10])
        self.assertEqual(inorder(result), [-3, -1, 0, 2, 5, 8, 10])
        self.assertTrue(is_balanced(result))

    def test_keeps_all_keys(self):
        keys = [10, 3, 8, 1, 15, 6, 12]
        result = GenerateBBSTArray(keys.copy())

        self.assertEqual(sorted(values(result)), sorted(keys))
        self.assertEqual(len(result), len(keys))
        self.assertNotIn(None, result)

    def test_inorder_is_sorted(self):
        result = GenerateBBSTArray([20, 4, 15, 1, 9, 30, 25])
        keys = inorder(result)

        self.assertEqual(keys, sorted(keys))

    def test_root_is_median(self):
        result = GenerateBBSTArray([1, 2, 3, 4, 5, 6, 7])

        self.assertEqual(result[0], 4)
        self.assertEqual(result[1], 2)
        self.assertEqual(result[2], 6)

    def test_height_is_logarithmic(self):
        result = GenerateBBSTArray([1, 2, 3, 4, 5, 6, 7])

        self.assertEqual(height(result), 3)
        self.assertTrue(is_balanced(result))

    def test_sorts_input_in_place(self):
        keys = [3, 1, 2]
        GenerateBBSTArray(keys)

        self.assertEqual(keys, [1, 2, 3])


class DeleteNodeTests(unittest.TestCase):

    def test_delete_leaf(self):
        tree = GenerateBBSTArray([1, 2, 3, 4, 5, 6, 7])

        result = DeleteNode(tree, 7)

        self.assertEqual(sorted(values(result)), [1, 2, 3, 4, 5, 6])
        self.assertNotIn(7, result)
        self.assertNotIn(None, result)
        self.assertEqual(inorder(result), [1, 2, 3, 4, 5, 6])
        self.assertTrue(is_balanced(result))

    def test_delete_root(self):
        tree = GenerateBBSTArray([1, 2, 3, 4, 5, 6, 7])

        result = DeleteNode(tree, 4)

        self.assertEqual(sorted(values(result)), [1, 2, 3, 5, 6, 7])
        self.assertNotIn(4, result)
        self.assertEqual(inorder(result), [1, 2, 3, 5, 6, 7])
        self.assertTrue(is_balanced(result))

    def test_delete_internal_node(self):
        tree = GenerateBBSTArray([1, 2, 3, 4, 5, 6, 7])

        result = DeleteNode(tree, 2)

        self.assertEqual(sorted(values(result)), [1, 3, 4, 5, 6, 7])
        self.assertNotIn(2, result)
        self.assertEqual(inorder(result), [1, 3, 4, 5, 6, 7])
        self.assertTrue(is_balanced(result))

    def test_delete_missing_key(self):
        tree = GenerateBBSTArray([1, 2, 3, 4, 5, 6, 7])

        result = DeleteNode(tree, 100)

        self.assertEqual(result, tree)
        self.assertEqual(inorder(result), [1, 2, 3, 4, 5, 6, 7])

    def test_delete_only_node(self):
        tree = GenerateBBSTArray([10])

        result = DeleteNode(tree, 10)

        self.assertEqual(result, [])

    def test_delete_from_empty_tree(self):
        result = DeleteNode([], 1)

        self.assertEqual(result, [])

    def test_delete_keeps_complete_layout(self):
        tree = GenerateBBSTArray([1, 2, 3, 4, 5, 6, 7])

        result = DeleteNode(tree, 1)

        self.assertEqual(len(result), 6)
        self.assertNotIn(None, result)
        self.assertEqual(sorted(result), [2, 3, 4, 5, 6, 7])
        self.assertEqual(inorder(result), [2, 3, 4, 5, 6, 7])
        self.assertTrue(is_balanced(result))

    def test_repeated_delete_until_empty(self):
        tree = GenerateBBSTArray([1, 2, 3, 4, 5, 6, 7])

        for key in [3, 6, 1, 7, 2, 5, 4]:
            tree = DeleteNode(tree, key)
            self.assertNotIn(key, tree)
            self.assertEqual(inorder(tree), sorted(values(tree)))
            self.assertTrue(is_balanced(tree))

        self.assertEqual(tree, [])


if __name__ == '__main__':
    unittest.main()
