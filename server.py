import socket
import threading

PORT = 6050
SERVER = '192.168.1.193'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!Disconnect"

# server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server.bind(ADDR)

def handle_client(conn, addr):

    print(f"New connection : {addr}\n")

    msg_lenght = conn.recv(HEADER).decode(FORMAT)
    
    if msg_lenght:

        msg_lenght = int(msg_lenght)
        msg = conn.recv(msg_lenght).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            return False
        return msg
        



# def start():
#     server.listen()
#     print(f"Started listening on {SERVER}")
#     while 1:
#         conn,addr = server.accept()
#         thread = threading.Thread(target=handle_client, args=(conn,addr))
#         thread.start()
#         print(threading.active_count())


