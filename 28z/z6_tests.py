import unittest
from z6 import PatternUnlock

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(PatternUnlock(10, [1,2,3,4,5,6,2,7,8,9]), "982843")

    def test_null(self):
        self.assertEqual(PatternUnlock(0, []), "")

if __name__ == '__main__':
    unittest.main()
