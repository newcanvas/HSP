import unittest
from z14 import Unmanned

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(Unmanned(10, 2, [ [3,5,5], [5,2,2] ]), 12)

if __name__ == '__main__':
    unittest.main()
