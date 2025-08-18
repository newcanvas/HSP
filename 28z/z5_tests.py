import unittest
from z5 import SynchronizingTables

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(SynchronizingTables(4, [50, 1, 2, 1024], [20000, 100000, 90000, 20000]), [90000, 20000, 20000, 100000])

    def test_max(self):
        self.assertEqual(SynchronizingTables(3, [50, 1, 1024], [9223372036854775808, 9223372036854775809, 9223372036854775801]), [9223372036854775808,9223372036854775801,9223372036854775809])

    def test_null(self):
        self.assertEqual(SynchronizingTables(1, [0], [0]), [0])

if __name__ == '__main__':
    unittest.main()
