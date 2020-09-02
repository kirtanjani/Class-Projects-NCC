# Alena Troia and Stephanie Kostrzeski and Kirtan Jani
# HW 3: Connect Four
# Due 10/18/19

# Import needed functions
import random


#----------------------function definition --------------------------

# Create board in matrix 
# 7 colimns by 6 rows
def displayBoard(board):

    print ("   0   1   2   3   4   5   6")
    print ("0: " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " | " + board[0][3] + " | " + board[0][4] + " | " + board[0][5] + " | " + board[0][6] + " | ")
    print ("  ---+---+---+---+---+---+---")
    print ("1: " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " | " + board[1][3] + " | " + board[1][4] + " | " + board[1][5] + " | " + board [1][6] + " | ")
    print ("  ---+---+---+---+---+---+---+")
    print ("2: " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " | " + board[2][3] + " | " + board [2][4] + " | " + board [2][5] + " | " + board [2][6] + " | ")
    print ("  ---+---+---+---+---+---+---+")
    print ("3: " + board[3][0] + " | " + board[3][1] + " | " + board[3][2] + " | " + board[3][3] + " | " + board [3][4] + " | " + board [3][5] + " | " + board [3][6] + " | ")
    print ("  ---+---+---+---+---+---+---+")
    print ("4: " + board[4][0] + " | " + board[4][1] + " | " + board[4][2] + " | " + board[4][3] + " | " + board [4][4] + " | " + board [4][5] + " | " + board [4][6] + " | ")
    print ("  ---+---+---+---+---+---+---+")
    print ("5: " + board[5][0] + " | " + board[5][1] + " | " + board[5][2] + " | " + board[5][3] + " | " + board [5][4] + " | " + board [5][5] + " | " + board [5][6] + " | ")
    print

# Check for wins
def winner(board):
    
    # Check rows for winner
    for row in range(6):
        for col in range(3):
            if (board[row][col] == board[row][col + 1] == board[row][col + 2] ==\
                board[row][col + 3]) and (board[row][col] != " "):
                return board[row][col]

    # Check columns for winner
    for col in range(7):
        for row in range(3):
            if (board[row][col] == board[row + 1][col] == board[row + 2][col] ==\
                board[row + 3][col]) and (board[row][col] != " "):
                return board[row][col]

    # Check diagonal (negative slope) for winner

    for row in range(3):
        for col in range(4):
            if (board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] ==\
                board[row + 3][col + 3]) and (board[row][col] != " "):
                return board[row][col]


    # Check diagonal (positive slope) for winner

    for row in range(5, 2, -1):
        for col in range(3):
            if (board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] ==\
                board[row - 3][col + 3]) and (board[row][col] != " "):
                return board[row][col]

    # No winner: return the string with space
    return " "

# Check to see if spot is empty
def validity(board,col):
    found_space = False  # Initially no space found
    for r in range(5,-1,-1):
      if board[r][col]== ' ' :
          found_space = True
    return found_space

# Checks for next empty row for game piece
def next_open_row(board,col):
  for r in range(5,-1,-1):
      if board[r][col]== ' ' :
          return r
      
# Drops game piece down to next empty row           
def slide_token(board,row,col,piece):
    board[row][col] = piece

def smartmove(board):
    for row in range(6):
        for col in range(3):
            if (board[row][col] == board[row][col + 1] == board[row][col + 2]) and (board[row][col] != " "):
                return [col + 3]

# ------------- main program -------------------------------------

# Print game board
gameBoard = [ [ " ", " ", " ", " ", " ", " "," "], [ " ", " ", " ", " ", " "," ", " "], [ " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " "] ]
displayBoard(gameBoard)
turns = 0

# Create game loop
while(True):    

    # Get user input, make sure it's valid, and determine row 
    while (True):
        col = int(input("X: Enter column number 0-6:"))                
        if validity(gameBoard,col):
            row = next_open_row(gameBoard,col)
            slide_token(gameBoard,row,col,'X')
    
            # Display user's choice on board                  
            gameBoard[row][col] = 'X'
            break
        
    turns = turns + 1
    displayBoard(gameBoard)

    # Check for a user win
    if (winner(gameBoard) != " "):
        print ("User wins!")
        break

    # Check for a tie
    if (turns == 42):
        print ("Tie!")
        break
    
    # Computer's turn   
    while (True):
        col = random.randint(0,5)   
        if validity(gameBoard,col):
            row = next_open_row(gameBoard,col)
            slide_token(gameBoard,row,col,'O')
        
            # Display user's choice on board                  
            gameBoard[row][col] = 'O'
            break     
                    
    turns = turns + 1
    displayBoard(gameBoard)
    
    # Check for a computer win
    if (winner(gameBoard) != " "):
        print ("Computer wins!")
        break

    




    


