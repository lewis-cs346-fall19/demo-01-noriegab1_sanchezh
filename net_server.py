import socket

# Creating Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding To Port
addr = ("localhost", 12458)
sock.bind(addr)

# Listening and Accepting
sock.listen(5)

while(True):
	(connectedSock, clientAddress) = sock.accept()
	# Receiving Data
	try:
		msg = connectedSock.recv(1024).decode()

		print(msg)

		reply = msg + ' - received'

		connectedSock.sendall(reply.encode())
	except ConnectionAbortedError:
		sock.close()
sock.close()