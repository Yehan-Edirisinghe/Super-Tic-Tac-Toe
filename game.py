import pygame
import numpy as np

white   = 255,255,255
red     = 255,  0,  0
black   =   0,  0,  0

    
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

def play(canvas):

    a,b = map_(8,8,canvas)
    draw_X(pos=(a,b),canvas=canvas)
    # draw_O(pos=(a,b),canvas=canvas)


    return True