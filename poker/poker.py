hand = input("What is you card? ")

def evaluate_hands(str):

    hand = str.split(",")
    # The suit for each card in the hand
    letters = [hand[i][1:] for i in range(5)] 
    # The number for each card in the hand
    numbers = [int(hand[i][:1]) for i in range(5)]  

    # Repetitions count for each number
    rnum = [numbers.count(i) for i in numbers] 

    # Repetitions count for each letter 
    rlet = [letters.count(i) for i in letters]  
    if rnum.count(2) == 4:
        return 'two pair'
    elif 3 in rnum:
        return 'three of a kind'
    elif 4 in rnum:
        return 'four of a kind'
    elif sorted(rnum) == [2,2,3,3,3]:
        return 'full house'
    elif rnum.count(2) == 2:
        return 'pair'
    elif max(numbers) - min(numbers) ==4:
        return 'straight'
    else:
        return 'Nothing'


print(evaluate_hands(hand))