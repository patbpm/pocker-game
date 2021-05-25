#hand = input("What card do you have in the Hand? ")
hand = '10S,10C,10H,3D,3S'

def evaluate_hands(str):

    hand = str.split(",")
    # The suit for each card in the hand
    letters = [hand[i][1:] for i in range(5)] 
    # The number for each card in the hand
    numbers = [hand[i][:-1] for i in range(5)]  
    ranks = list(map(converter, numbers))

    # Repetitions count for each number
    rnum = [numbers.count(i) for i in numbers] 

    # Repetitions count for each letter 
    rlet = [letters.count(i) for i in letters]
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
   
   

def converter(num):
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
    

#print(evaluate_hands(hand))
