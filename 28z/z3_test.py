import unittest
from z3 import ConquestCampaign

class DivTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(ConquestCampaign(3,4,2,[2,2, 3,4]), 3)

if __name__ == '__main__':
    unittest.main()
