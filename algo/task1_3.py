import unittest
from task1 import LinkedList, Node
from task1_2 import list_summ

class DivTests(unittest.TestCase):

    # 1.1., 1.2.
    def test_delete_empty(self):
        s_list = LinkedList()
        s_list.delete(1)
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)

    def test_delete_one(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(1))
        s_list.delete(1)

        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)

    def test_delete_first(self):
        s_list = LinkedList()
        for number in [1, 2, 3, 4, 5, 1]:
            s_list.add_in_tail(Node(number))
        s_list.delete(1)
        self.assertEqual(s_list.head.value, 2)
        self.assertEqual(s_list.len(), 5)

    def test_delete_all(self):
        s_list = LinkedList()
        for number in [1, 2, 3, 4, 5, 1]:
            s_list.add_in_tail(Node(number))
        s_list.delete(1, all=True)
        self.assertEqual(s_list.len(), 4)
        self.assertEqual(s_list.head.value, 2)
        self.assertEqual(s_list.tail.value, 5)

    # 1.3.

    def test_clean_empty(self):
        s_list = LinkedList()
        s_list.clean()
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)

    def test_clean_empty_single(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(5))
        s_list.clean()
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)

    def test_clean_multiple(self):
        s_list = LinkedList()
        for number in [1, 2, 3, 4, 5, 1]:
            s_list.add_in_tail(Node(number))
        s_list.clean()
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)

    # 1.4.

    def test_find_all_empty(self):
        s_list = LinkedList()
        self.assertEqual(s_list.find_all(1), [])

    def test_find_all_single(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(5))
        result = s_list.find_all(5)
        self.assertEqual([result[0].value], [5])

    def test_find_all_multiple(self):
        s_list = LinkedList()
        for number in [1, 2, 3, 4, 5, 1]:
            s_list.add_in_tail(Node(number))
        result = s_list.find_all(1)
        self.assertEqual([result[0].value, result[1].value], [1, 1])

    # 1.5.

    def test_len_empty(self):
        s_list = LinkedList()
        self.assertEqual(s_list.len(), 0)

    def test_len_single(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(5))
        self.assertEqual(s_list.len(), 1)

    def test_len_multiple(self):
        s_list = LinkedList()
        for number in [1, 2, 3, 4, 5, 1]:
            s_list.add_in_tail(Node(number))
        self.assertEqual(s_list.len(), 6)

    # 1.6.

    def test_insert_empty(self):
        s_list = LinkedList()
        node = Node(10)
        s_list.insert(None, node)
        self.assertEqual(s_list.head, node)

    def test_insert_after_head(self):
        s_list = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        node = Node(99)
        s_list.insert(n1, node)
        self.assertEqual(s_list.head.value, 1)
        self.assertEqual(s_list.tail.value, 2)
        self.assertEqual(s_list.len(), 3)

    def test_insert_after_tail(self):
        s_list = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        node = Node(99)
        s_list.insert(n2, node)
        self.assertEqual(s_list.head.value, 1)
        self.assertEqual(s_list.tail.value, 99)
        self.assertEqual(s_list.len(), 3)

    # 1.8.

    def test_summ_empty(self):
        s_list1 = LinkedList()
        s_list2 = LinkedList()
        self.assertEqual(list_summ(s_list1, s_list2), [])

    def test_summ_different(self):
        s_list1 = LinkedList()
        n1 = Node(1)
        s_list1.add_in_tail(n1)
        s_list2 = LinkedList()
        self.assertEqual(list_summ(s_list1, s_list2), None)

    def test_summ_equal_one(self):
        s_list1 = LinkedList()
        n1 = Node(1)
        s_list1.add_in_tail(n1)
        s_list2 = LinkedList()
        n2 = Node(2)
        s_list2.add_in_tail(n2)
        self.assertEqual(list_summ(s_list1, s_list2), [3])

    def test_summ_equal_many(self):
        s_list1 = LinkedList()
        for number in [1, 2, 3, 4, 5, 1]:
            s_list1.add_in_tail(Node(number))
        s_list2 = LinkedList()
        for number in [1, 2, 3, 4, 5, 1]:
            s_list2.add_in_tail(Node(number))
        self.assertEqual(list_summ(s_list1, s_list2), [2,4,6,8,10,2])

if __name__ == '__main__':
    unittest.main()
