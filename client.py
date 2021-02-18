import socket
import threading
from ip_info import SERVER

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
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

def read_messages():
	prev_message = None
	while True:
		message = client.recv(2048).decode(FORMAT).replace("\n", "")
		#message = client.recv(2048).decode(FORMAT)
		if message != prev_message:
			print(message, end = "\n>")
		prev_message = message		

def main():
	username = input("Input your username here: ")
	msg = None	
	thread = threading.Thread(target = read_messages) 
	thread.start()
	
	first = True
	while msg != DISCONNECT_MESSAGE:
		if first == True:
			msg = input(">")
			first = False
		else:
			msg = input("")
		if msg != DISCONNECT_MESSAGE:
			send(username+ ': ' + msg)

main()
