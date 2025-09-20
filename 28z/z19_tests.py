import unittest
from z19 import ShopOLAP

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(ShopOLAP(5, ['платье1 5', 'сумка32 2', 'платье1 1', 'сумка23 2', 'сумка128 4']), ['платье1 6', 'сумка128 4', 'сумка23 2', 'сумка32 2'])

    def test_regression2(self):
        self.assertEqual(ShopOLAP(5,['dress1 5','handbug32 3','dress2 1','handbug23 2','handbug128 4']), ['dress1 5','handbug128 4','handbug32 3','handbug23 2','dress2 1'])
    
    def test_min(self):
        self.assertEqual(ShopOLAP(1, ['платье1 5']), ['платье1 5'])

if __name__ == '__main__':
    unittest.main()
