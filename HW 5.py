# Kirtin Jani
# HW 5: Black Jack
# Due 11/22/19 at 8am

#--------------Imports------------------
import random

#--------------  Class Definitions ----------------------------
class Card:
    def __init__ (self, s, v):
        # s is the suit: "spades" "hearts" "diamonds" "club"
        # v is value: 1(A) 2-10 11(J)  12(Q)  13(K)
        self.suit = s
        self.value = v
    
    def display(self):
        
        # Assigns correct facecard card to value for displaying (A,J,Q,K)
        if (self.value == 1):
            value = 'A'
        elif (self.value == 11):
            value = 'J'
        elif (self.value == 12):
            value = 'Q'
        elif (self.value == 13):
            value = 'K'
        # If not a facecard, value displayed is the number
        else:
            value = self.value

        # Assigns symbols to the suit for displaying
        if (self.suit == "spades"):        
             print("[\u2660", value,"]",sep='',end='')
        elif (self.suit == "hearts"):
             print("[\u2661", value,"]",sep='',end='')
        elif (self.suit == "diamonds"):
             print("[\u2662", value,"]",sep='',end='')            
        elif (self.suit == "clubs"):
             print("[\u2663", value,"]",sep='',end='')
    

class Deck:
    def __init__ (self):
        
        # Creates deck of 104
        self.cards = [None] * 104
        
        # Fills in first 52 cards with deck 1
        for i in range(0,13,1):
            self.cards[i] = Card("spades", i+1)
        
        for i in range(0,13,1):
            self.cards[i+13] = Card("hearts", i+1)
        
        for i in range(0,13,1):
            self.cards[i+26] = Card("diamonds", i+1)
        
        for i in range(0,13,1):
            self.cards[i+39] = Card("clubs", i+1)
        
        # Fills in next 52 cards with deck 2
        for i in range(0,13,1):
            self.cards[i+52] = Card("spades", i+1)
        
        for i in range(0,13,1):
            self.cards[i+65] = Card("hearts", i+1)
        
        for i in range(0,13,1):
            self.cards[i+78] = Card("diamonds", i+1)
        
        for i in range(0,13,1):
            self.cards[i+91] = Card("clubs", i+1)
        
        # Keeps track of top of deck
        self.topIdx = 0
    
    # Displays card deck
    def display(self):
        for i in range(len(self.cards)):
            self.cards[i].display()
        print("")
            
    # Shuffles deck randomly by a three line swap 200 times  
    def shuffle(self):
        for k in range(200):
            idx1 = random.randint(0,103)
            idx2 = random.randint(0,103)
               
            # Three line swap to shuffle cards
            temp = self.cards[idx1]
            self.cards[idx1] = self.cards[idx2]
            self.cards[idx2] = temp

    def dealCard(self):
        #  returns the card from the top of the deck
        #  and update the top index
                
        someCard = self.cards[ self.topIdx ]
        self.topIdx = self.topIdx + 1
        return someCard
    
    # Resets and shuffles deck
    def reset(self):
        self.shuffle()
        self.topIdx = 0
        
        
class Player:
    def __init__(self, n, m):
        # n = name of the player (string)
        # m = amount of money the player has initially
        self.name = n
        self.wallet = m
    
        self.hand = [None] * 5
        
        self.nCards = 0 # num cards you actually have at the moment        

    # Displays player info
    def show(self):
        print("----------------")
        print(self.name, " $", self.wallet, sep='')
        
        for i in range(self.nCards):
            self.hand[i].display()
        print("")
        
    def getCard(self, c):
        # c = a card object
        self.hand[ self.nCards ] = c
        self.nCards = self.nCards + 1
    
    # Calculate player's score
    def score (self):
        score = 0
        for i in range (self.nCards):
            # Make facecards equal 10 points
            if (self.hand[i].value == 11 or self.hand[i].value == 12 or self.hand[i].value == 13):
                self.hand[i].value = 10
            # Check the best value for Ace
            if (self.hand[i].value == 1):
                if (score > 10):
                    self.hand[i].value = 1
                elif (score == 10 or score < 10):
                    self.hand[i].value = 11
            score = score + self.hand[i].value 
        # Return the calculated score or -1 for bust 
        if (score == 21):
            return 21
        elif (score > 21):
            return -1
        else:
            return score        
        
