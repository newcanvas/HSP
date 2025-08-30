import unittest
from z12 import MassVote

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(MassVote(4, [111, 111, 110, 110]), 'no winner')
    
    def test_regression2(self):
        self.assertEqual(MassVote(5, [60, 10, 10, 15, 5]), 'majority winner 1')

    def test_regression3(self):
        self.assertEqual(MassVote(3, [10, 15, 10]), 'minority winner 2')

    def test_max(self):
        self.assertEqual(MassVote(3, [9999999999999999, 9999999999999999, 9999999999999999]), 'no winner')

    def test_null(self):
        self.assertEqual(MassVote(4, [0, 0, 0, 0]), 'no winner')

if __name__ == '__main__':
    unittest.main()
