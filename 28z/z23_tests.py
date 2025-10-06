import unittest
from z23 import TreeOfLife

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(TreeOfLife(3,4, 1, [".+..","..+.",".+.."]), ["++++","++++","++++"])
    
    def test_regression2(self):
        self.assertEqual(TreeOfLife(3,4, 2, [".+..","..+.",".+.."]), ["...+","+...","...+"])
    
    def test_regression3(self):
        self.assertEqual(TreeOfLife(3,4, 3, [".+..","..+.",".+.."]), ["++++","++++","++++"])

    def test_regression4(self):
        self.assertEqual(TreeOfLife(3,4, 4, [".+..","..+.",".+.."]), [".+..","..+.",".+.."])

    def test_regression5(self):
        self.assertEqual(TreeOfLife(6,7,24,['.......','...+...','....+..','.......','++.....','++.....']), ['.......','...+...','....+..','.......','++.....','++.....'])

if __name__ == '__main__':
    unittest.main()
