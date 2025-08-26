import unittest
from z10 import PrintingCosts

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(PrintingCosts('! M'), 37)

    def test_max(self):
        self.assertEqual(PrintingCosts('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'), 1888)

    def test_null(self):
        self.assertEqual(PrintingCosts(' '), 0)

if __name__ == '__main__':
    unittest.main()
