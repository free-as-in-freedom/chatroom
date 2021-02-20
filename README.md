# chatroom

This is a chatroom project that lets clients connect to a server and communicate with eachother through the server. To start the client server, make sure to create a ip_info.py file in the directory with the line  `SERVER = "IP ADDRESS OR URL HERE"` inside fo it. 

To run the server, run `python3 server.py` on the server side, and run `python3 client.py` on the client side.


[Software Demo Video](https://youtu.be/vdlf2p6fi1g)

# Network Communication

This program is a client/server that uses TCP and runs on any port that the server specifies. I decided to use port 5050, and I think that will work well ni most use cases. The messages are encoded and decoded using UTF-8.

# Development Environment

This software was creatied using Python 3 and Vim with the [socket](https://docs.python.org/3/library/socket.html) and [threading](https://docs.python.org/3/library/threading.html) libraries. These libraries come preinstalled with Python 3.

I am running a Debian server VPS through [Vultr](https://www.vultr.com/?ref=8802157). 


# Useful Websites

{Make a list of websites that you found helpful in this project}
* [socket Official Documentation](https://docs.python.org/3/library/socket.html)
* [Python Socket Programming Tutorial - Tech With Tim](https://www.youtube.com/watch?v=3QiPPX-KeSc)

# Future Work

* User authentication system with secure username/passwords
* Message encryption
* Print a userlist to the client
