import socket
import threading
from ip_info import SERVER

#Global variables
HEADER = 64
PORT = 5050
#get your local ipv4 address
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!D"

#Set up server at IP address
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)

#What to do when a new client connects
def handle_client(conn, addr, my_clients):
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            contents = msg.split(": ")[1]
            #what to do on disconnect
            if contents == DISCONNECT_MESSAGE:
                connected = False
                my_clients.remove(conn)
            print(msg.replace("\n", ""))
            send_all(msg.encode(FORMAT), my_clients, conn)

#send a message to all connected clients
def send_all(message, my_clients, conn):
    print(len(my_clients))
    for client in my_clients:
        if conn != client:
            #message = '\n' + message.decode(FORMAT)
            #message = message.encode(FORMAT)
            client.send(message)
        else:
            #message = (message.decode(FORMAT).replace("\n","").encode(FORMAT))
            client.send(message)

#start server and thread the different users
def start():
    my_clients = []
    server.listen()
    print(f"[LISTENING] Chatroom is online at {SERVER}.")
    while True:
        #add their conn to a list of all connections
        conn, addr = server.accept()
        my_clients.append(conn)
        #start a thread of handleclient() with each new user
        thread = threading.Thread(target=handle_client, args=(conn, addr, my_clients))
        thread.start()


print("[STARTING] Server is starting...")
start()

