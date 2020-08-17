import socket
import smtplib
'''
host='localhost'
ip=socket.gethostbyname(host)
print("Scanning",ip)
for port in range(1,1025):
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	c=s.connect_ex((ip,port))
	if c==0:
		print(port)
		break
s.close()
'''
email=input("Enter your email id")
password=input("Enter your password")
dest=input("")