import socket 

# Creating Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ("localhost",12458)
sock.connect(addr)

# print("got here")


file = open('github_lab.txt')



def send_message(line):
	sock.send(line.encode())


for line in file:
	try:
		send_message(line)

		msg = sock.recv(1024).decode()
		print(msg)

	except ConnectionAbortedError:
		sock.close()

sock.close()