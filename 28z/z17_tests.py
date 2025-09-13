import unittest
from z17 import LineAnalysis

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(LineAnalysis('*..*..*..*..*..*..*'), True)
    
    def test_regression2(self):
        self.assertEqual(LineAnalysis('*..*..*..*..*..*...*'), False)
    
    def test_min(self):
        self.assertEqual(LineAnalysis('*'), True)

    def test_max(self):
        self.assertEqual(LineAnalysis('*' * 99999), True)

    def test_null(self):
        self.assertEqual(LineAnalysis(''), False)

if __name__ == '__main__':
    unittest.main()
