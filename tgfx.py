import time
import deck

row1 = ['╔════╗','║▒▓▒▓║','║▓▒▓▒║','║▒▓▒▓║','╚════╝','  ◢◣  ','╔════╗','║▒▓▒▓║','║▓▒▓▒║','║▒▓▒▓║','╚════╝','      ','╔════╗','║▒▓▒▓║','║▓▒▓▒║','║▒▓▒▓║','╚════╝','      ','╔════╗','║▒▓▒▓║','║▓▒▓▒║','║▒▓▒▓║','╚════╝','      ']

row2 = ['╔════╗','║▒▓▒▓║','║▓▒▓▒║','║▒▓▒▓║','╚════╝','      ','╔════╗','║▒▓▒▓║','║▓▒▓▒║','║▒▓▒▓║','╚════╝','      ','╔════╗','║▒▓▒▓║','║▓▒▓▒║','║▒▓▒▓║','╚════╝','      ']

row3 = ['╔════╗','║▒▓▒▓║','║▓▒▓▒║','║▒▓▒▓║','╚════╝','      ','╔════╗','║▒▓▒▓║','║▓▒▓▒║','║▒▓▒▓║','╚════╝','      ']

row4 = ['╔════╗','║▒▓▒▓║','║▓▒▓▒║','║▒▓▒▓║','╚════╝','      ']

opti = ['      ','  ◢◣  ']

suit = ['║♣   ║','║♡   ║','║♠   ║','║♢   ║']

nums = ['║ 𝐀  ║','║   1║','║ ⠁⠄ ║','║   2║','║ ⠡⠁ ║','║   3║','║ ⠅⠅ ║','║   4║','║ ⠺⠂ ║','║   5║','║ ⠇⠇ ║','║   6║','║ ⠿⠂ ║','║   7║','║ ⠯⠇ ║','║   8║','║ ⠿⠇ ║','║   9║','║ ⣻⡃ ║','║  10║','║ ♘  ║','║  11║','║ ♔  ║','║  12║','║ ♕  ║','║  13║']

cursor = [1, 1]

def arrangeDeck():
    x = 0
    gameboard = ""
    while x < 24:
        gameboard += ((str(row1[x]).replace("'","")).replace("[","")).replace("]","")
        if 3 <= x <= 20:
            gameboard += ((str(row2[x-3]).replace("'","")).replace("[","")).replace("]","")
            if 6 <= x <= 17:
                gameboard += ((str(row3[x-6]).replace("'","")).replace("[","")).replace("]","")
                if 9 <= x <= 14:
                    gameboard += ((str(row4[x-9]).replace("'","")).replace("[","")).replace("]","")
        gameboard += "\n"
        x += 1
    return gameboard

def flipCard(r, c, d): #row (starting at 1, left-to-right), card to update (starting at 1, top-to-bottom), data of drawn card
    updatePos = 6 * (c - 1) + 1 # starting updatePos
    card = ['║▒▓▒▓║','║▓▒▓▒║','║▒▓▒▓║'] #set d variable to 'reset' to reset card

    if d != 'reset':
        if d[1] == "Clubs":
            card[0] = suit[0]
        if d[1] == "Hearts":
            card[0] = suit[1]
        if d[1] == "Spades":
            card[0] = suit[2]
        if d[1] == "Diamonds":
            card[0] = suit[3]

        card[1] = nums[2 * (d[2] - 1) - 1]
        card[2] = nums[2 * (d[2] - 1)]

    if r == 1:
        global row1
        row1[updatePos] = card[0]
        row1[updatePos + 1] = card[1]
        row1[updatePos + 2] = card[2]
    if r == 2: 
        global row2
        row2[updatePos] = card[0]
        row2[updatePos + 1] = card[1]
        row2[updatePos + 2] = card[2]
    if r == 3:
        global row3
        row3[updatePos] = card[0]
        row3[updatePos + 1] = card[1]
        row3[updatePos + 2] = card[2]
    if r == 4:
        global row4
        row4[updatePos] = card[0]
        row4[updatePos + 1] = card[1]
        row4[updatePos + 2] = card[2]


# def updateCursor(r, c):

## bug checkerrr
#'''
print(arrangeDeck())

dih = deck.gen()
deck.shuffle(dih)

time.sleep(1)
flipCard(1, 1, deck.drawCard(dih, 0))
print(arrangeDeck())

time.sleep(1)
flipCard(1, 2, deck.drawCard(dih, 0))
print(arrangeDeck())

time.sleep(1)
flipCard(1, 3, deck.drawCard(dih, 0))
print(arrangeDeck())

time.sleep(1)
flipCard(1, 4, deck.drawCard(dih, 0))
print(arrangeDeck())
#'''
