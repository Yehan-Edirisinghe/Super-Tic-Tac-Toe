import pygame
from game import play,Player,Board,checkTris
from draw import drawBoard

white   = 255,255,255
red     = 255,  0,  0
black   =   0,  0,  0

def init_window(size):
    '''initialise pygame with graphic settings'''
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


    run = True
    turn = 0
    # Loop commands:
    while run:
        
        moved = False
        canvas.fill(black)
        drawBoard(board,canvas)
        pygame.display.flip()

        for event in pygame.event.get():
            
            if play(canvas.get_size(),board,turn):
                moved = True
            
            for i in range(3):
                for j in range(3):
                    if checkTris(i,j,board.grid,p1):
                        board.bigTris[i,j] = p1.marker
                    if checkTris(i,j,board.grid,p2):
                        board.bigTris[i,j] = p2.marker
            
            if event.type is pygame.QUIT:
                run = False
        if moved:
            turn+=1
        clock.tick(60)

        
    pygame.quit()


if __name__ == '__main__':
    main()