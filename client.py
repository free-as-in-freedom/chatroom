import socket
import threading

#global variables
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
#get user input for IP address or URL
SERVER = input("Enter server URL/IP ADDRESS: ")
ADDR = (SERVER, PORT)

def send(msg):
	msg = "\n" + msg
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length))
	client.send(send_length)
	client.send(message)

def read_messages(username):
	prev_message = None
	while True:
		message = client.recv(2048).decode(FORMAT).replace("\n", "")
		other_user = message.split(":")[0]
		if message != prev_message:
			if ": !DISCONNECT" in message:
				if other_user == username:
					print(f"You has disconnected.")
					return	
				else:
					print(f"\n{other_user} has disconnected.", end = "\n>")
			elif message.split(":")[0] == username:
				print(message, end = "\n>")
			else:
				print(f"\n{message}", end = "\n>")
		prev_message = message		

def main():
	username = input("Input your username here: ")
	print(f"Welcome to the chatroom, {username}!")	
	msg = None	
	#create thread for reading messages so everything can be done in real time
	thread = threading.Thread(target = read_messages, args = (username, ))
	thread.start()
	
	first = True
	
	#user input and sending messages
	while True:
		#if else is for display purposes
		if first == True:
			msg = input(">")
			first = False
		else:
			msg = input("")
		send(username+ ': ' + msg)


#join server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"Connecting to {SERVER}...")
client.connect(ADDR)
print(f"Connection to {SERVER} successful.")

main()

