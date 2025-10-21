import unittest
from z27 import Football

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(Football([1,3,2], 3), True)
    
    def test_regression2(self):
        self.assertEqual(Football([1,7,5,3,9], 5), True)
    
    def test_regression3(self):
        self.assertEqual(Football([3,2,1], 3), True)

    def test_regression4(self):
        self.assertEqual(Football([9,5,3,7,1], 5), False)

    def test_regression5(self):
        self.assertEqual(Football([1,4,3,2,5], 5), True)

    def test_regression6(self):
        self.assertEqual(Football([1,2,3], 3), False)

if __name__ == '__main__':
    unittest.main()
