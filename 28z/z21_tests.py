import unittest
from z21 import BiggerGreater

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(BiggerGreater('ая'), 'яа')
    
    def test_regression2(self):
        self.assertEqual(BiggerGreater('fff'), '')
    
    def test_regression3(self):
        self.assertEqual(BiggerGreater('нклм'), 'нкмл')

    def test_regression4(self):
        self.assertEqual(BiggerGreater('вибк'), 'викб')

    def test_regression5(self):
        self.assertEqual(BiggerGreater('вкиб'), 'ибвк')

if __name__ == '__main__':
    unittest.main()
