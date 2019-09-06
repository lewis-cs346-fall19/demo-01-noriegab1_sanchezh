import socket 

# Creating Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ("localhost",12458)
sock.connect(addr)

# print("got here")

msg1 = "Hey Ben"
msg2 = "Hi Hecty"

sock.sendall(msg1.encode())



try:
	msg = sock.recv(1024).decode()
	print(msg)
	sock.sendall(msg2.encode())

except ConnectionAbortedError:
	sock.close()

sock.close()