import unittest
from task3 import DynArray
from task3_2 import DynArray_2, MultiDynArray


class DivTests(unittest.TestCase):

    # 1.

    def test_insert_within_buffer(self):
        da = DynArray()
        for i in range(5):
            da.append(i)
        da.insert(0,8)
        self.assertEqual(da.array[0], 8)
        self.assertEqual(da.array[1], 0)
        self.assertEqual(da.array[da.count-1], 4)
        self.assertEqual(da.count, 6)
        self.assertEqual(da.capacity, 16)

    def test_insert_outside_buffer(self):
        da = DynArray()
        for i in range(16):
            da.append(i)
        da.insert(16,99)
        self.assertEqual(da.array[0], 0)
        self.assertEqual(da.array[16], 99)
        self.assertEqual(da.array[da.count-1], 99)
        self.assertEqual(da.count, 17)
        self.assertEqual(da.capacity, 32)

    def test_insert_incorrect_i(self):
        with self.assertRaises(Exception):
            da = DynArray()
            for i in range(16):
                da.append(i)
            da.insert(99,0)

    # 2.

    def test_delete_within_buffer(self):
        da = DynArray()
        for i in range(5):
            da.append(i)
        da.delete(0)
        self.assertEqual(da.array[0], 1)
        self.assertEqual(da.array[da.count-1], 4)
        self.assertEqual(da.count, 4)
        self.assertEqual(da.capacity, 16)

    def test_delete_minimize_buffer(self):
        da = DynArray()
        for i in range(17):
            da.append(i)
        da.delete(16)
        self.assertEqual(da.array[0], 0)
        self.assertEqual(da.array[da.count-1], 15)
        self.assertEqual(da.count, 16)
        self.assertEqual(da.capacity, 21)

    def test_delete_incorrect_i(self):
        with self.assertRaises(Exception):
            da = DynArray()
            for i in range(16):
                da.append(i)
            da.delete(99)

    def test_delete_last(self):
        da = DynArray()
        for i in range(5):
            da.append(i)
        da.delete(4)
        self.assertEqual(da.array[0], 0)
        self.assertEqual(da.array[da.count-1], 3)
        self.assertEqual(da.count, 4)
        self.assertEqual(da.capacity, 16)

    # 5.

    def test_bank_grows_without_resize(self):
        da = DynArray_2()
        for i in range(5):
            da.append(i)
        self.assertEqual(da.count, 5)
        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.bank, 10)

    def test_resize_paid_by_bank(self):
        da = DynArray_2()
        for i in range(16):
            da.append(i)
        bank_before = da.bank
        da.append(99)
        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 17)
        self.assertEqual(da.bank, bank_before - 16 + 2)

    def test_insert_does_not_spend_bank(self):
        da = DynArray_2()
        for i in range(5):
            da.append(i)
        bank_before = da.bank
        da.insert(2, 99)
        self.assertEqual(da.bank, bank_before + 2)
        self.assertEqual(da.count, 6)
        self.assertEqual(da.capacity, 16)

    def test_bank_never_negative(self):
        da = DynArray_2()
        for i in range(100):
            da.append(i)
            self.assertGreaterEqual(da.bank, 0)
        for i in range(10):
            da.insert(0, -i)
            self.assertGreaterEqual(da.bank, 0)

    # 6.

    def test_initial_access(self):
        arr = MultiDynArray((2, 2))
        self.assertIsNone(arr[0, 0])
        self.assertIsNone(arr[1, 1])

    def test_set_and_get_value(self):
        arr = MultiDynArray((2, 2, 2))
        arr[1, 0, 1] = 42
        self.assertEqual(arr[1, 0, 1], 42)

    def test__resize_on_set(self):
        arr = MultiDynArray((2, 2))
        arr[3, 1] = 99
        self.assertEqual(arr[3, 1], 99)
        self.assertIsNone(arr[2, 0])

    def test_incorrect_indices_count(self):
        arr = MultiDynArray((2, 2, 2))
        with self.assertRaises(IndexError):
            arr[1, 2] = 10

if __name__ == '__main__':
    unittest.main()
