import unittest
from z13 import UFO

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(UFO(2, [1234, 1777], True), [668, 1023])
    
    def test_regression2(self):
        self.assertEqual(UFO(2, [1234, 1777], False), [4660, 6007])

if __name__ == '__main__':
    unittest.main()
