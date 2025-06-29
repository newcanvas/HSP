import unittest
from random import randint
from exercise_code import sort_mass

class SortTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(sort_mass([3,2,1]), [1,2,3])

    def test_random(self):
        my_list = []
        for i in range(100):
            my_list.append(randint(-1000,1000))
            x = sort_mass(my_list)
            my_list.sort()
        self.assertEqual(x, my_list)

    def test_null(self):
        my_list = []
        self.assertEqual(my_list, [])

    def test_max(self):
        my_list = []
        for i in range(100):
            my_list.append(randint(100000000000000000, 1000000000000000000))
            x = sort_mass(my_list)
            my_list.sort()
        self.assertEqual(x, my_list)

if __name__ == '__main__':
    unittest.main()
