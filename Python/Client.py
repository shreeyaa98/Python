import socket
port=5000
host='127.0.0.1'

s=socket.socket()
s.connect((host,port))
message=input("Client:")
while message!='Quit':
	s.send(message.encode())
	data=s.recv(1024).decode()
	print("received"+str(data))
	message=input("Client:")
s.close()
