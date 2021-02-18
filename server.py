import socket
import threading
import keyboard

HEADER = 64
PORT = 5050
#get your local ipv4 address
#SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "INSERT IP HERE"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)
        
def handle_client(conn, addr):
    #print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            
            print(conn, addr, "\n")
            #print(msg, end="")
            conn.send(msg.encode(FORMAT))
            
def start():
    server.listen()
    print(f"[LISTENING] Chatroom is online.")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        #print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] Server is starting...")
start()

