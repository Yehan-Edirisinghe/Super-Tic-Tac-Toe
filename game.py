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


def checkTris(x, y, grid:Board.grid ,p:Player):
            
    center = ((3*x)+1 ,(3*y)+1)

    if grid[center] == p.marker :
                        
        
        if grid[center[0]+1,center[1]]    == grid[center[0]-1,center[1]] == p.marker:
            return True
        if grid[center[0],center[1]+1]    == grid[center[0],center[1]-1] == p.marker:
            return True
        if grid[center[0]+1,center[1]+1]  == grid[center[0]-1,center[1]-1] == p.marker:
            return True
        if grid[center[0]+1,center[1]-1]  == grid[center[0]-1,center[1]+1] == p.marker:
            return True
        
    elif grid[center[0]-1,center[1]] == p.marker:

        if grid[center[0]-1,center[1]+1] == grid[center[0]-1,center[1]-1] == p.marker:
            return True
        
    elif grid[center[0]+1,center[1]] == p.marker:
        
        if grid[center[0]+1,center[1]+1] == grid[center[0]+1,center[1]-1] == p.marker:
            return True
        
    elif grid[center[0],center[1]-1] == p.marker:

        if grid[center[0]-1,center[1]-1] == grid[center[0]+1,center[1]-1] == p.marker:
            return True
        
    elif grid[center[0],center[1]+1] == p.marker:
    
        if grid[center[0]-1,center[1]+1] == grid[center[0]+1,center[1]+1] == p.marker:
            return True

def checkBigTris(grid:Board, p:Player):
    
    if checkTris(0,0,grid,p):
        return True   

def play(size,board:Board,turn):
    '''makes a move on the board, given the position and player'''

    input = click(size)

    if input != False:

        if board.grid[input[0],input[1]] !=1 and board.grid[input[0],input[1]] !=2:

            if turn%2 == 0:
                marker = 1
                board.grid[input[0],input[1]] = marker
                return True

            elif turn%2 != 0:
                marker = 2
                board.grid[input[0],input[1]] = marker
                return True

    return False