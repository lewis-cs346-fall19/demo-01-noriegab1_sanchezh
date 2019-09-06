import socket 

# Creating Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ("localhost",12458)
sock.connect(addr)

# print("got here")

file = open('github_lab.txt')
for line in file:
	sock.sendall(line.encode())


msg = sock.recv(1024).decode()
print(msg)


sock.close()