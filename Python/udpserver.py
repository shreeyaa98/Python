import socket
host='127.0.0.1'
port=5000

client=[]

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(1)
quitting=False
print("Server Started")
while not quitting:
	data,addr=s.recvfrom(1024)
	print(str(data))
	if str(data)=='Quit':
		quitting=True
	if addr not in client:
		print(addr)
		client.append(addr)

	print("Received"+str(data))
	for client in clients:
		msg=input("Enter Data to send")
		s.sendto(msg,client)

s.close()