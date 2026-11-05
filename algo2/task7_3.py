import unittest
from task7 import Heap
from task7_2 import FindMaxInRange, FindLess, FindAllGreater, Merge

Heap.FindMaxInRange = FindMaxInRange
Heap.FindLess = FindLess
Heap.FindAllGreater = FindAllGreater
Heap.Merge = Merge


def values(heap):
    return [key for key in heap.HeapArray if key is not None]


def make_heap(a, depth):
    heap = Heap()
    heap.MakeHeap(a, depth)
    return heap


class TestMakeHeap(unittest.TestCase):

    def test_empty_array(self):
        heap = make_heap([], 2)

        self.assertEqual(heap.HeapArray, [None] * 7)
        self.assertTrue(heap.IsHeap())

    def test_depth_zero(self):
        heap = make_heap([5], 0)

        self.assertEqual(heap.HeapArray, [5])

    def test_three_elements(self):
        heap = make_heap([1, 2, 3], 1)

        self.assertEqual(heap.HeapArray, [3, 1, 2])

    def test_unsorted_array(self):
        keys = [11, 9, 4, 7, 8, 3, 1, 2, 5, 6]
        heap = make_heap(keys, 3)

        self.assertEqual(len(heap.HeapArray), 15)
        self.assertEqual(heap.HeapArray[0], 11)
        self.assertEqual(sorted(values(heap)), sorted(keys))
        self.assertTrue(heap.IsHeap())

    def test_sorted_ascending(self):
        heap = make_heap([1, 2, 3, 4, 5, 6, 7], 2)

        self.assertEqual(heap.HeapArray[0], 7)
        self.assertNotIn(None, heap.HeapArray)
        self.assertTrue(heap.IsHeap())

    def test_too_many_elements(self):
        heap = make_heap([1, 2, 3, 4, 5], 1)

        self.assertEqual(sorted(values(heap)), [1, 2, 3])
        self.assertTrue(heap.IsHeap())

    def test_duplicates(self):
        heap = make_heap([5, 5, 5, 5], 2)

        self.assertEqual(values(heap), [5, 5, 5, 5])
        self.assertTrue(heap.IsHeap())


class TestGetMax(unittest.TestCase):

    def test_empty_heap(self):
        heap = make_heap([], 2)

        self.assertEqual(heap.GetMax(), -1)

    def test_not_created_heap(self):
        heap = Heap()

        self.assertEqual(heap.GetMax(), -1)

    def test_one_element(self):
        heap = make_heap([5], 1)

        self.assertEqual(heap.GetMax(), 5)
        self.assertEqual(heap.HeapArray, [None, None, None])
        self.assertEqual(heap.GetMax(), -1)

    def test_returns_root_and_rebuilds(self):
        heap = make_heap([11, 9, 4, 7, 8, 3, 1, 2, 5, 6], 3)

        self.assertEqual(heap.GetMax(), 11)
        self.assertEqual(heap.HeapArray[0], 9)
        self.assertEqual(len(values(heap)), 9)
        self.assertTrue(heap.IsHeap())

    def test_returns_sorted_until_empty(self):
        keys = [3, 10, 1, 8, 6, 0, 7]
        heap = make_heap(keys, 2)
        result = []

        key = heap.GetMax()
        while key != -1:
            result.append(key)
            self.assertTrue(heap.IsHeap())
            key = heap.GetMax()

        self.assertEqual(result, sorted(keys, reverse=True))

    def test_zero_key(self):
        heap = make_heap([0], 0)

        self.assertEqual(heap.GetMax(), 0)
        self.assertEqual(heap.GetMax(), -1)


class TestAdd(unittest.TestCase):

    def test_add_to_empty(self):
        heap = make_heap([], 1)

        self.assertTrue(heap.Add(5))
        self.assertEqual(heap.HeapArray, [5, None, None])

    def test_add_new_max(self):
        heap = make_heap([5, 3, 4], 2)

        self.assertTrue(heap.Add(10))
        self.assertEqual(heap.HeapArray[0], 10)
        self.assertTrue(heap.IsHeap())

    def test_add_small_key(self):
        heap = make_heap([5, 3, 4], 2)

        self.assertTrue(heap.Add(1))
        self.assertEqual(heap.HeapArray[:4], [5, 3, 4, 1])
        self.assertTrue(heap.IsHeap())

    def test_add_to_full_heap(self):
        heap = make_heap([1, 2, 3], 1)

        self.assertFalse(heap.Add(10))
        self.assertEqual(heap.HeapArray, [3, 1, 2])

    def test_add_to_not_created_heap(self):
        heap = Heap()

        self.assertFalse(heap.Add(1))
        self.assertEqual(heap.HeapArray, [])

    def test_add_after_get_max(self):
        heap = make_heap([1, 2, 3], 1)
        heap.GetMax()

        self.assertTrue(heap.Add(7))
        self.assertEqual(heap.HeapArray[0], 7)
        self.assertTrue(heap.IsHeap())


class TestIsHeap(unittest.TestCase):

    def test_empty_heap(self):
        heap = Heap()

        self.assertTrue(heap.IsHeap())

    def test_generated_heap(self):
        heap = make_heap([8, 3, 10, 1, 6, 14, 4, 7, 13, 2], 3)

        self.assertTrue(heap.IsHeap())

    def test_child_bigger_than_parent(self):
        heap = Heap()
        heap.HeapArray = [5, 10, 3]

        self.assertFalse(heap.IsHeap())

    def test_deep_violation(self):
        heap = Heap()
        heap.HeapArray = [10, 8, 9, 7, 9, 1, 2]

        self.assertFalse(heap.IsHeap())

    def test_gap_in_array(self):
        heap = Heap()
        heap.HeapArray = [10, None, 5]

        self.assertFalse(heap.IsHeap())

    def test_equal_keys(self):
        heap = Heap()
        heap.HeapArray = [5, 5, 5, None, None, None, None]

        self.assertTrue(heap.IsHeap())


