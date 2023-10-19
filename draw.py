import pygame

white   = 255,255,255
red     = 255,  0,  0
black   =   0,  0,  0

def draw_X(pos,canvas):

    pos = map_(pos[0],pos[1],canvas)
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
    pos = map_(pos[0],pos[1],canvas)
    r = canvas.get_width()/20
    pygame.draw.circle(canvas,white,pos,r,1)

def map_(x,y,canvas):
    '''change coordinates from 1-8 numbers to pixel coords'''
    x_size,y_size = canvas.get_size()
    a = (x_size/9 )*x+ x_size/18
    b = (y_size/9 )*y+ y_size/18
    return a,b

def drawGrid(size,canvas):
    '''draws the lines of the grid'''
    
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

def drawBoard(board,canvas):
    '''draws O and X in the occupied places'''

    drawGrid(board.size,canvas)
    

    for i in range(9):
        for j in range(9):
            
            if board.grid[i,j] == 1:
                draw_X((i,j),canvas)

            elif board.grid[i,j] == 2:
                draw_O((i,j),canvas)