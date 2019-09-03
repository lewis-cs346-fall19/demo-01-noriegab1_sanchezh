import socket

# Creating Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding To Port
addr = ("0.0.0.0", 12458)
sock.bind(addr)

# Listening and Accepting
sock.listen(5)

while(True):
	(connectedSock, clientAddress) = sock.accept()

# Receiving Data

try:
	msg = sock.recv(1024).decode()
	print(len(msg))
except ConnectionAbortedError:
	sock.close()

sock.sendall(msg.encode())