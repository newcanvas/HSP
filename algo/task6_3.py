import unittest

from task6 import Deque
from task6_2 import isStringPalindrome, DynDeque, isBalanced

class DivTests(unittest.TestCase):

    # 7.2.

    def test_remove_front_empty(self):
        deque1 = Deque()
        self.assertIsNone(deque1.removeFront())
        self.assertIsNone(deque1.head)
        self.assertIsNone(deque1.tail)

    def test_add_remove_front_one(self):
        deque1 = Deque()
        deque1.addFront(10)
        self.assertEqual(deque1.head.value, 10)
        self.assertEqual(deque1.tail.value, 10)
        self.assertEqual(deque1.size(), 1)
        self.assertEqual(deque1.removeFront(), 10)
        self.assertEqual(deque1.size(), 0)
        self.assertIsNone(deque1.head)
        self.assertIsNone(deque1.tail)

    def test_add_remove_front_several(self):
        deque1 = Deque()
        for number in [1, 2, 3]:
            deque1.addFront(number)
        self.assertEqual(deque1.head.value, 3)
        self.assertEqual(deque1.tail.value, 1)
        self.assertEqual(deque1.size(), 3)
        self.assertEqual(deque1.removeFront(), 3)
        self.assertEqual(deque1.removeFront(), 2)
        self.assertEqual(deque1.removeFront(), 1)
        self.assertEqual(deque1.size(), 0)
        self.assertIsNone(deque1.head)
        self.assertIsNone(deque1.tail)

    def test_remove_tail_empty(self):
        deque1 = Deque()
        self.assertIsNone(deque1.removeTail())
        self.assertIsNone(deque1.head)
        self.assertIsNone(deque1.tail)

    def test_add_remove_tail_one(self):
        deque1 = Deque()
        deque1.addTail(10)
        self.assertEqual(deque1.head.value, 10)
        self.assertEqual(deque1.tail.value, 10)
        self.assertEqual(deque1.size(), 1)
        self.assertEqual(deque1.removeTail(), 10)
        self.assertEqual(deque1.size(), 0)
        self.assertIsNone(deque1.head)
        self.assertIsNone(deque1.tail)

    def test_add_remove_tail_several(self):
        deque1 = Deque()
        for number in [1, 2, 3]:
            deque1.addTail(number)
        self.assertEqual(deque1.head.value, 1)
        self.assertEqual(deque1.tail.value, 3)
        self.assertEqual(deque1.size(), 3)
        self.assertEqual(deque1.removeTail(), 3)
        self.assertEqual(deque1.removeTail(), 2)
        self.assertEqual(deque1.removeTail(), 1)
        self.assertEqual(deque1.size(), 0)
        self.assertIsNone(deque1.head)
        self.assertIsNone(deque1.tail)

    def test_add_front_remove_tail(self):
        deque1 = Deque()
        for number in [1, 2, 3]:
            deque1.addFront(number)
        self.assertEqual(deque1.head.value, 3)
        self.assertEqual(deque1.tail.value, 1)
        self.assertEqual(deque1.size(), 3)
        self.assertEqual(deque1.removeTail(), 1)
        self.assertEqual(deque1.removeTail(), 2)
        self.assertEqual(deque1.removeTail(), 3)
        self.assertEqual(deque1.size(), 0)
        self.assertIsNone(deque1.head)
        self.assertIsNone(deque1.tail)

    def test_add_tail_remove_front(self):
        deque1 = Deque()
        for number in [1, 2, 3]:
            deque1.addTail(number)
        self.assertEqual(deque1.head.value, 1)
        self.assertEqual(deque1.tail.value, 3)
        self.assertEqual(deque1.size(), 3)
        self.assertEqual(deque1.removeTail(), 3)
        self.assertEqual(deque1.removeTail(), 2)
        self.assertEqual(deque1.removeTail(), 1)
        self.assertEqual(deque1.size(), 0)
        self.assertIsNone(deque1.head)
        self.assertIsNone(deque1.tail)

    # 7.3.

    def test_palindrome_empty(self):
        result = isStringPalindrome('')
        self.assertEqual(result, True)

    def test_palindrome_true(self):
        result = isStringPalindrome('довод')
        self.assertEqual(result, True)

    def test_palindrome_false1(self):
        result = isStringPalindrome('макар')
        self.assertEqual(result, False)

    def test_palindrome_false2(self):
        result = isStringPalindrome('123')
        self.assertEqual(result, False)

    # 7.4.

    def test_return_min_empty(self):
        deque1 = Deque()
        self.assertIsNone(deque1.returnMin())

    def test_return_min_adding_front(self):
        deque1 = Deque()
        for i in range(1000):
            deque1.addFront(i)
        for i in range(-100, 0):
            deque1.addFront(i)
        self.assertEqual(deque1.returnMin(), -100)

    def test_return_min_adding_tail(self):
        deque1 = Deque()
        for i in range(1000):
            deque1.addTail(i)
        for i in range(-100, 0):
            deque1.addFront(i)
        self.assertEqual(deque1.returnMin(), -100)

    def test_return_min_adding_removing(self):
        deque1 = Deque()
        for i in range(1000):
            deque1.addTail(i)
        deque1.removeFront()
        self.assertEqual(deque1.returnMin(), 1)

    # 7.5.

    def test_add_within_buffer(self):
        da = DynDeque()
        for i in range(5):
            da.addFront(i)
        da.addTail(8)
        self.assertEqual(da[0], 4)
        self.assertEqual(da[4], 0)
        self.assertEqual(da[5], 8)
        self.assertEqual(da.count, 6)
        self.assertEqual(da.capacity, 16)

    def test_add_outside_buffers(self):
        da = DynDeque()
        for i in range(17):
            da.addTail(i)
        for i in range(17):
            da.addFront(i)
        self.assertEqual(da.count, 34)
        self.assertEqual(da.capacity, 64)
        self.assertEqual(da[0], 16)
        self.assertEqual(da[16], 0)
        self.assertEqual(da[17], 0)
        self.assertEqual(da[33], 16)

    def test_remove_no_resize(self):
        da = DynDeque()
        for i in range(5):
            da.addFront(i)
        da.addTail(8)
        self.assertEqual(da.removeFront(), 4)
        self.assertEqual(da.removeFront(), 3)
        self.assertEqual(da.removeFront(), 2)
        self.assertEqual(da.count, 3)
        self.assertEqual(da[0], 1)
        self.assertEqual(da[1], 0)
        self.assertEqual(da[2], 8)
        self.assertEqual(da.removeTail(), 8)
        self.assertEqual(da.count, 2)
        self.assertEqual(da.capacity, 16)

    def test_remove_resize(self):
        da = DynDeque()
        for i in range(17):
            da.addTail(i)
        for i in range(17):
            da.addFront(i)
        self.assertEqual(da.capacity, 64)
        for i in range(10):
            da.removeTail()
        for i in range(10):
            da.removeFront()
        self.assertEqual(da.count, 14)
        self.assertEqual(da.capacity, 16)
        self.assertEqual(da[0], 6)
        self.assertEqual(da[6], 0)
        self.assertEqual(da[7], 0)
        self.assertEqual(da[13], 6)

    # 7.6.

    def test_balance_empty(self):
        balance = isBalanced('')
        self.assertEqual(balance, None)

    def test_balance_mono_true(self):
        balance = isBalanced('12 + (33 // 89) == 0')
        self.assertEqual(balance, True)

    def test_balance_mono_false(self):
        balance = isBalanced('(57^33)()()))')
        self.assertEqual(balance, False)

    def test_balance_many_true(self):
        balance = isBalanced('()()((({21-23[]}[])))')
        self.assertEqual(balance, True)

    def test_balance_many_false(self):
        balance = isBalanced('()(90+9=[]){{({}}))99)')
        self.assertEqual(balance, False)

if __name__ == '__main__':
    unittest.main()
