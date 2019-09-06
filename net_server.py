import socket

# Creating Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding To Port
addr = ("localhost", 12458)
sock.bind(addr)

# Listening and Accepting
sock.listen(5)



while(True):
	try:
		(connectedSock, clientAddress) = sock.accept()

		# Receiving Data
		msg = connectedSock.recv(1024).decode()

		print(msg)

		reply = msg + ' - received'

		connectedSock.send(reply.encode())
	except ConnectionAbortedError:
		sock.close()
sock.close()