import unittest
from task2 import digital_rain

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(digital_rain("1111000"), "111000")
    
    def test_regression2(self):
        self.assertEqual(digital_rain("11101000"), "11101000")
    
    def test_regression3(self):
        self.assertEqual(digital_rain("011111110"), "10")

    def test_regression4(self):
        self.assertEqual(digital_rain("11111111"), "")

if __name__ == '__main__':
    unittest.main()
