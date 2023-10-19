import pygame
from game import play,Player,Board
from draw import drawBoard

white   = 255,255,255
red     = 255,  0,  0
black   =   0,  0,  0

def init_window(size):

    pygame.init()
    pygame.display.set_caption("Tic Tac Toe by edi")
    canvas = pygame.display.set_mode((size[0]+1,size[1]+1))
    return canvas


def main():

    # One time commands:

    size = 600,600
    canvas = init_window(size)

    board = Board(size)
    
    p1 = Player("Mario",1)
    p2 = Player("Pierina",2)


    # Loop commands:
    run = True
    turn = 0
    while run:

        canvas.fill(black)
        drawBoard(board,canvas)
        pygame.display.flip()

        
        play(canvas,board,turn)

        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                run = False

        turn +=1
    pygame.quit()


if __name__ == '__main__':
    main()