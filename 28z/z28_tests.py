import unittest
from z28 import Keymaker

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(Keymaker(5), '10010')

    def test_min(self):
        self.assertEqual(Keymaker(1), '1')

if __name__ == '__main__':
    unittest.main()
