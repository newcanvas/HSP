import unittest

from task10 import PowerSet
from task10_2 import FindMultiIntersection, Bag

class DivTests(unittest.TestCase):

    # 3.

    def test_ps_put(self):
        ps = PowerSet()
        self.assertEqual(ps.size(), 0)
        ps.put(1)
        ps.put(1)
        self.assertEqual(ps.pow_set, [1])
        self.assertEqual(ps.size(), 1)

    def test_ps_get(self):
        ps = PowerSet()
        self.assertEqual(ps.get(123), False)
        ps.put(123)
        ps.put(1333)
        self.assertEqual(ps.size(), 2)
        self.assertEqual(ps.get(123), True)
        self.assertEqual(ps.get(12322), False)

    def test_ps_remove(self):
        ps = PowerSet()
        ps.put(123)
        ps.put(1333)
        ps.put(1818)
        self.assertEqual(ps.size(), 3)
        self.assertEqual(ps.get(123), True)
        self.assertEqual(ps.remove(123), True)
        self.assertEqual(ps.get(123), False)
        self.assertEqual(ps.size(), 2)
        self.assertEqual(ps.remove(1213), False)
        self.assertEqual(ps.size(), 2)

    def test_ps_intersection(self):
        ps = PowerSet()
        ps2 = PowerSet()
        result = ps.intersection(ps2)
        self.assertEqual(result.pow_set, [])
        ps.put(123)
        ps.put(1333)
        result = ps.intersection(ps2)
        self.assertEqual(result.pow_set, [])
        ps.put(1818)
        ps.put(1000)
        ps2.put(123)
        ps2.put(1333)
        ps2.put(1818)
        ps2.put(0)
        result = ps.intersection(ps2)
        self.assertEqual(result.pow_set, [123, 1333, 1818])

    def test_ps_union(self):
        ps = PowerSet()
        ps2 = PowerSet()
        result = ps.union(ps2)
        self.assertEqual(result.pow_set, [])
        ps.put(123)
        ps.put(1333)
        result = ps.union(ps2)
        self.assertEqual(result.pow_set, [123, 1333])
        ps.put(1818)
        ps.put(1000)
        ps2.put(123)
        ps2.put(1333)
        ps2.put(1818)
        ps2.put(0)
        result = ps.union(ps2)
        self.assertEqual(result.pow_set, [123, 1333, 1818, 1000, 0])

    def test_ps_difference(self):
        ps = PowerSet()
        ps2 = PowerSet()
        result = ps.difference(ps2)
        self.assertEqual(result.pow_set, [])
        ps.put(123)
        ps.put(1333)
        result = ps.difference(ps2)
        self.assertEqual(result.pow_set, [123, 1333])
        ps.put(1818)
        ps.put(1000)
        ps.put(100220)
        ps2.put(123)
        ps2.put(1333)
        ps2.put(1818)
        ps2.put(0)
        result = ps.difference(ps2)
        self.assertEqual(result.pow_set, [1000, 100220])

    def test_ps_sub_1(self):
        ps = PowerSet()
        ps2 = PowerSet()
        for i in range(20):
            ps.put(i)
        for i in range(5):
            ps2.put(i)
        result = ps.issubset(ps2)
        self.assertEqual(result, True)

    def test_ps_sub_2(self):
        ps = PowerSet()
        ps2 = PowerSet()
        for i in range(5):
            ps.put(i)
            ps2.put(i)
        result = ps.issubset(ps2)
        self.assertEqual(result, True)

    def test_ps_sub_3(self):
        ps = PowerSet()
        ps2 = PowerSet()
        for i in range(15):
            ps.put(i)
        for i in range(10, 20):
            ps2.put(i)
        result = ps.issubset(ps2)
        self.assertEqual(result, False)

    def test_ps_equals(self):
        ps = PowerSet()
        ps2 = PowerSet()
        result = ps.equals(ps2)
        self.assertEqual(result, True)
        ps.put(123)
        ps.put(1333)
        result = ps.equals(ps2)
        self.assertEqual(result, False)
        self.assertEqual(ps.size(), 2)
        self.assertEqual(ps2.size(), 0)
        for i in range(20000):
            ps.put(i)
        for i in range(20000, 40000):
            ps2.put(i)
        result = ps.equals(ps2)
        self.assertEqual(result, False)

    # 4.

    def test_decart_basic(self):
        s1 = PowerSet()
        s2 = PowerSet()
        s1.put(1)
        s1.put(2)
        s2.put(3)
        s2.put(4)
        result = s1.decart(s2)
        self.assertEqual(sorted(result), sorted([(1, 3), (1, 4), (2, 3), (2, 4)]))

    def test_decart_empty_first(self):
        s1 = PowerSet()
        s2 = PowerSet()
        s2.put(1)
        s2.put(2)
        result = s1.decart(s2)
        self.assertEqual(result, [])

    def test_decart_empty_second(self):
        s1 = PowerSet()
        s2 = PowerSet()
        s1.put(1)
        s1.put(2)
        result = s1.decart(s2)
        self.assertEqual(result, [])

    def test_decart_single_elements(self):
        s1 = PowerSet()
        s2 = PowerSet()
        s1.put(5)
        s2.put(9)
        result = s1.decart(s2)
        self.assertEqual(result, [(5, 9)])

    # 5.

    def test_ps_fmi(self):
        ps = PowerSet()
        ps2 = PowerSet()
        ps3 = PowerSet()
        ps_list = [ps, ps2, ps3]
        result = FindMultiIntersection(ps_list)
        self.assertEqual(result.pow_set, [])

    def test_ps_fmi_1(self):
        ps = PowerSet()
        ps2 = PowerSet()
        ps3 = PowerSet()
        for i in range(5):
            ps.put(i)
            ps2.put(i)
        for i in range(3, 10):
            ps3.put(i)
        ps_list = [ps, ps2, ps3]
        result = FindMultiIntersection(ps_list)
        self.assertEqual(result.pow_set, [3,4])

    def test_ps_fmi_2(self):
        ps = PowerSet()
        ps2 = PowerSet()
        ps3 = PowerSet()
        for i in range(5):
            ps.put(i)
        for i in range(6,10):
            ps2.put(i)
        for i in range(10, 100):
            ps3.put(i)
        ps_list = [ps, ps2, ps3]
        result = FindMultiIntersection(ps_list)
        self.assertEqual(result.pow_set, [])

    def test_ps_fmi_3(self):
        ps = PowerSet()
        ps2 = PowerSet()
        ps3 = PowerSet()
        ps4 = PowerSet()
        for i in range(100):
            ps.put(i)
            ps2.put(i)
        for i in range(10):
            ps3.put(i)
        for i in range(80):
            ps4.put(i)
        ps_list = [ps, ps2, ps3, ps4]
        result = FindMultiIntersection(ps_list)
        self.assertEqual(result.pow_set, [0,1,2,3,4,5,6,7,8,9])

    # 6.

    # put

    def test_put_single(self):
        b = Bag()
        b.put(1)
        self.assertEqual(b.get_all(), {1: 1})
        self.assertEqual(len(b.pow_set), 1)

    def test_put_duplicates(self):
        b = Bag()
        b.put(1)
        b.put(1)
        b.put(1)
        self.assertEqual(b.get_all(), {1: 3})
        self.assertEqual(len(b.pow_set), 3)

    def test_put_different_values(self):
        b = Bag()
        b.put(1)
        b.put(2)
        b.put(3)
        self.assertEqual(b.get_all(), {1: 1, 2: 1, 3: 1})
        self.assertEqual(len(b.pow_set), 3)

    def test_put_mixed(self):
        b = Bag()
        b.put(1)
        b.put(2)
        b.put(1)
        b.put(2)
        b.put(1)
        self.assertEqual(b.get_all(), {1: 3, 2: 2})

    # remove

    def test_remove_existing_once(self):
        b = Bag()
        b.put(1)
        result = b.remove(1)
        self.assertEqual(result, True)
        self.assertEqual(b.get_all(), {})
        self.assertEqual(len(b.pow_set), 0)

    def test_remove_multiple(self):
        b = Bag()
        b.put(1)
        b.put(1)
        b.remove(1)
        self.assertEqual(b.get_all(), {1: 1})
        self.assertEqual(len(b.pow_set), 1)

    def test_remove_non_existing(self):
        b = Bag()
        b.put(1)
        result = b.remove(2)
        self.assertEqual(result, False)
        self.assertEqual(b.get_all(), {1: 1})

    def test_remove_until_empty(self):
        b = Bag()
        b.put(1)
        b.put(1)
        b.remove(1)
        b.remove(1)
        self.assertEqual(b.get_all(), {})
        self.assertEqual(len(b.pow_set), 0)

    # get_all

    def test_get_all_empty(self):
        b = Bag()
        self.assertEqual(b.get_all(), {})

    def test_get_all_after_put(self):
        b = Bag()
        b.put(1)
        b.put(2)
        self.assertEqual(b.get_all(), {1: 1, 2: 1})

    def test_get_all_after_operations(self):
        b = Bag()
        b.put(1)
        b.put(1)
        b.remove(1)
        self.assertEqual(b.get_all(), {1: 1})

    def test_get_all_zero(self):
        b = Bag()
        b.put(1)
        b.remove(1)
        self.assertEqual(b.get_all(), {})

if __name__ == '__main__':
    unittest.main()
