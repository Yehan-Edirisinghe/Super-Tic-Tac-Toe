import pygame
from game import *
from draw import drawBoard
import socket
from server import handle_client
import threading

white   = 255,255,255
red     = 255,  0,  0
black   =   0,  0,  0

#SERVER-CLIENT data

PORT = 6050
SERVER = '192.168.1.193'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!Disconnect"

####################################


def init_window(size):
    '''initialise pygame with graphic settings'''

    pygame.init()
    pygame.display.set_caption("Tic Tac Toe by edi")
    canvas = pygame.display.set_mode((size[0]+1,size[1]+1))
    return canvas


def server_start():

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"Started listening on: {SERVER}\n")

    run = True
    while run:
        conn,addr = server.accept()

        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(thread.join())
        print(f"Active Clients:\t{threading.active_count()-1}\n")





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
            
            for i in range(3):
                for j in range(3):

                    if checkBigTris(board.bigTris,p1):
                        print("Player 1 won")
                        break
                    if checkBigTris(board.bigTris,p2):
                        print("Player 2 won")
                        run = False
                        

            if event.type is pygame.QUIT:
                run = False
        if moved:
            turn+=1
        clock.tick(60)

        
    pygame.quit()


if __name__ == '__main__':
    # main()
    server_start()