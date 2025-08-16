import unittest
from z4 import MadMax

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(MadMax(7, [1,2,3,4,5,6,7]), [1,2,3,7,6,5,4])

    def test_max(self):
        self.assertEqual(MadMax(3, [9223372036854775808, 9223372036854775809, 9223372036854775801]), [9223372036854775801,9223372036854775809,9223372036854775808])

    def test_null(self):
        self.assertEqual(MadMax(1, [0]), [0])

if __name__ == '__main__':
    unittest.main()
