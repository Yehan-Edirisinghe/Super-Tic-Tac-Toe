import pygame
from game import play,Player,Board,drawBoard

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
    while run:

        canvas.fill(black)
        
        run = play(canvas,board,p2,(8,8))

        drawBoard(board,canvas)

        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == '__main__':
    main()