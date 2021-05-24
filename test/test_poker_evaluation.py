import unittest

from poker.poker import *


class TestPokerHand(unittest.TestCase):
    def test_two_pairs(self):
        """
        Test that can evaluate two pairs
        """
        data = '1S, 10C, 10H, 3D, 3S'
        result = evaluate_hands(data)
        self.assertEqual(result, 'two pair')

if __name__ == '__main__':
    unittest.main()