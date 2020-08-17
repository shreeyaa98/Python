import socket
host="127.0.0.1"
port=5000
'''

s=socket.socket()
s.bind((host,port))
s.listen(1)
c,addr=s.accept()
print("Connection Established from"+str(addr))
while True:
	file=c.recv(1024)
	file=str(file.decode())
	f=open("file.txt","w")
	f.write(file)
	f.close()
	print("File copied")
c.close()
'''
s=socket.socket()
s.bind((host,port))
s.listen(1)
c,addr=s.accept()
print("Connection Established from"+str(addr))
while True:
	data=c.recv(1024).decode()
	data=str(data)
	if data=='':
		break
	print("Client"+data)
	msg=input("Server:")
	c.send(msg.encode())
s.close()
c.close()