class TestFindMaxInRange(unittest.TestCase):

    def test_empty_heap(self):
        heap = make_heap([], 2)

        self.assertEqual(heap.FindMaxInRange(0, 100), -1)

    def test_whole_range(self):
        heap = make_heap([11, 9, 4, 7, 8, 3, 1, 2, 5, 6], 3)

        self.assertEqual(heap.FindMaxInRange(0, 100), 11)

    def test_inner_range(self):
        heap = make_heap([11, 9, 4, 7, 8, 3, 1, 2, 5, 6], 3)

        self.assertEqual(heap.FindMaxInRange(3, 6), 6)
        self.assertEqual(heap.FindMaxInRange(2, 2), 2)

    def test_no_keys_in_range(self):
        heap = make_heap([11, 9, 4, 7, 8, 3, 1, 2, 5, 6], 3)

        self.assertEqual(heap.FindMaxInRange(12, 20), -1)
        self.assertEqual(heap.FindMaxInRange(100, 50), -1)

    def test_borders_included(self):
        heap = make_heap([10, 20, 30], 1)

        self.assertEqual(heap.FindMaxInRange(10, 20), 20)
        self.assertEqual(heap.FindMaxInRange(30, 30), 30)

    def test_heap_not_changed(self):
        heap = make_heap([5, 3, 8, 1], 2)
        before = heap.HeapArray.copy()

        heap.FindMaxInRange(2, 4)

        self.assertEqual(heap.HeapArray, before)


class TestFindLess(unittest.TestCase):

    def test_empty_heap(self):
        heap = make_heap([], 2)

        self.assertEqual(heap.FindLess(10), -1)

    def test_one_element(self):
        heap = make_heap([5], 0)

        self.assertEqual(heap.FindLess(6), 5)
        self.assertEqual(heap.FindLess(5), -1)

    def test_found_key_is_less(self):
        heap = make_heap([11, 9, 4, 7, 8, 3, 1, 2, 5, 6], 3)

        result = heap.FindLess(4)

        self.assertIn(result, [1, 2, 3])

    def test_all_keys_bigger(self):
        heap = make_heap([11, 9, 4, 7, 8, 3, 1, 2, 5, 6], 3)

        self.assertEqual(heap.FindLess(1), -1)

    def test_min_key_found(self):
        heap = make_heap([11, 9, 4, 7, 8, 3, 1, 2, 5, 6], 3)

        self.assertEqual(heap.FindLess(2), 1)

    def test_zero_key(self):
        heap = make_heap([3, 0, 2], 1)

        self.assertEqual(heap.FindLess(1), 0)


class TestFindAllGreater(unittest.TestCase):

    def test_empty_heap(self):
        heap = make_heap([], 2)

        self.assertEqual(heap.FindAllGreater(0), [])

    def test_all_keys(self):
        keys = [11, 9, 4, 7, 8, 3, 1, 2, 5, 6]
        heap = make_heap(keys, 3)

        self.assertEqual(sorted(heap.FindAllGreater(0)), sorted(keys))

    def test_part_of_keys(self):
        heap = make_heap([11, 9, 4, 7, 8, 3, 1, 2, 5, 6], 3)

        self.assertEqual(sorted(heap.FindAllGreater(6)), [7, 8, 9, 11])

    def test_no_keys(self):
        heap = make_heap([11, 9, 4, 7, 8, 3, 1, 2, 5, 6], 3)

        self.assertEqual(heap.FindAllGreater(11), [])

    def test_strictly_greater(self):
        heap = make_heap([5, 5, 6], 1)

        self.assertEqual(heap.FindAllGreater(5), [6])


class TestMerge(unittest.TestCase):

    def test_merge_two_heaps(self):
        heap = make_heap([11, 4, 7], 2)
        other = make_heap([9, 3, 8, 1], 2)

        heap.Merge(other)

        self.assertEqual(sorted(values(heap)), [1, 3, 4, 7, 8, 9, 11])
        self.assertEqual(heap.HeapArray[0], 11)
        self.assertTrue(heap.IsHeap())

    def test_merge_empty_other(self):
        heap = make_heap([5, 3, 4], 1)
        before = heap.HeapArray.copy()

        heap.Merge(make_heap([], 2))

        self.assertEqual(heap.HeapArray, before)

    def test_merge_into_empty(self):
        heap = Heap()
        other = make_heap([5, 3, 4], 1)

        heap.Merge(other)

        self.assertEqual(sorted(values(heap)), [3, 4, 5])
        self.assertEqual(len(heap.HeapArray), 3)
        self.assertTrue(heap.IsHeap())

    def test_merge_grows_full_heap(self):
        heap = make_heap([1, 2, 3], 1)
        other = make_heap([10, 20, 30], 1)

        heap.Merge(other)

        self.assertEqual(len(heap.HeapArray), 7)
        self.assertEqual(sorted(values(heap)), [1, 2, 3, 10, 20, 30])
        self.assertEqual(heap.GetMax(), 30)
        self.assertTrue(heap.IsHeap())

    def test_other_becomes_empty(self):
        heap = make_heap([5], 1)
        other = make_heap([6, 7], 1)

        heap.Merge(other)

        self.assertEqual(other.GetMax(), -1)
        self.assertEqual(values(other), [])

    def test_merge_duplicates(self):
        heap = make_heap([5, 5], 1)
        other = make_heap([5, 5], 1)

        heap.Merge(other)

        self.assertEqual(values(heap), [5, 5, 5, 5])
        self.assertTrue(heap.IsHeap())


if __name__ == '__main__':
    unittest.main()
