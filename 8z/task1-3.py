import unittest
from task1 import white_walker_2

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(white_walker_2("axxb6===4xaf5===eee5"), True)
    
    def test_regression2(self):
        self.assertEqual(white_walker_2("5==ooooooo=5=5"), False)
    
    def test_regression3(self):
        self.assertEqual(white_walker_2("abc=7==hdjs=3gg1=======5"), True)

    def test_regression4(self):
        self.assertEqual(white_walker_2("aaS=8"), False)

    def test_regression5(self):
        self.assertEqual(white_walker_2("9===1===9===1===9"), True)

if __name__ == '__main__':
    unittest.main()
