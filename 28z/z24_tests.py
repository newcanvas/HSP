import unittest
from z24 import MatrixTurn

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(MatrixTurn(["123456", "234567", "345678", "456789"], 4,6, 3), ['212345', '343456', '456767', '567898'])
