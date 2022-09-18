import socket
import threading
import os
import time
import errno
from socket import error as socket_error
from ip_info import SERVER

#global variables
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!D'
#get user input for IP address or URL
#SERVER = input("Enter server URL/IP ADDRESS: ")
ADDR = (SERVER, PORT)

def send(msg):
	msg = "\n" + msg
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length))
	client.send(send_length)
	client.send(message)
	if DISCONNECT_MESSAGE == msg.split(": ")[1]:
		print("You have disconnected.")
		os._exit(0)	

def read_messages(username):
	while True:
		message = client.recv(2048).decode(FORMAT).replace("\n", "")
		#message = client.recv(2048).decode(FORMAT)
		user = message.split(":")[0]
		current_time = getTime()
		if DISCONNECT_MESSAGE == message.split(": ")[1]:
			print(f"\n{current_time} {user} has disconnected.", end = "\n>")
		else:
			print(f"\n{current_time} {message}", end = "\n>")

def getTime():
	#Time variable	
	hours = str(time.localtime().tm_hour)
	mins = str(time.localtime().tm_min)
	if int(mins) < 10:
		mins = '0' + mins
	secs = str(time.localtime().tm_sec)
	if int(secs) < 10:
		secs = '0' + secs
	return '[' + hours + ':' + mins + ':' + secs + ']'

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


try:
	#join server
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print(f"Connecting to {SERVER}...")
	client.connect(ADDR)
	print(f"Connection to {SERVER} successful.")
	main()

except socket_error as serr:
	if serr.errno != errno.ECONNREFUSED:
		raise serr
	print("Could not connect to server.")



