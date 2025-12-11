import unittest
from task5 import massdriver

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(massdriver([1,2,3,1,2,3,4]), 0)
    
    def test_regression2(self):
        self.assertEqual(massdriver([1,2,3,4,3,4,2]), 1)
    
    def test_regression3(self):
        self.assertEqual(massdriver([1,2,3,4,5,6,7]), -1)

if __name__ == '__main__':
    unittest.main()
