import unittest
from z9 import TheRabbitsFoot

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(TheRabbitsFoot('отдай мою кроличью лапку', True), 'омоюу толл дюиа акчп йрьк')
        self.assertEqual(TheRabbitsFoot('омоюу толл дюиа акчп йрьк', False), 'отдаймоюкроличьюлапку')

if __name__ == '__main__':
    unittest.main()
