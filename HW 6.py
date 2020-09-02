# Kirtan Jani
# HW 6: Soduku
# Due 12/4/19 at 8am

#--------------Imports------------------
import random
import sys, os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

#--------------  Class Definitions ----------------------------

class Sudoku:
    def __init__(self, fileName=None):
        self.origBoard = [None] * 9  # Used to mark original puzzle state
        self.board = [None] * 9      # Used to mark user-entered numbers
        self.combo = [None] * 9      # Used for the combination board (check and save)
        for i in range(9):
            self.board[i] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]
            self.origBoard[i] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]
            self.combo[i] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]
            
        if (fileName==None):  # default puzzle
            self.default()
        else:                 # create puzzle
            self.readFile(fileName)
    
    def readFile(self, fn):
        
        #fileformat
        #9 lines of original puzzle state
        #9 lines of user entered values
        #Use 0 for empty space
        #Example (refer to the puzzle in the default function):
        #019374652
        #576182943
        #342596718
        #921753864
        #638419527
        #457628139
        #185237496
        #763941285
        #294865370
        #000000000
        #000000000
        #000000000
        #000000000
        #000000000
        #000000000
        #000000000
        #000000000
        #000000000
        
        #setup file to open
        file = open(os.path.join(__location__,fn), 'r')
        
        #read data as an array of strings
        data = file.readlines()
        #treat the array of strings as a matrix of characters
        
        #First, process the portion that belongs to the original board
        for i in range(9):
            for j in range(9):
                if (data[i][j] != '0'):
                    self.origBoard[i][j] = data[i][j]
                    
                    
        #Then, process the user entered values
        for i in range(9,18): #row index 9~17
            for j in range(9):
                if (data[i][j] != '0'):
                    self.board[i-9][j] = data[i][j]
        
        #close the file
        file.close()
        
    def default(self):
        #user did not provide a puzzle so we will provide one
        self.origBoard[0]=' 19374652'
        self.origBoard[1]='576182943'
        self.origBoard[2]='342596718'
        self.origBoard[3]='921753864'
        self.origBoard[4]='638419527'
        self.origBoard[5]='457628139'
        self.origBoard[6]='185237496'
        self.origBoard[7]='763941285'
        self.origBoard[8]='29486537 '

                    
    def display(self):
        #combine original board and current board
        db = [None] * 9
        for i in range(9):
            db[i] = [None] * 9
            for j in range(9):
                if (self.origBoard[i][j] == ' '):
                    db[i][j] = ' ' + self.board[i][j]
                else:
                    db[i][j] = '*' + self.origBoard[i][j]
        #format and print
        print("   0  1  2  3  4  5  6  7  8")
        print(" \u2554\u2550\u2550\u2564\u2550\u2550\u2564\u2550\u2550\u2566\u2550\u2550\u2564\u2550\u2550\u2564\u2550\u2550\u2566\u2550\u2550\u2564\u2550\u2550\u2564\u2550\u2550\u2557")
        i=0
        for m in range(0,3):
            for k in range(0,2):
                print(i,"\u2551",sep='',end='')
                for j in range(0,9,3):
                    print(db[i][j], db[i][j+1], db[i][j+2], sep='\u2502', end='\u2551')
                print("")
                print(" \u255F\u2500\u2500\u253C\u2500\u2500\u253C\u2500\u2500\u256B\u2500\u2500\u253C\u2500\u2500\u253C\u2500\u2500\u256B\u2500\u2500\u253C\u2500\u2500\u253C\u2500\u2500\u2562")
                i+=1
            print(i,"\u2551",sep='',end='')
            for j in range(0,9,3):
                print(db[i][j], db[i][j+1], db[i][j+2], sep='\u2502', end='\u2551')
            print("")
            if (m<2):
                print(" \u255F\u2550\u2550\u256A\u2550\u2550\u256A\u2550\u2550\u256C\u2550\u2550\u256A\u2550\u2550\u256A\u2550\u2550\u256C\u2550\u2550\u256A\u2550\u2550\u256A\u2550\u2550\u2562")
            else:
                print(" \u255A\u2550\u2550\u2567\u2550\u2550\u2567\u2550\u2550\u2569\u2550\u2550\u2567\u2550\u2550\u2567\u2550\u2550\u2569\u2550\u2550\u2567\u2550\u2550\u2567\u2550\u2550\u255D")
            i+=1
            
    def saveGame(self, fileName=None):
        if (fileName==None):
            print("You must provide a file name so we can save the game!")
        else:
            #combine original board and current board
            self.combo = [None] * 9
            for i in range(9):
                self.combo[i] = [None] * 9
                for j in range(9):
                    if (self.origBoard[i][j] == ' '):
                        self.combo[i][j] = self.board[i][j]
                    else:
                        self.combo[i][j] = self.origBoard[i][j]
            #open file (for writing)
            f = open(os.path.join(__location__,fileName), 'w')
            #process origBoard and board and write it to the file
            for j in range (9):
                for i in range (9):
                    if (self.combo[j][i] == " "):
                        number = str(0)
                    else:
                        number = self.combo[j][i] 
                    f.write(number)
                f.write("\n")
            for j in range (9):
                for i in range (9):
                    number = str(0)
                    f.write(number)
                f.write("\n")
            #close file
            f.close()
    
    def rowUnique(self, m, rowNum):
        #combine original board and current board
        self.combo = [None] * 9
        for i in range(9):
            self.combo[i] = [None] * 9
            for j in range(9):
                if (self.origBoard[i][j] == ' '):
                    self.combo[i][j] = self.board[i][j]
                else:
                    self.combo[i][j] = self.origBoard[i][j]
        #Use combinded board combo to check rows
        unique = True 
        for num in range (1,10):
            count = 0
            for j in range (9):
                if (self.combo[0][j] == num):
                    count += 1
            if (count != 1):
                unique == False
        return unique
                
    def colUnique(self, m, colNum):
        #combine original board and current board
        self.combo = [None] * 9
        for i in range(9):
            self.combo[i] = [None] * 9
            for j in range(9):
                if (self.origBoard[i][j] == ' '):
                    self.combo[i][j] = self.board[i][j]
                else:
                    self.combo[i][j] = self.origBoard[i][j]
        #Use combinded board combo to check rows
        unique2 = True 
        for num in range (1,10):
            count = 0
            for j in range (9):
                if (self.combo[j][0] == num):
                    count += 1
            if (count != 1):
                unique2 == False
        return unique2
    
    def squareUnique(self, m, r, c):
        #combine original board and current board
        self.combo = [None] * 9
        for i in range(9):
            self.combo[i] = [None] * 9
            for j in range(9):
                if (self.origBoard[i][j] == ' '):
                    self.combo[i][j] = self.board[i][j]
                else:
                    self.combo[i][j] = self.origBoard[i][j]
        #Use combined board to check for subsquares
        unique3 = True
        for num in range (1,10):
            count = 0
            for i in range (r,r+3):
                for j in range (c,c+3):
                    if (self.combo[i][j] == num):
                        count += 1
            if (count != 1):
                unique3 = False
        return unique3
                
                
        

