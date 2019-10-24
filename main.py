import numpy as np
import sys
import random as rand

def create_board():
    #Creates a 7 x 6 matrix of 0s
    board = [['0'] * 7 for row in range(6)]
    return board


def display(board):
    for rows in board:
        print(' '.join(rows))
        

def who_goes_first(p1, p2):
    #randomly chooses player to go first
    if rand.randint(1,2) == 1:
        return p1
    else:
        return p2

def choose_column():
    col = input("Choose a column from 0-6: ")
    return col


def valid_col(colnum):
    #checks if user input is valid col number
    valid = False
    while int(colnum) < 0 or int(colnum) > 6:
        print("try again, invalid input")
        colnum = choose_column()
    else:
        print(colnum)
        valid = True
    return valid


def update_board(board, colnum, player):
    piece = ""
    if player == 1:
        piece = 'r'
    else:
        piece = 'y'
    count = 6
    num = 6
    while count >= 0:
        for rows in reversed(board):
            if rows[colnum] == '0':
                rows[colnum] = piece
                return board
            else:
                count -= 1
                num -= 1
    else:
        print("All spaces Full, Game over!")

           
def main():
    gameMoves = 42
    board = create_board()
    display(board)
    player1 = 1
    player2 = 2
    play = who_goes_first(player1, player2)
    print("Welcome to connect 4! Player:", play, "will start.")
    while gameMoves >= 0:
        print("Player", play, "Turn!")
        colnum = choose_column()
        if valid_col(colnum) == True:
            print("Placing Piece!")
            board = update_board(board, int(colnum), play)
            display(board)
            if play == 1:
                play = 2
            else:
                play = 1
    gameMoves -= 1
        
    
main()
    
    
