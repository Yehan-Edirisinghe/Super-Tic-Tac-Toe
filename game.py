import pygame
import numpy as np

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
            if board.grid[i,j] == 1:
                

def checkBigTris():
    for i in range(4):
        for j in range(4):
            pass

def play(canvas,board:Board,turn):
    '''makes a move on the board, given the position and player'''

    if turn%2 == 0:
        
        move = ask_Move("Player one turn:\n")
        marker = 1

    if turn%2 != 0:

        move = ask_Move("Player two turn:\n")
        marker = 2

    board.grid[move[0],move[1]] = marker
    checkTris(0,1,board)


    return True