#--------------  main program ----------------------------            

while (True):
    #Ask user what they would like to do
    c1 = int(input("Welcome to Sudoku. Enter 1 to load a saved file or enter 2 to load a default game:"))
    #Load their file
    if (c1 == 1):
        #Use sudoku1.txt to test
        try: 
            file = input ("Enter your file name now:")
            game = Sudoku(file)
            break
        except:
            print ("That file does not exist..")
            print ("Default puzzle loaded.")
            game = Sudoku()
            break
    #Create default game
    elif (c1 == 2):
        game = Sudoku()
        break
    else:
        print ("Invalid choice.")

#Start game loop
while (True):
    
    #Display game board
    game.display()
    
    
#User move
    while (True):
        #Request row and column
        spaceR = int(input("Enter the row:"))
        spaceC = int(input ("Enter the column:"))
        
        #Check if space is able to be changed and if valid
        if (game.origBoard[spaceR][spaceC] == ' ' and -1<spaceR<9 and -1<spaceC<9):
            break
        else:
            print ("This number is not able to be changed or doesn't exist, please choose another.")
    
    while (True):
        #Enter the number to be added
        num = input ("Enter the number you would like in this space:")
        num2 = int(num)

        #Check for valid input
        if (10>num2>0):
            break
        else:
            print ("Invalid number, please choose a number 1-9.")
    
    
        
    #Assign number to spot, show the board with move on it
    game.board[spaceR][spaceC]= num
    game.display()
    
    
    #Asks user what they would like to do, save? continue? Check for win?
    while (True):
        endGame = False
        choice = int(input("Enter 1 to coninute playing, enter 2 to check for a win, enter 3 to save and quit the game, or enter 4 to quit without saving:"))
        if (choice == 1):
            break
        elif (choice == 2):
            #Check for unique in all rows
            solved = True
            for i in range(9):
                if (game.rowUnique(game.combo, i) == False):
                    solved = False
            #Check for unique in all columns
            solved2 = True
            for i in range(9):
                if (game.rowUnique(i, game.combo) == False):
                    solved2 = False
            #Check for unique subsquares
            solved3 = True
            for i in range (0,9,3):
                if (game.squareUnique (game.combo, 0, i)):
                    solved3 = False
                if (game.squareUnique (game.combo, 3, i)):
                    solved3 == False
                if (game.squareUnique (game.combo, 6, i)):
                    solved3 = False
            if (solved == True and solved2 == True and solved3==True):
                endGame = True
                print ("Congrats! You have won the game.")
                break
            else: 
                print ("This puzzle isn't solved yet, keep trying!")
                continue
        elif (choice == 3):
            name = input("Enter the name of the file you would like to save to:")
            game.saveGame(name)
            endGame = True
            break
        elif (choice == 4):
            endGame = True
            break
        else: 
            print("Invalid choice.")
    
    if (endGame == True):
        break



























