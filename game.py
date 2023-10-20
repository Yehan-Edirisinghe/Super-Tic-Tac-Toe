import numpy as np
from interaction import click

white   = 255,255,255
red     = 255,  0,  0
black   =   0,  0,  0


class Board:

    grid    = np.empty((9,9))

    bigTris = np.empty((3,3))

    def __init__(self,size):
        self.size = size
        for i in range(8):
            for j in range(8):
                self.grid[i,j] = 0

class Player:
    name = ""
    marker = 0
    points = 0
    def __init__(self,name,marker):
        self.same = name
        self.marker = marker

def ask_Move(string):
    a = input(string).split('.')
    return int(a[0]), int(a[1])

def checkTris(x,y,board):

    for i in range(3*x,3*x+3):
        for j in range(3*y,3*y+3):

            center = (i-3*x ,j-3*y)

            if i == 3*x+1 and j == 3*y+3 and board.grid[i,j] == 1:
                print(i,j)
                
                
            #     if board.grid[i+1,j] == board.grid[i-1,j] == 1:
            #         return True
            #     if board.grid[i,j+1] == board.grid[i,j-1] == 1:
            #         return True
            #     if board.grid[i+1,j+1] == board.grid[i-1,j-1] == 1:
            #         return True
            #     if board.grid[i+1,j-1] == board.grid[i-1,j+1] == 1:
            #         return True
                
            # elif board.grid[center[0]-1,j] == 1:

            #     if board.grid[center[0]-1,j+1] == board.grid[center[0]-1,j-1] == 1:
            #         return True
                



def checkBigTris():
    for i in range(4):
        for j in range(4):
            pass

def play(size,board:Board,turn):
    '''makes a move on the board, given the position and player'''

    input = click(size)

    if input != False:

        if turn%2 == 0:
            marker = 1
            board.grid[input[0],input[1]] = marker
            return True

        elif turn%2 != 0:
            marker = 2
            board.grid[input[0],input[1]] = marker
            return True

    return False