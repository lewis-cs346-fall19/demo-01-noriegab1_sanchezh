import socket

# Creating Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding To Port
addr = ("localhost", 12458)
sock.bind(addr)

# Listening and Accepting
sock.listen(5)

(connectedSock, clientAddress) = sock.accept()

while(True):
	try:
		# Receiving Data
		msg = connectedSock.recv(1024).decode()

		print(msg)

		reply = msg + ' - received'

		connectedSock.sendall(reply.encode())
	except ConnectionAbortedError:
		sock.close()
sock.close()