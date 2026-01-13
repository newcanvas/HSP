import unittest
from task2 import LinkedList2, Node
from task2_2 import LinkedList2_1

class DivTests(unittest.TestCase):

    # 2.1.

    def test_find_empty(self):
        ds_list1 = LinkedList2()
        self.assertEqual(ds_list1.find(1), None)

    def test_find_single(self):
        ds_list1 = LinkedList2()
        node = Node(5)
        ds_list1.add_in_tail(node)
        result = ds_list1.find(5)
        self.assertEqual(result.value, 5)
        self.assertEqual(result, node)


    def test_find_multiple(self):
        ds_list1 = LinkedList2()
        node1 = Node(5)
        node2 = Node(6)
        node3 = Node(7)
        ds_list1.add_in_tail(node1)
        ds_list1.add_in_tail(node2)
        ds_list1.add_in_tail(node3)
        result = ds_list1.find(7)
        self.assertEqual(result.value, 7)
        self.assertEqual(result, node3)
        self.assertEqual(result, ds_list1.tail)

    # 2.2.

    def test_find_all_empty(self):
        ds_list = LinkedList2()
        self.assertEqual(ds_list.find_all(1), [])

    def test_find_all_single(self):
        ds_list = LinkedList2()
        ds_list.add_in_tail(Node(5))
        result = ds_list.find_all(5)
        self.assertEqual([result[0].value], [5])

    def test_find_all_multiple(self):
        ds_list = LinkedList2()
        for number in [1, 2, 3, 4, 5, 1]:
            ds_list.add_in_tail(Node(number))
        result = ds_list.find_all(1)
        self.assertEqual([result[0].value, result[1].value], [1, 1])

    # 2.3., 2.4.

    def test_delete_empty(self):
        ds_list = LinkedList2()
        ds_list.delete(1)
        self.assertIsNone(ds_list.head)
        self.assertIsNone(ds_list.tail)

    def test_delete_one(self):
        ds_list = LinkedList2()
        ds_list.add_in_tail(Node(1))
        ds_list.delete(1)

        self.assertIsNone(ds_list.head)
        self.assertIsNone(ds_list.tail)

    def test_delete_first(self):
        ds_list = LinkedList2()
        for number in [1, 2, 3, 4, 5, 1]:
            ds_list.add_in_tail(Node(number))
        ds_list.delete(1)
        self.assertEqual(ds_list.head.value, 2)
        self.assertEqual(ds_list.len(), 5)

    def test_delete_all(self):
        ds_list = LinkedList2()
        for number in [1, 2, 3, 4, 5, 1]:
            ds_list.add_in_tail(Node(number))
        ds_list.delete(1, all=True)
        self.assertEqual(ds_list.len(), 4)
        self.assertEqual(ds_list.head.value, 2)
        self.assertEqual(ds_list.tail.value, 5)

    # 2.5.

    def test_insert_empty(self):
        ds_list = LinkedList2()
        node = Node(10)
        ds_list.insert(None, node)
        self.assertEqual(ds_list.head, node)
        self.assertEqual(ds_list.tail, node)

    def test_insert_with_none(self):
        ds_list = LinkedList2()
        for number in [1, 2, 3, 4, 5, 1]:
            ds_list.add_in_tail(Node(number))
        node = Node(10)
        ds_list.insert(None, node)
        self.assertEqual(ds_list.tail, node)
        self.assertEqual(ds_list.len(), 7)

    def test_insert_after_head(self):
        ds_list = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        ds_list.add_in_tail(n1)
        ds_list.add_in_tail(n2)
        node = Node(99)
        ds_list.insert(n1, node)
        self.assertEqual(ds_list.head.value, 1)
        self.assertEqual(ds_list.tail.value, 2)
        self.assertEqual(ds_list.len(), 3)

    def test_insert_after_tail(self):
        ds_list = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        ds_list.add_in_tail(n1)
        ds_list.add_in_tail(n2)
        node = Node(99)
        ds_list.insert(n2, node)
        self.assertEqual(ds_list.head.value, 1)
        self.assertEqual(ds_list.tail.value, 99)
        self.assertEqual(ds_list.len(), 3)

    # 2.6.

    def test_add_empty(self):
        ds_list = LinkedList2()
        node = Node(99)
        ds_list.add_in_head(node)
        self.assertEqual(ds_list.head, node)
        self.assertEqual(ds_list.tail, node)

    def test_add_one(self):
        ds_list = LinkedList2()
        node1 = Node(99)
        node2 = Node(1)
        ds_list.add_in_tail(node1)
        ds_list.add_in_head(node2)
        self.assertEqual(ds_list.head, node2)
        self.assertEqual(ds_list.tail, node1)

    def test_add_many(self):
        ds_list = LinkedList2()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        ds_list.add_in_tail(node1)
        ds_list.add_in_tail(node2)
        ds_list.add_in_tail(node3)
        ds_list.add_in_head(node4)
        self.assertEqual(ds_list.head.value, 4)
        self.assertEqual(ds_list.head.next.value, 1)
        self.assertEqual(ds_list.len(), 4)

    # 2.7.

    def test_clean_empty(self):
        ds_list = LinkedList2()
        ds_list.clean()
        self.assertIsNone(ds_list.head)
        self.assertIsNone(ds_list.tail)

    def test_clean_empty_single(self):
        ds_list = LinkedList2()
        ds_list.add_in_tail(Node(5))
        ds_list.clean()
        self.assertIsNone(ds_list.head)
        self.assertIsNone(ds_list.tail)

    def test_clean_multiple(self):
        ds_list = LinkedList2()
        for number in [1, 2, 3, 4, 5, 1]:
            ds_list.add_in_tail(Node(number))
        ds_list.clean()
        self.assertIsNone(ds_list.head)
        self.assertIsNone(ds_list.tail)

    # 2.8.

    def test_len_empty(self):
        ds_list = LinkedList2()
        self.assertEqual(ds_list.len(), 0)

    def test_len_single(self):
        ds_list = LinkedList2()
        ds_list.add_in_tail(Node(5))
        self.assertEqual(ds_list.len(), 1)

    def test_len_multiple(self):
        ds_list = LinkedList2()
        for number in [1, 2, 3, 4, 5, 1]:
            ds_list.add_in_tail(Node(number))
        self.assertEqual(ds_list.len(), 6)

    # 2.10.

    def test_flip_empty(self):
        ds_list = LinkedList2_1()
        ds_list.flip_list()
        self.assertIsNone(ds_list.head)
        self.assertIsNone(ds_list.tail)

    def test_flip_one(self):
        ds_list = LinkedList2_1()
        node = Node(10)
        ds_list.add_in_tail(node)
        self.assertEqual(ds_list.head, node)
        self.assertEqual(ds_list.tail, node)

    def test_flip_multiple(self):
        ds_list = LinkedList2_1()
        for number in [10, 2, 3, 4, 5, 1]:
            ds_list.add_in_tail(Node(number))
        ds_list.flip_list()
        self.assertEqual(ds_list.head.value, 1)
        self.assertEqual(ds_list.tail.value, 10)
        expected = [1, 5, 4, 3, 2, 10]
        node = ds_list.head
        for value in expected:
            self.assertIsNotNone(node)
            self.assertEqual(node.value, value)
            node = node.next

    def test_flip_multiple_negative(self):
        ds_list = LinkedList2_1()
        for number in [-10, -2, -1, 99]:
            ds_list.add_in_tail(Node(number))
        ds_list.flip_list()
        self.assertEqual(ds_list.head.value, 99)
        self.assertEqual(ds_list.tail.value, -10)
        expected = [99, -1, -2, -10]
        node = ds_list.head
        for value in expected:
            self.assertIsNotNone(node)
            self.assertEqual(node.value, value)
            node = node.next

    # 2.11.

    def test_find_loop_empty(self):
        ds_list = LinkedList2_1()
        result = ds_list.find_loop()
        self.assertEqual(result, False)

    def test_find_loop_one(self):
        ds_list = LinkedList2_1()
        ds_list.add_in_tail(Node(10))
        result = ds_list.find_loop()
        self.assertEqual(result, False)

    def test_find_loop_multiple_false(self):
        ds_list = LinkedList2_1()
        for number in [10, 2, 3, 4, 5, 1]:
            ds_list.add_in_tail(Node(number))
        result = ds_list.find_loop()
        self.assertEqual(result, False)

    def test_find_loop_multiple_true(self):
        ds_list = LinkedList2_1()
        node1 = Node(11)
        node2 = Node(12)
        for number in [10, 2, 3, 4, 5, 1]:
            ds_list.add_in_tail(Node(number))
        ds_list.add_in_tail(node1)
        ds_list.add_in_tail(node2)
        ds_list.tail.next = node1
        result = ds_list.find_loop()
        self.assertEqual(result, True)

    # 2.12.

    def test_sort_empty(self):
        ds_list = LinkedList2_1()
        self.assertEqual(ds_list.head, None)
        self.assertEqual(ds_list.tail, None)

    def test_sort_one(self):
        ds_list = LinkedList2_1()
        ds_list.add_in_tail(Node(10))
        ds_list.sort_list()
        self.assertEqual(ds_list.head.value, 10)
        self.assertEqual(ds_list.tail.value, 10)

    def test_sort_many(self):
        ds_list = LinkedList2_1()
        for number in [10, 2, 3, 4, 5, 1]:
            ds_list.add_in_tail(Node(number))
        ds_list.sort_list()
        self.assertEqual(ds_list.head.value, 1)
        self.assertEqual(ds_list.tail.value, 10)
        expected = [1, 2, 3, 4, 5, 10]
        node = ds_list.head
        for value in expected:
            self.assertIsNotNone(node)
            self.assertEqual(node.value, value)
            node = node.next

    def test_sort_many_negatives(self):
        ds_list = LinkedList2_1()
        for number in [10, 2, -3, 4, -5, 1]:
            ds_list.add_in_tail(Node(number))
        ds_list.sort_list()
        self.assertEqual(ds_list.head.value, -5)
        self.assertEqual(ds_list.tail.value, 10)
        expected = [-5, -3, 1, 2, 4, 10]
        node = ds_list.head
        for value in expected:
            self.assertIsNotNone(node)
            self.assertEqual(node.value, value)
            node = node.next

    # 2.13., 2.14.

    def test_merge_empty(self):
        ds_list = LinkedList2_1()
        ds_list2 = LinkedList2_1()
        result = LinkedList2_1.merge_lists(ds_list, ds_list2)
        self.assertEqual(result, None)

    def test_merge_one_in_one(self):
        ds_list = LinkedList2_1()
        ds_list.add_in_tail(Node(10))
        ds_list2 = LinkedList2_1()
        result = LinkedList2_1.merge_lists(ds_list, ds_list2)
        self.assertEqual(result.head.value, 10)
        self.assertEqual(result.tail.value, 10)
        self.assertEqual(result.len(), 1)

    def test_merge_one_in_two(self):
        ds_list = LinkedList2_1()
        ds_list.add_in_tail(Node(10))
        ds_list2 = LinkedList2_1()
        ds_list2.add_in_tail(Node(1))
        result = LinkedList2_1.merge_lists(ds_list, ds_list2)
        self.assertEqual(result.head.value, 1)
        self.assertEqual(result.tail.value, 10)
        self.assertEqual(result.len(), 2)

    def test_merge_many(self):
        ds_list = LinkedList2_1()
        for number in [10, 2, -3, 4, -5, 1]:
            ds_list.add_in_tail(Node(number))
        ds_list2 = LinkedList2_1()
        for number in [10, 2, -3, 4, -5, 1, 2000, 0]:
            ds_list2.add_in_tail(Node(number))
        result = LinkedList2_1.merge_lists(ds_list, ds_list2)
        self.assertEqual(result.head.value, -5)
        self.assertEqual(result.tail.value, 2000)
        self.assertEqual(result.len(), 14)


if __name__ == '__main__':
    unittest.main()
