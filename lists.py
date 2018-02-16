#LISTS (31PTS TOTAL)
#In these exercises you should should use functions as needed.  All functions should have comments to describe their purpose.

import random

# PROBLEM 1 (Using List Comprehensions - 6pts)
# Use the list comprehension method to do the following:
# a) Make a list of numbers from 1 to 100
my_list = [x for x in range(1, 101)]
print(my_list)

# b) Make a list of even numbers from 20 to 40
my_list = [x for x in range(20, 41) if x % 2 == 0]
print(my_list)

# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)
my_list = [x ** 2 for x in range(1, 101)]
print(my_list)

#PROBLEM 2 (8-ball - 5pts)
# A magic 8-ball, when asked a question, provides a random answer from a list.
# The code below contains a list of possible answers. Create a magic 8-ball program that
# prints a random answer.

answer_list = [ "It is certain", "It is decidedly so", "Without a \
doubt", "Yes, definitely", "You may rely on it", "As I see it, \
yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
"Reply hazy try again", "Ask again later", "Better not tell you \
now", "Cannot predict now", "Concentrate and ask again", "Don ' t \
count on it", "My reply is no", "My sources say no", "Outlook \
not so good", "Very doubtful" ]

'''
question = input("Ask a yes or no question:\n")
print(random.choice(answer_list))
'''

# PROBLEM 3 (Shuffle - 5pts)
# A playing card consists of a suit (Heart, Diamond, Club, Spade) and a value (2,3,4,5,6,7,8,9,10,J,Q,K,A).
# Create a list of all possible playing cards, which is a deck.
# Then create a function that shuffles the deck, producing a random order.
deck = []
suits = ["S", "H", "C", "D"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
for number in numbers:
    for suit in suits:
        deck.append(number + suit)
print(deck)

shuffled_deck = []
for x in range(len(deck)):
    shuffled_deck.append(deck.pop(random.randrange(len(deck))))
print(shuffled_deck)


# PROBLEM 4 (Tic-Tac-Toe - 15pts)
# Write a Tic-Tac-Toe program that allows two people to play the game against each other.
# In turn, ask each player which row and column they want to play.
# Make sure that the program checks if that row/column combination is empty.
# When a player has won, end the game.
# When the whole board is full and there is no winner, announce a draw.
# This is a fairly long program to write (60 lines or so).
# It will definitely help to use some functions.
# I recommend that you create a function display_board() that gets the board
# as parameter and displays it,
# a function get_row_column() that asks for a row or a column (depending on a parameter)
# and checks whether the user entered a legal value,
# and a function winner() that gets the board as argument and checks if there is a winner.
# Keep track of who the current player is using a global variable player that you can
# pass to a function as an argument if the function needs it.
# I also use a function opponent(), that takes the player as argument and returns
# the opponent. I use that to switch players after each move.
print

def draw_board(board_input):
    print(" - - - ")
    print("|" + board_input[0][0], board_input[0][1], board_input[0][2] + "|")
    print("|" + board_input[1][0], board_input[1][1], board_input[1][2] + "|")
    print("|" + board_input[2][0], board_input[2][1], board_input[2][2] + "|")
    print(" - - - ")

def check_full(board_input):
    full = 0
    for x in range(3):
        for y in range(3):
            if board_input[x][y] == " ":
                return False
    return True

def check_win(board_input,player):
    for x in range(3):
        if board_input[x][0] == board_input[x][1] == board_input[x][2] == player:
            return True
    for x in range(3):
        if board_input[0][x] == board_input[1][x] == board_input[2][x] == player:
            return True
    if board_input[0][0] == board_input[1][1] == board_input[2][2] == player:
        return True
    if board_input[0][2] == board_input[1][1] == board_input[2][0] == player:
        return True



done = False
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
draw_board(board)
player = "X"
while not done:
    row = int(input("Player " + player + " Enter row (1,2,3): "))
    col = int(input("Player " + player + " Enter col (1,2,3): "))
    if board[row-1][col-1] == " ":
        board[row-1][col-1] = player
    else:
        print("That space is taken")
        continue
    draw_board(board)
    if check_win(board,player):
        print(player, "wins!!")
        break
    if check_full(board):
        print("Draw!")
        break
    if player == "X":
        player = "O"
    else:
        player = "X"

# The main program will be something along the lines of (in pseudo-code):
# display board
# while True:
#   ask for row
#   ask for column
#       if row/column already occupied:
#           display error
#   place player marker in row/col
#   display board
#   check for winner:
#       announce winner
#       break
#   check board full:
#       announce draw
#       break
#   switch player

# CHALLENGE PROBLEM 5 (MAY DO AS SUBSTITUTE FOR PROBLEM 4, NO ADDITIONAL CREDIT)
# Create a program that is a simplified version of the game “Battleship.”
# The computer creates (in memory) a grid that is 4 cells wide and 3 cells high.
# The rows of the grid are numbered 1 to 3, and the columns of the grid are labeled A to D.
# The computer hides a battleship in three random cells in the grid.
# Each battleship occupies exactly one cell.
# Battleships are not allowed to touch each other horizontally or vertically.
# Make sure that the program places the battleships randomly, so not pre-configured.
# The computer asks the player to “shoot” at cells of the grid.
# The player does so by entering the column letter and row number of the cell
# which she wants to shoot at (e.g., "D3").
# If the cell which the player shoots at contains nothing, the computer responds with “Miss!”
#  If the cell contains a battleship, the computer responds with “You sunk my battleship!”
# and removes the battleship from the cell (i.e., a second shot at the same cell is a miss).
# As soon as the player hits the last battleship, the computer responds with displaying
# how many shots the player needed to shoot down all three battleships, and the program ends.
# To help with debugging the game, at the start the computer should display the grid with
# O's marking empty cells and X's marking cells with battleships.
# Hint: If you have troubles with this exercise, start by using a board which has the
# battleships already placed.
# Once the rest of the code works, add a function that places the battleships at random,
# at first without checking if they are touching one another.
# Once that works, add code that disallows battleships touching each other.
