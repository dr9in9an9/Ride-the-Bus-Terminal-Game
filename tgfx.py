class tgfx:
    
    # Finally got the constructor working--tgfx now functions as an object! 
    def __init__(self):
        self.row1 = ['╔════╗','║▒▓▒▓║','║▓▒▓▒║','║▒▓▒▓║','╚════╝','  ◢◣  ','╔════╗','║▒▓▒▓║','║▓▒▓▒║','║▒▓▒▓║','╚════╝','      ','╔════╗','║▒▓▒▓║','║▓▒▓▒║','║▒▓▒▓║','╚════╝','      ','╔════╗','║▒▓▒▓║','║▓▒▓▒║','║▒▓▒▓║','╚════╝','      ']

        self.row2 = ['╔════╗','║▒▓▒▓║','║▓▒▓▒║','║▒▓▒▓║','╚════╝','      ','╔════╗','║▒▓▒▓║','║▓▒▓▒║','║▒▓▒▓║','╚════╝','      ','╔════╗','║▒▓▒▓║','║▓▒▓▒║','║▒▓▒▓║','╚════╝','      ']

        self.row3 = ['╔════╗','║▒▓▒▓║','║▓▒▓▒║','║▒▓▒▓║','╚════╝','      ','╔════╗','║▒▓▒▓║','║▓▒▓▒║','║▒▓▒▓║','╚════╝','      ']

        self.row4 = ['╔════╗','║▒▓▒▓║','║▓▒▓▒║','║▒▓▒▓║','╚════╝','      ']

        self.opti = ['      ','  ◢◣  ']

        self.suit = ['║♣   ║','║♡   ║','║♠   ║','║♢   ║']

        self.nums = ['║ 𝐀  ║','║   1║','║ ⠁⠄ ║','║   2║','║ ⠡⠁ ║','║   3║','║ ⠅⠅ ║','║   4║','║ ⠺⠂ ║','║   5║','║ ⠇⠇ ║','║   6║','║ ⠿⠂ ║','║   7║','║ ⠯⠇ ║','║   8║','║ ⠿⠇ ║','║   9║','║ ⣻⡃ ║','║  10║','║ ♘  ║','║  11║','║ ♔  ║','║  12║','║ ♕  ║','║  13║']

        self.cursor = [1, 1]

    # DON'T WORRY ABOUT THIS... it works, thats all that matters
    def arrangeDeck(self):
        x = 0
        gameboard = ""

        while x < 24:
            gameboard += ((str(self.row1[x]).replace("'","")).replace("[","")).replace("]","")
            if 3 <= x <= 20:
                gameboard += ((str(self.row2[x-3]).replace("'","")).replace("[","")).replace("]","")
                if 6 <= x <= 17:
                    gameboard += ((str(self.row3[x-6]).replace("'","")).replace("[","")).replace("]","")
                    if 9 <= x <= 14:
                        gameboard += ((str(self.row4[x-9]).replace("'","")).replace("[","")).replace("]","")
            gameboard += "\n"
            x += 1
        
        return gameboard

    # flipCard(row: starting at 1 && left-to-right, card to update: starting at 1 && top-to-bottom, data of drawn card)
    def flipCard(self, r, c, d):
        updatePos = 6 * (c - 1) + 1 # starting updatePos
        card = ['║▒▓▒▓║','║▓▒▓▒║','║▒▓▒▓║'] #set d variable to 'reset' to reset card

        if d != 'reset':
            if d[1] == "Clubs":
                card[0] = self.suit[0]
            if d[1] == "Hearts":
                card[0] = self.suit[1]
            if d[1] == "Spades":
                card[0] = self.suit[2]
            if d[1] == "Diamonds":
                card[0] = self.suit[3]

            card[1] = self.nums[2 * (d[2] - 1)]
            card[2] = self.nums[2 * (d[2] - 1) + 1]

        if r == 1:
            self.row1[updatePos] = card[0]
            self.row1[updatePos + 1] = card[1]
            self.row1[updatePos + 2] = card[2]
        if r == 2: 
            self.row2[updatePos] = card[0]
            self.row2[updatePos + 1] = card[1]
            self.row2[updatePos + 2] = card[2]
        if r == 3:
            self.row3[updatePos] = card[0]
            self.row3[updatePos + 1] = card[1]
            self.row3[updatePos + 2] = card[2]
        if r == 4:
            self.row4[updatePos] = card[0]
            self.row4[updatePos + 1] = card[1]
            self.row4[updatePos + 2] = card[2]

    # moveCursor(row of card to point at, card to point at, row of card previously pointed at, card previously pointed at)
    def moveCursor(self, r, c, pr, pc): 
        prevPos = 6 * pc - 1 

        if pr == 1:
            self.row1[prevPos] = self.opti[0]
        if pr == 2: 
            self.row2[prevPos] = self.opti[0]
        if pr == 3:
            self.row3[prevPos] = self.opti[0]
        if pr == 4:
            self.row4[prevPos] = self.opti[0]

        updatePos = 6 * c - 1

        if r == 1:
            self.row1[updatePos] = self.opti[1]
        if r == 2: 
            self.row2[updatePos] = self.opti[1]
        if r == 3:
            self.row3[updatePos] = self.opti[1]
        if r == 4:
            self.row4[updatePos] = self.opti[1]


## bug checkerrr
'''
import time
import deck

graphics = tgfx()
print(graphics.row1)

print(graphics.arrangeDeck())

dih = deck.gen()
deck.shuffle(dih)

time.sleep(1)
graphics.flipCard(1, 1, deck.drawCard(dih, 0))
print(graphics.arrangeDeck())

time.sleep(1)
graphics.flipCard(1, 2, deck.drawCard(dih, 0))
graphics.moveCursor(1, 2, 1, 1)
print(graphics.arrangeDeck())

time.sleep(1)
graphics.flipCard(1, 3, deck.drawCard(dih, 0))
graphics.moveCursor(1, 3, 1, 2)
print(graphics.arrangeDeck())

time.sleep(1)
graphics.flipCard(1, 4, deck.drawCard(dih, 0))
graphics.moveCursor(1, 4, 1, 3)
print(graphics.arrangeDeck())
#'''
