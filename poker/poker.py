class PokerHand:
    RANKS = {
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "J",
        12: "Q",
        13: "K",
        14: "A",
    }
    SUITS = [
         "H",  # Hearts
         "D",  # Diamonds
         "C",  # Clubs
         "S",  # Spades
    ]
    def __init__(self, cards):
        self.hand = cards
        hand = self.hand.split(",")
        # The suit for each card in the hand
        self.letters = [hand[i][-1:] for i in range(5)] 
        # The number for each card in the hand
        numbers = [hand[i][:-1] for i in range(5)]  
        self.ranks = list(map(self.converter, numbers))

        for index in range(len(hand)):
            if self.ranks[index] not in PokerHand.RANKS:
                raise ValueError("Invalid card rank")
            if self.letters[index] not in PokerHand.SUITS:
                raise ValueError("Invalid card suit")
        
        


    def evaluate_hands( self):

        # Repetitions count for each number
        rnum = [self.ranks.count(i) for i in self.ranks] 

        # Repetitions count for each letter 
        rlet = [self.letters.count(i) for i in self.letters]
        #return rnum 
        
        if rnum.count(2) == 4:
            return 'two pair'
        elif 3 in rnum:
            if rnum.count(3) == 3 and rnum.count(2) == 2:
                return 'full house'
            else:
                return 'three of a kind'
        elif 4 in rnum:
            return 'four of a kind'
        elif sorted(rnum) == [2,2,3,3,3]:
            return 'full house'
        elif rnum.count(2) == 2:
            return 'pair'
        else:
            return 'High Card'
    
    

    def converter(self, num):
        if num == 'A':
            return 14
        elif num == 'K':
            return 13
        elif num == 'Q':
            return 12
        elif num == 'J':
            return 11
        else:
            return int(num)
    
    def verification(self, ):
        if num == 'A':
            return 14
        
#hand = input("What card do you have in the Hand? ")
hand = '10S,AC,10D,3D,3S'
#print(evaluate_hands(hand))
poker = PokerHand(hand)
print(poker.evaluate_hands())
