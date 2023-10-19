import pygame
import numpy as np

white   = 255,255,255
red     = 255,  0,  0
black   =   0,  0,  0

def init_window(size):

    pygame.init()
    pygame.display.set_caption("Tic Tac Toe by edi")
    canvas = pygame.display.set_mode((size[0]+1,size[1]+1))
    return canvas

class Board:

    canvas = np.empty((9,9))

    def __init__(self):
        pass

class Player:
    name = ""
    marker = 0
    points = 0
    def __init__(self,name,marker):
        self.same = name
        self.marker = marker

def draw_board(size,canvas):

    for i in range(0,9):
        a = i*size[0]/9 , 0
        b = i*size[0]/9 , size[1]
        c = 0   , i*size[1]/9
        d = size[1] , i*size[1]/9
        pygame.draw.line(canvas,white,a,b)
        pygame.draw.line(canvas,white,c,d)

    for i in range(0,9):
        a = i*size[0]/3 , 0
        b = i*size[0]/3 , size[1]
        c = 0   , i*size[1]/3
        d = size[1] , i*size[1]/3
        pygame.draw.line(canvas,red,a,b)
        pygame.draw.line(canvas,red,c,d)
    
def draw_X(pos,canvas):
    size = canvas.get_size()
    k = size[0]/20
    l = size[1]/20
    i = pos[0]-k,pos[1]-k
    f = pos[0]+l,pos[1]+l
    
    i1 = pos[0]-k,pos[1]+k
    f1 = pos[0]+k,pos[1]-k

    pygame.draw.line(canvas,white,i,f)
    pygame.draw.line(canvas,white,i1,f1)

def draw_O(pos,canvas):
    r = canvas.get_width()/20
    pygame.draw.circle(canvas,white,pos,r,1)

def map_(x,y,canvas):
    '''change coordinates from 1-8 numbers to pixel coords'''
    x_size,y_size = canvas.get_size()
    a = (x_size/9 )*x+ x_size/18
    b = (y_size/9 )*y+ y_size/18
    return a,b

def game(canvas):

    a,b = map_(8,8,canvas)
    draw_X(pos=(a,b),canvas=canvas)
    # draw_O(pos=(a,b),canvas=canvas)



    return True


def main():

    # One time commands:

    size = 600,600
    canvas = init_window(size)

    board = Board()
    
    player1 = Player("Mario",1)
    player2 = Player("Pierina",0)


    # Loop commands:
    run = True
    while run:

        canvas.fill(black)
        draw_board(size,canvas)
        
        run = game(canvas)

        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == '__main__':
    main()