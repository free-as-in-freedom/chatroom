import socket
import threading
from ip_info import SERVER

HEADER = 64
PORT = 5050
#get your local ipv4 address
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)

def handle_client(conn, addr, my_clients):
    #print(f"[NEW CONNECTION] {addr} connected.")
    my_clients.append(conn)
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                my_clients.remove(conn)
                print(conn, addr, "\n")
            print(msg.replace("\n", ""))
            send_all(msg.encode(FORMAT), my_clients)
            
def send_all(message, my_clients):
    for client in my_clients:
        client.send(message)
def start():
    my_clients = []
    server.listen()
    print(f"[LISTENING] Chatroom is online.")
    while True:
        conn, addr = server.accept()
        my_clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr, my_clients))
        thread.start()
        #print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] Server is starting...")
start()

