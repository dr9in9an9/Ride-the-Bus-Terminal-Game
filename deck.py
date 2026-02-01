## Clubs, Hearts, Spades, Diamonds - 13 cards each.
import random

# Generates a "deck", a list object, containing "cards", arrays with a singular card's info specified.
def gen():
    n = 52 # The number of cards desired. 
    # Setting n to > 52 makes more cards generate in a predictable manner. 
    # I recommend generting multiples of 52.

    posNum = []
    for i in range(1, n + 1): ## Sigma notation which counts by intervals of 1, starting @ 1, to n.
        posNum += [i] ## Adds every num (1-n) to empty list.

#### FOR FUTURE REFERENCE: THIS COULD BE CODED MUCH CLEANER.
    m = 13 # The number of cards per suit.
    deckset = []

    while posNum != []:
        for i in range(1, m + 1):
            deckset += ["c" + str(i)]
            del posNum[0]
        for i in range(1, m + 1):
            deckset += ["h" + str(i)]
            del posNum[0]
        for i in range(1, m + 1):
            deckset += ["s" + str(i)]
            del posNum[0]
        for i in range(1, m + 1):
            deckset += ["d" + str(i)]
            del posNum[0]

    deck = []

    def unpack(deckset):
        cardID = str(drawCard(deckset, 0)) # creates string obj from list element.
        card = []

        if cardID[0] == 'c': 
            card += ["Black"]
            card += ["Clubs"]
        elif cardID[0] == 'h':
            card += ["Red"]
            card += ['Hearts']
        elif cardID[0] == 's':
            card += ["Black"]
            card += ['Spades']
        else:
            card += ["Red"]
            card += ['Diamonds']
        
        if len(cardID) == 3:
            num = 10 + int(cardID[2])
            card += [num]
        else: 
            num = int(cardID[1])
            card += [num]

        return card

    while deckset != []:
        deck.append(unpack(deckset))
#### ONLY KEEPING INEFFECIENT CODE TO HIGHLIGHT MY ABILITY TO WORK WITH PREVIOUSLY COMPLETED PROJECTS.

    return deck

# Method shuffles arrays contained in deck list.
def shuffle(deck):
    o = 0
    shuffledDeckset = []
    
    for o in range(0, len(deck), 1):
        shuffledDeckset.append(drawCard(deck, random.randrange(0, len(deck), 1)))

    # adds each 'card' arr indiv, in new order, to the previous 'deck' list obj.
    for o in range(0, len(shuffledDeckset), 1):
        deck.append(shuffledDeckset[o])

# Method for quickly pulling an array containing a singular card's info from stack.
def drawCard(deckList, pos):
    card = deckList[pos]
    del deckList[pos]
    return card


## bug checkerrr
'''

dih = gen()
print(dih)
print("break! \n")
shuffle(dih)
print(dih)
print(len(dih))

#'''
