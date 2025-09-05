import unittest
from z15 import TankRush

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(TankRush(3, 4, '1234 2345 0987', 2, 2, '34 98'), True)

if __name__ == '__main__':
    unittest.main()
