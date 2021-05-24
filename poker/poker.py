#hand = input("What card do you have in the Hand? ")
hand = 'AS,10C,10H,3D,3S'

def evaluate_hands(str):

    hand = str.split(",")
    # The suit for each card in the hand
    letters = [hand[i][1:] for i in range(5)] 
    # The number for each card in the hand
    numbers = [hand[i][:-1] for i in range(5)]  
    

    # Repetitions count for each number
    rnum = [numbers.count(i) for i in numbers] 

    # Repetitions count for each letter 
    rlet = [letters.count(i) for i in letters]  
    return numbers
    
def converter(number):
    if num == 'A':
        return 14
    if

print(evaluate_hands(hand))
