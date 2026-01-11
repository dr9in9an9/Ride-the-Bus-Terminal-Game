## Clubs, Hearts, Spades, Diamonds - 13 cards each.
import random

n = 52 ## number of cards.
posNum = []
for i in range(1, n + 1): ## Sigma notation which counts by intervals of 1, starting @ 1, to n.
    posNum += [i] ## Adds every num (1-n) to empty list.

deckset = []  ## holds avaliable cards. 
m = 13 ## number of cards per suit.
while posNum != []:
    for i in range(1, m + 1):
        deckset += ["c"+str(i)]
        del posNum[0]
    for i in range(1, m + 1):
        deckset += ["h"+str(i)]
        del posNum[0]
    for i in range(1, m + 1):
        deckset += ["s"+str(i)]
        del posNum[0]
    for i in range(1, m + 1):
        deckset += ["d"+str(i)]
        del posNum[0]



o = 0
def shuffle():
    shuffledDeckset = []
    
    for o in range(0, len(deckset), 1):
        shuffledDeckset.append(draw_Card(random.randrange(0, len(deckset), 1)))

    
    for o in range(0, len(shuffledDeckset), 1):
        deckset.append(shuffledDeckset[o])
        



def draw_Card(pos): ##  accessor method.
    card = str(deckset[pos]) ## creates string obj from list element.
    cardInfo = []
    if card[0] == 'c': 
        cardInfo += ["Black"]
        cardInfo += ["Clubs"]
    elif card[0] == 'h':
        cardInfo += ["Red"]
        cardInfo += ['Hearts']
    elif card[0] == 's':
        cardInfo += ["Black"]
        cardInfo += ['Spades']
    else:
        cardInfo += ["Red"]
        cardInfo += ['Diamonds']

    cardInfo += card[1:] ##

    del deckset[pos]
    return cardInfo


## bug checkerrr
#'''


x = 17
#print(deckset[x])
#print(draw_Card(x))
print(deckset)
shuffle()
print("\n")
print(deckset)
#'''
