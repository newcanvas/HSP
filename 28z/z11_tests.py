import unittest
from z11 import BigMinus

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(BigMinus('1234567891', '1'), '1234567890')

    def test_max(self):
        self.assertEqual(BigMinus('10^16', '1'), '9999999999999999')

    def test_null(self):
        self.assertEqual(BigMinus('0', '0'), '0')

if __name__ == '__main__':
    unittest.main()
