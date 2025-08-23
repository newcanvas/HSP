import unittest
from z7 import WordSearch

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(WordSearch(12, "1) строка разбивается на набор строк через выравнивание по заданной ширине.", "строк"), [0,0,0,1,0,0,0])

    def test_null(self):
        self.assertEqual(WordSearch(12, "", "строка"), [])

if __name__ == '__main__':
    unittest.main()
