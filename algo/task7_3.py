import unittest

from task7 import OrderedList
from task7_2 import delete_double, merge_ordered_lists, find_sublist, most_common

class DivTests(unittest.TestCase):

    # 7.

    def test_add_asc(self):
        OL = OrderedList(True)
        self.assertEqual(OL.len(), 0)
        OL.add(1)
        self.assertEqual(OL.head.value, 1)
        self.assertEqual(OL.tail.value, 1)
        self.assertEqual(OL.len(), 1)
        OL.add(2)
        self.assertEqual(OL.head.value, 1)
        self.assertEqual(OL.tail.value, 2)
        self.assertEqual(OL.len(), 2)
        OL.add(3)
        self.assertEqual(OL.head.value, 1)
        self.assertEqual(OL.tail.value, 3)
        self.assertEqual(OL.len(), 3)
        OL.add(-1)
        self.assertEqual(OL.head.value, -1)
        self.assertEqual(OL.tail.value, 3)
        self.assertEqual(OL.len(), 4)

    def test_add_desc(self):
        OL = OrderedList(False)
        self.assertEqual(OL.len(), 0)
        OL.add(1)
        self.assertEqual(OL.head.value, 1)
        self.assertEqual(OL.tail.value, 1)
        self.assertEqual(OL.len(), 1)
        OL.add(2)
        self.assertEqual(OL.head.value, 2)
        self.assertEqual(OL.tail.value, 1)
        self.assertEqual(OL.len(), 2)
        OL.add(3)
        self.assertEqual(OL.head.value, 3)
        self.assertEqual(OL.tail.value, 1)
        self.assertEqual(OL.len(), 3)
        OL.add(-1)
        self.assertEqual(OL.head.value, 3)
        self.assertEqual(OL.tail.value, -1)
        self.assertEqual(OL.len(), 4)

    def test_delete_asc(self):
        OL = OrderedList(True)
        self.assertEqual(OL.len(), 0)
        self.assertIsNone(OL.delete(0))
        OL.add(1)
        OL.add(2)
        OL.add(3)
        self.assertIsNone(OL.delete(0))
        OL.delete(1)
        self.assertEqual(OL.head.value, 2)
        self.assertEqual(OL.tail.value, 3)
        self.assertEqual(OL.len(), 2)
        OL.delete(3)
        self.assertEqual(OL.head.value, 2)
        self.assertEqual(OL.tail.value, 2)
        self.assertEqual(OL.len(), 1)
        OL.add(3)
        OL.add(3)
        OL.add(3)
        OL.delete(3)
        self.assertEqual(OL.head.value, 2)
        self.assertEqual(OL.tail.value, 3)
        self.assertEqual(OL.len(), 3)

    def test_delete_desc(self):
        OL = OrderedList(False)
        self.assertEqual(OL.len(), 0)
        self.assertIsNone(OL.delete(0))
        OL.add(1)
        OL.add(2)
        OL.add(3)
        self.assertIsNone(OL.delete(0))
        OL.delete(1)
        self.assertEqual(OL.head.value, 3)
        self.assertEqual(OL.tail.value, 2)
        self.assertEqual(OL.len(), 2)
        OL.delete(3)
        self.assertEqual(OL.head.value, 2)
        self.assertEqual(OL.tail.value, 2)
        self.assertEqual(OL.len(), 1)
        OL.add(3)
        OL.add(3)
        OL.add(3)
        OL.delete(3)
        self.assertEqual(OL.head.value, 3)
        self.assertEqual(OL.tail.value, 2)
        self.assertEqual(OL.len(), 3)

    def test_find_asc(self):
        OL = OrderedList(True)
        self.assertEqual(OL.len(), 0)
        self.assertIsNone(OL.find(0))
        OL.add(1)
        OL.add(1)
        OL.add(1)
        OL.add(1)
        OL.add(2)
        OL.add(2)
        self.assertEqual(OL.find(1), OL.head)
        self.assertNotEqual(OL.find(2), OL.tail)

    def test_find_desc(self):
        OL = OrderedList(False)
        self.assertEqual(OL.len(), 0)
        self.assertIsNone(OL.find(0))
        OL.add(1)
        OL.add(1)
        OL.add(1)
        OL.add(1)
        OL.add(2)
        OL.add(2)
        self.assertNotEqual(OL.find(1), OL.tail)
        self.assertEqual(OL.find(2), OL.head)

    # 8.

    def test_delete_double_middle(self):
        OL = OrderedList(True)
        for i in [1, 2, 2, 3, 3, 4]:
            OL.add(i)
        self.assertEqual(OL.len(), 6)
        OL.delete_double()
        values = [node.value for node in OL.get_all()]
        self.assertEqual(values, [1, 2, 3, 4])
        self.assertEqual(OL.len(), 4)

    def test_delete_double_all_same(self):
        OL = OrderedList(True)
        for i in [5, 5, 5, 5]:
            OL.add(i)
        OL.delete_double()
        values = [node.value for node in OL.get_all()]
        self.assertEqual(values, [5])
        self.assertEqual(OL.len(), 1)

    def test_delete_double_no_duplicates(self):
        OL = OrderedList(True)
        for i in [1, 2, 3, 4]:
            OL.add(i)
        self.assertEqual(OL.len(), 4)
        OL.delete_double()
        values = [node.value for node in OL.get_all()]
        self.assertEqual(values, [1, 2, 3, 4])
        self.assertEqual(OL.len(), 4)

    def test_delete_double_empty(self):
        OL = OrderedList(True)
        result = OL.delete_double()
        self.assertIsNone(result)

    # 9.

    def test_merge_simple(self):
        l1 = OrderedList(True)
        l2 = OrderedList(True)
        for i in [1, 3, 5]:
            l1.add(i)
        for i in [2, 4, 6]:
            l2.add(i)
        result = merge_ordered_lists(l1, l2, True)
        values = [node.value for node in result.get_all()]
        self.assertEqual(values, [1, 2, 3, 4, 5, 6])
        self.assertEqual(result.len(), 6)

    def test_merge_one_empty(self):
        l1 = OrderedList(True)
        l2 = OrderedList(True)
        for i in [1, 2, 3]:
            l1.add(i)
        result = merge_ordered_lists(l1, l2, True)
        values = [node.value for node in result.get_all()]
        self.assertEqual(values, [1, 2, 3])
        self.assertEqual(result.len(), 3)

    def test_merge_both_empty(self):
        l1 = OrderedList(False)
        l2 = OrderedList(False)
        result = merge_ordered_lists(l1, l2, False)
        self.assertIsNone(result.head)
        self.assertIsNone(result.tail)

    # 10.

    def test_sublist_exists(self):
        OL = OrderedList(True)
        sub = OrderedList(False)
        for i in [0, 0, 1, 2, 3, 4, 5]:
            OL.add(i)
        for i in [0, 0]:
            sub.add(i)
        self.assertTrue(OL.find_sublist(sub))

    def test_sublist_not_exists(self):
        OL = OrderedList(True)
        sub = OrderedList(True)
        for i in [1, 2, 3, 4]:
            OL.add(i)
        for i in [2, 5]:
            sub.add(i)
        self.assertFalse(OL.find_sublist(sub))

    def test_sublist_equal_list(self):
        OL = OrderedList(True)
        sub = OrderedList(True)
        for i in [1, 2, 3]:
            OL.add(i)
            sub.add(i)
        self.assertTrue(OL.find_sublist(sub))

    def test_sublist_empty(self):
        OL = OrderedList(True)
        sub = OrderedList(True)
        for i in [1, 2, 3]:
            OL.add(i)
        self.assertTrue(OL.find_sublist(sub))

    # 11.

    def test_most_common_simple(self):
        OL = OrderedList(True)
        OL2 = OrderedList(False)
        for i in [1, 2, 2, 3]:
            OL.add(i)
            OL2.add(i)
        self.assertEqual(OL.most_common(), 2)
        self.assertEqual(OL2.most_common(), 2)

    def test_most_common_all_same(self):
        OL = OrderedList(True)
        OL2 = OrderedList(False)
        for i in [5, 5, 5]:
            OL.add(i)
            OL2.add(i)
        self.assertEqual(OL.most_common(), 5)
        self.assertEqual(OL2.most_common(), 5)

    def test_most_common_single(self):
        OL = OrderedList(True)
        OL2 = OrderedList(False)
        OL.add(10)
        OL2.add(10)
        self.assertEqual(OL.most_common(), 10)
        self.assertEqual(OL2.most_common(), 10)

    def test_most_common_empty(self):
        OL = OrderedList(True)
        OL2 = OrderedList(False)
        self.assertIsNone(OL.most_common())
        self.assertIsNone(OL2.most_common())

    # 12.

    def test_get_by_index_asc(self):
        OL = OrderedList(True)
        for i in [3, 1, 4, 1, 5]:
            OL.add(i)
        self.assertEqual(OL.get_by_index(0).value, 1)
        self.assertEqual(OL.get_by_index(2).value, 3)
        self.assertEqual(OL.get_by_index(4).value, 5)

    def test_get_by_index_desc(self):
        OL = OrderedList(False)
        for i in [3, 1, 4, 1, 5]:
            OL.add(i)
        self.assertEqual(OL.get_by_index(0).value, 5)
        self.assertEqual(OL.get_by_index(2).value, 3)
        self.assertEqual(OL.get_by_index(4).value, 1)

    def test_out_of_bounds(self):
        OL = OrderedList(True)
        OL2 = OrderedList(True)
        self.assertIsNone(OL.get_by_index(0))
        self.assertIsNone(OL2.get_by_index(0))
        OL.add(1)
        OL2.add(1)
        self.assertIsNone(OL.get_by_index(-1))
        self.assertIsNone(OL.get_by_index(1))
        self.assertIsNone(OL2.get_by_index(-1))
        self.assertIsNone(OL2.get_by_index(1))

    def test_get_by_index_after_operstions(self):
        OL = OrderedList(True)
        for i in [1, 2, 3, 4, 5]:
            OL.add(i)
        OL.delete(1)
        OL.delete(5)
        OL.add(6)
        self.assertEqual(OL.get_by_index(0).value, 2)
        self.assertEqual(OL.get_by_index(3).value, 6)
        self.assertEqual(OL.len(), 4)

if __name__ == '__main__':
    unittest.main()
