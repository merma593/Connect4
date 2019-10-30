import numpy as np
import sys
import random as rand
import pygame
import math

#GLOBALS
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


def create_board():
    #Creates a 7 x 6 matrix of 0s
    board = [['0'] * 7 for row in range(6)]
    return board


def display(board):
    #Displays the board in cmd line
    for rows in board:
        print(' '.join(rows))
        

def who_goes_first(p1, p2):
    #randomly chooses player to go first
    if rand.randint(1,2) == 1:
        return p1
    else:
        return p2

def choose_column():
    #was for original cmd line game
    col = input("Choose a column from 0-6: ")
    return col


def valid_col(colnum):
    #checks if user input is valid col number

    if int(colnum) < 0 or int(colnum) > 6:
        print("Invalid column! Try again")
        return False
    else:
        return True



def update_board(board, colnum, player):

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
        print("All spaces Full in this column, Try another one!")
        colnum = choose_column()
        update_board(board, int(colnum), player)
        return board


def vertical_win(board, colnum, player):
    #checks if there is a connect 4 vertically in row
    count = 0
    if player == 1:
        piece = 'r'
    else:
        piece = 'y'
        
    if piece == 'r':   
        for rows in reversed(board):
            if rows[colnum] == piece:
                count += 1
            elif rows[colnum] == 'y':
                count = 0
    if piece == 'y':   
        for rows in reversed(board):
            if rows[colnum] == piece:
                count += 1
            elif rows[colnum] == 'r':
                count = 0
                
    if count == 4:
        return True


def horizontal_win(board, player):
    cols = len(board)
    rows = len(board[0])

    count = 0
    if player == 1:
        piece = 'r'
    else:
        piece ='y'
        
    for rows in range(cols):
        for x in range(rows):
            if board[rows][x] == piece and board[rows][x+1] == piece and board[rows][x+2] == piece and board[rows][x+3] == piece:
                return True



def diagonal_win(board, player):
    #checks all ascending and diagonal spaces for win
    boardWidth = len(board)
    boardHeight = len(board[0])

    if player == 1:
        piece = 'r'
    else:
        piece ='y'

     # check ascending diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(3, boardHeight):
            if board[x][y] == piece and board[x+1][y-1] == piece and board[x+2][y-2] == piece and board[x+3][y-3] == piece:
                return True

    # check descending diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(boardHeight - 3):
            if board[x][y] == piece and board[x+1][y+1] == piece and board[x+2][y+2] == piece and board[x+3][y+3] == piece:
                return True

    return False
            
        
    
    
                        
def win(board, colnum, player):
    #all possible winning methods
    win = False
    if vertical_win(board, colnum, player) == True:
        print("Vert win")
        win = True
    elif diagonal_win(board, player):
        print("Diag win")
        win = True        
    elif horizontal_win(board, player) == True:
        print("Hoz win")
        win = True

        
    return win


def draw_game(screen, board, SQUARESIZE):
    #draws blue outline and circles on board
    RADIUS = int(SQUARESIZE/2 - 5)
    for cols in range(7):
        for rows in range(6):
            pygame.draw.rect(screen, BLUE, (cols * SQUARESIZE, rows * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            if board[rows][cols] == '0':
                pygame.draw.circle(screen, BLACK, (int(cols * SQUARESIZE + SQUARESIZE/2),int(rows * SQUARESIZE + SQUARESIZE+SQUARESIZE/2)), RADIUS) 
            elif board[rows][cols] == 'r':
                pygame.draw.circle(screen, RED, (int(cols * SQUARESIZE + SQUARESIZE/2),int(rows * SQUARESIZE + SQUARESIZE+SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (int(cols * SQUARESIZE + SQUARESIZE/2),int(rows * SQUARESIZE + SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()

    
def main():
    gameMoves = 42 #Max amount of moves on 6 x 7 board
    board = create_board()
    display(board)
    player1 = 1
    player2 = 2
    play = who_goes_first(player1, player2)
    print("Welcome to connect 4! Player:", play, "will start.")

    pygame.init()

    SQUARESIZE = 100
    width = 7 * SQUARESIZE
    height = 7 * SQUARESIZE

    size = (width, height)

    screen = pygame.display.set_mode(size)
    draw_game(screen, board, SQUARESIZE)
    pygame.display.update()
    font = pygame.font.SysFont("monospace", 40) #font for win text
    
    
    while gameMoves >= 0:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                print("Player", play, "Turn!")
                #colnum = choose_column() for cmd line game
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE)) #finds column based on user click
                        
                if valid_col(col) == True: #valid col for cmd line game
                    print("Placing Piece!")
                    board = update_board(board, int(col), play)
                    display(board) 
                    draw_game(screen, board, SQUARESIZE)
                            
                    if win(board, int(col), play) == True:
                        #print("Game over!, player: ",play, "Wins!") cmd line game
                        if play == 1:
                            label = font.render(("Game over!, player 1 Wins!"),1, RED)
                        else:
                            label = font.render(("Game over!, player 2 Wins!"),1, YELLOW)
                        screen.blit(label, (40,10))
                        draw_game(screen, board, SQUARESIZE)
                        exit()
                    else:                
                        if play == 1:
                            play = 2
                        else:
                            play = 1                 
                    gameMoves -= 1

        
    
if __name__ == "__main__":
    main()
    
    
