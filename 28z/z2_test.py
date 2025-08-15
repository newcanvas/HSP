import unittest
from z2 import odometer

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(odometer([10,1,20,4]), 70)

    def test_max(self):
        self.assertEqual(odometer([9223372036854775808,1,10,2]), 9223372036854775818)

    def test_null(self):
        self.assertEqual(odometer([0,1,0,3,0,9]), 0)

if __name__ == '__main__':
    unittest.main()
