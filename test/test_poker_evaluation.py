import unittest

from poker.poker import *


class TestPokerHand(unittest.TestCase):
    def test_two_pairs(self):
        """
        Test that can evaluate two pairs
        """
        data = 'AS, 10C, 10H, 3D, 3S'
        result = evaluate_hands(data)
        self.assertEqual(result, 'two pair')
    
    def test_pairs(self):
        """
        Test that can evaluate pairs
        """
        data = 'AS, 10C, 10H,JD, 3S'
        result = evaluate_hands(data)
        self.assertEqual(result, 'pair')
    
    def test_three_of_a_kind(self):
        """
        Test that can evaluate three of a kind
        """
        data = 'AS,AC,AH,JD,3S'
        result = evaluate_hands(data)
        self.assertEqual(result, 'three of a kind')
    
    def test_four_of_a_kind(self):
        """
        Test that can evaluate four of a kind
        """
        data = 'AS,AC,AH,AD,3S'
        result = evaluate_hands(data)
        self.assertEqual(result, 'four of a kind')
    
    def test_full_house(self):
        """
        Test that can evaluate full house
        """
        data = 'AS,AC,AH,3D,3S'
        result = evaluate_hands(data)
        self.assertEqual(result, 'full house')

if __name__ == '__main__':
    unittest.main()