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

    clock = pygame.time.Clock()

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

        

        for event in pygame.event.get():
            
            if play(canvas.get_size(),board,turn):
                print(turn)
                turn+=1
            
            

            
            if event.type is pygame.QUIT:
                run = False
        clock.tick(60)

        
    pygame.quit()


if __name__ == '__main__':
    main()