import unittest
from task6 import TRC_sort

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(TRC_sort([2,1,0]), [0,1,2])
    
    def test_regression2(self):
        self.assertEqual(TRC_sort([0,1,2,1,0,2]), [0,0,1,1,2,2])
    
    def test_regression3(self):
        self.assertEqual(TRC_sort([1,2,0,2,1,0,0,0,1]), [0,0,0,0,1,1,1,2,2])

if __name__ == '__main__':
    unittest.main()
