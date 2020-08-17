import socket

host='127.0.0.1'
port=5000
server=('127.0.0.1',5000)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))

while True:
	msg=input("Enter a message")
	s.sendto(msg.encode(),server)
	data,addr=s.recvfrom(1024) 
	print("Received Data:"+str(data))
	continue
s.close()