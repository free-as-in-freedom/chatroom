import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = '45.77.215.116'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting...")
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

send("Based!")
