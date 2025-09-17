import unittest
from z18 import MisterRobot

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(MisterRobot(7, [1,3,4,5,6,2,7]), True)


if __name__ == '__main__':
    unittest.main()
