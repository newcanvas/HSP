import unittest
from z16 import MaximumDiscount

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(MaximumDiscount(7, [400, 350, 300, 250, 200, 150, 100]), 450)

    def test_max(self):
        self.assertEqual(MaximumDiscount(3, [9999999999999999, 9999999999999999, 9999999999999999]), 9999999999999999)

    def test_null(self):
        self.assertEqual(MaximumDiscount(4, [0, 0, 0, 0]), 0)

if __name__ == '__main__':
    unittest.main()
