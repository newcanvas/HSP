import unittest
from task3 import EEC_help

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(EEC_help([1,2,3], [1,2,3]), True)
    
    def test_regression2(self):
        self.assertEqual(EEC_help([1,2,3], [1,2,3,4]), False)
    
    def test_regression3(self):
        self.assertEqual(EEC_help([1,3,2], [1,2,3]), True)

    def test_regression4(self):
        self.assertEqual(EEC_help([1,3,2,3], [1,2,2,3]), False)

    def test_regression5(self):
        self.assertEqual(EEC_help([1,1], [1,1]), True)

if __name__ == '__main__':
    unittest.main()
