import unittest
from z8 import SumOfThe

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(SumOfThe(7, [10,-25,-45,-35,5]), -45)

    def test_null(self):
        self.assertEqual(SumOfThe(2, [0,0]), 0)

if __name__ == '__main__':
    unittest.main()
