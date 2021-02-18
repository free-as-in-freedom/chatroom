import socket
import ip_info

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = '45.77.215.116'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting to server...")
client.connect(ADDR)
print("Connection successful.")

def send(msg):
	msg = "\n" + msg
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length))
	client.send(send_length)
	client.send(message)

username = input("Input your username here: ")

msg = None
while msg != DISCONNECT_MESSAGE:
	msg = input(">")
	if msg != DISCONNECT_MESSAGE:
		send(username+ ': ' + msg)
		message = client.recv(2048).decode(FORMAT).replace("\n", "")
		print(message)