#--------------  main program ----------------------------

# Create the deck, shuffle, and display it
d = Deck()
d.shuffle()
d.display()

# Gather user input
n1 = input("Enter your name:")
b1 = int(input("Enter your wallet amount:"))
p1 = Player(n1, b1)
comp = Player("Computer", 100000000000000000000)


while (True):
    # Enter bet amount and check for correct accounting
    while (True):
        bet = int(input("Enter bet amount:"))
        wallet = int(p1.wallet)
        if (bet < 1):
            print ("Invalid bet.")
        elif (bet > wallet):
            print ("Invaild bet.")
        else:
            print ("You have chosen to bet $", bet, ".")
            break

    # Reset player and computer's hands
    p1.nCards = 0
    comp.nCards = 0
    
    # Deal out 1 computer card, show
    comp.getCard( d.dealCard() )
    comp.show()
    
    # Deal out 2 computer card, don't show
    comp.getCard( d.dealCard() )
    
    # Deal out 1 user cards
    p1.getCard( d.dealCard() )
    
    # Deal out 2 user card
    p1.getCard( d.dealCard() )
    p1.show()
    
    
    # Calculate user score
    if (p1.score () == 21):
        print ("BLACKJACK, you win!")
        p1.wallet = p1.wallet + bet
    
    if (comp.score() == 21):
        print ("BLACKJACK, the computer wins!")
        p1.wallet = p1.wallet - bet
        break
    else:
        print ("Your score is", p1.score())
    
    # Ask user if they would like to hit or stay and complete action
    while (True):
        move = int(input ("Would you like to hit or stand? Enter 1 for hit and 2 for stay."))
        if(move == 1):
            print("You chose to hit.")
            p1.getCard( d.dealCard() )
            p1.show()
            # Calculate user score
            if (p1.score () == 21):
                print ("BLACKJACK, you win!")
                p1.wallet = p1.wallet + bet
                break
            elif (p1.score() == -1):
                print ("BUSTED, you lose.")
                p1.wallet = p1.wallet - bet
                break
            else:
                print ("Your score is", p1.score())
            
        elif(move == 2):
            print ("You chose to stand.")
            break
    
    if (p1.wallet == wallet):
        # Dealer (Computer's) turn
        comp.show()
        while (True):
            if (comp.score() < 17 or comp.score() < p1.score ()):
                comp.getCard (d.dealCard())
                comp.show()
                if (comp.score() == 21):
                    print ("BLACKJACK, the computer wins!")
                    p1.wallet = p1.wallet - bet
                    break
                    break
                elif (comp.score () == -1):
                    print ("BUSTED, the computer lost.")
                    p1.wallet = p1.wallet + bet
                    break
                    break
                else:
                    print ("The computer's score is", comp.score())
                    break
            else:
                break
    
    if (p1.wallet == wallet):
        # Compare user and computer scores
        if (comp.score() > p1.score() or comp.score() == p1.score()):
            print ("The computer has won!")
            p1.wallet = p1.wallet - bet
        elif (comp.score() < p1.score()):
            print ("You have won!")
            p1.wallet = p1.wallet + bet
    
    # Let user know how much money is now in their wallet
    #and ask if they would like to keep playig or if empty, exit
    print ("You now have $", p1.wallet, "in your wallet.")
    if (p1.wallet == 0):
        print ("Your wallet is empty." )
        break
    cont = int(input("Enter 1 if you would like to keep playing, enter 2 to quit."))
    if (cont == 2):
        break
    
    
    # Check to see if deck is less than 52 and if so, reset
    if (d.topIdx < 52):
        d.reset
        

