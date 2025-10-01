import unittest
from z22 import SherlockValidString

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(SherlockValidString('xyz'), True)
    
    def test_regression2(self):
        self.assertEqual(SherlockValidString('xyzaa'), True)
    
    def test_regression3(self):
        self.assertEqual(SherlockValidString('xxyyz'), True)

    def test_regression4(self):
        self.assertEqual(SherlockValidString('xyzzz'), False)

    def test_regression5(self):
        self.assertEqual(SherlockValidString('xxyyza'), False)

    def test_regression6(self):
        self.assertEqual(SherlockValidString('xxyyzabc'), False)

if __name__ == '__main__':
    unittest.main()
