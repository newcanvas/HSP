import unittest
from task4 import artificial_muscle_fibers

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(artificial_muscle_fibers([1,2,3,4,5]), 0)
    
    def test_regression2(self):
        self.assertEqual(artificial_muscle_fibers([1,2,3,2,1]), 2)
    
    def test_regression3(self):
        self.assertEqual(artificial_muscle_fibers([1,2,3,2,1,2,4,2,1]), 2)

if __name__ == '__main__':
    unittest.main()
