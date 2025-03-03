# FUNCTION TESTS COMMENTED AT BOTTOM OF FUNCTION
# Created a main function for the purposes of easy modual exportation and parameter jumping. 
# Also allows for easy importation of user created lists of card numbers to check instead of always making new ones.
def cardValidator(cards = {}):

    # as user create a list, not necessary if main function is called with a list as a parameter
    def phase1(): 
        id = 1
        
        # create dictionary
        if isinstance(cards, dict):
            while(id <= 3):            
                cards[id] = input(f"Please input a credit card number\n: ").strip()
                id += 1 

        # create list
        elif isinstance(cards, list):
            while(id <= 3):            
                cards.append(input(f"Please input a credit card number\n: ").strip())
                id += 1 

                    
                                        
    #phase 2        
    def phase2():

        # check dictonary for errors and duplicates
        if isinstance(cards, dict):
            removed = {}
            clones = {}
            seen = {}  # Store first occurrence of each number

            for card in cards.keys():
                try:
                    cards[card] = int(cards[card])   
                except ValueError:             
                    print(f"Card number {cards[card]} ID {card} contains non-numeric characters. Throwing out.\n")
                    removed[card] = cards[card]  # Remove invalid card
                    continue

                if len(str(cards[card])) != 16:
                    print(f"Card number {cards[card]} ID {card} is not 16 digits long. Throwing out.\n")
                    removed[card] = cards[card]
                    continue

                if str(cards[card])[0] not in "456":
                    print(f"Card number {cards[card]} ID {card} does not start with '4' '5' or '6'. Throwing out.\n")
                    removed[card] = cards[card]
                    continue

            # Check for duplicates in DICT version


            for card in list(cards.keys()):  # Iterate over a copy
                value = cards[card]
                
                if value in seen:  # If card value was already seen, it's a duplicate
                    print(f"Card number {value} ID {card} is a duplicate of ID {seen[value]}. Throwing out duplicate.\n")
                    clones[card] = value  # Store duplicate
                else:
                    seen[value] = card  # Track first occurrence     
            # print all errors and clones
            print(f"\nInvalid cards removed: {removed}")
            print(f"Duplicate cards removed: {clones}\n")
            
            # remove all incorrect values and duplicates
            for card in removed.keys():
                del cards[card]
            
            for card in clones.keys():
                del cards[card]

        # check LIST for errors
        
        elif isinstance(cards, list):
            removed = []
            i = len(cards) - 1

            while i >= 0:
                try:
                    cards[i] = int(cards[i])
                
                except ValueError:
                    print(f"Card number {cards[i]} contains non-numeric characters. Throwing out.\n")
                    removed.append(cards.pop(i))
                    continue

                if len(str(cards[i])) != 16:
                    print(f"Card number {cards[i]} is not 16 digits long. Throwing out.\n")
                    removed.append(cards.pop(i))
                    continue

                if str(cards[i])[0] not in "456":
                    print(f"Card number {cards[i]} does not start with '4' '5' or '6'. Throwing out.\n")
                    removed.append(cards.pop(i))
                    continue
                i -= 1

            i = len(cards) - 1
            clones = []
            seen = set()
            # Check for duplicates in LIST version
            for i in reversed(range(len(cards))):  # Iterate in reverse to avoid skipping elements
                if cards[i] in seen:
                    print(f"Card number {cards[i]} has a duplicate. Throwing out duplicate.\n")
                    clones.append(cards.pop(i))  # Remove duplicate
                else:
                    seen.add(cards[i])
            
            i -= 1
                    
            # print errors and duplicates
            print(f"\nInvalid cards removed: {removed}")
            print(f"Duplicate cards removed: {clones}")



    # phase 3
    def phase3():
        # take valid cards and format them to look like "####-####-####-####" - dict version
        if isinstance(cards, dict):
            for card in cards.keys():

                cardNum = str(cards[card])
                numForm = "-".join([cardNum[i:i+4] for i in range(0,16,4)])
                cards[card] = numForm

        # take valid cards and format them to look like "####-####-####-####" - list version
        elif isinstance(cards, list):
            for i, card in list(enumerate(cards)):

                cardNum = str(card)
                numForm = "-".join([cardNum[i:i+4] for i in range(0,16,4)])
                cards[i] = numForm

        
        return cards


    if cards == {} or cards == []:
        phase1()
    phase2()
    phase3()
    return cards


# used to test an external dictionary
cardDict = {1:4234567890909999, 2:4234567890909999, 3:"4234567890909997m", 4:1234567890909995, 5:423456, 6:4234567890909999, 7:5234567890910000}

# used to test an external list
cardList = [4234567890909999, 4234567890909999, '4234567890909997m', 1234567890909995, 423456, 4234567890909999, 5234567890910000]

# below are function call tests uncomment/comment any one of them to test cardValidator. If you find any errors please let me know!
# print(cardValidator(cardDict)) #Use external predefined dictonary
# print(cardValidator(cardList)) #Use external predefined list
# print(cardValidator()) #Make your own 3 length dictionary
print(cardValidator([])) #Make your own 3 length list