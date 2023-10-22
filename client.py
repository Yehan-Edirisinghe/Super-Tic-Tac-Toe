import socket


PORT = 6050
SERVER = '127.0.1.1'
ADDR = (SERVER,PORT)

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!Disconnect"




def send(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b' ' * (HEADER-len(send_lenght))
    client.send(send_lenght)
    client.send(message)


if __name__=='__main__':
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)

    send("hello")