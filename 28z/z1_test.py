import unittest
from z1 import squirrel

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(squirrel(5), 1)

    def test_max(self):
          self.assertEqual(squirrel(1420), 3)

if __name__ == '__main__':
    unittest.main()
