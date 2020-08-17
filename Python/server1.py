import socket 
import select 
import sys 
# from thread import *
import threading
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 4
WAVE_OUTPUT_FILENAME = "server_output.wav"
WIDTH = 2
frames = []

"""The first argument AF_INET is the address domain of the 
socket. This is used when we have an Internet Domain with 
any two hosts The second argument is the type of socket. 
SOCK_STREAM means that data or characters are read in 
a continuous flow."""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
  

  
# takes the first argument from command prompt as IP address 
IP_address =  '10.120.106.85'
  
# takes second argument from command prompt as port number 
Port = 50007              
  
""" 
binds the server to an entered IP address and at the 
specified port number. 
The client must be aware of these parameters 
"""
server.bind((IP_address, Port)) 
  
""" 
listens for 100 active connections. This number can be 
increased as per convenience. 
"""
server.listen(100) 
  
list_of_clients = [] 
  
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)


def clientthread(conn, addr): 
  
    # sends a message to the client whose user object is conn
    message= "Welcome to this chatroom!"
    conn.send(message.encode()) 
    print('Connected by', addr)
    data = conn.recv(1024)

    i=1
    while True:
        stream.write(data)
        data = conn.recv(1024)
        print(i)
        i=i+1
        frames.append(data)
        print(data)
        broadcast(data, conn)

  
"""Using the below function, we broadcast the message to all 
clients who's object is not the same as the one sending 
the message """
def broadcast(message, connection): 
    for clients in list_of_clients: 
        if clients!=connection: 
            try: 
                clients.sendall(message) 
            except: 
                clients.close() 
  
                # if the link is broken, we remove the client 
                remove(clients) 
  
"""The following function simply removes the object 
from the list that was created at the beginning of  
the program"""
def remove(connection): 
    if connection in list_of_clients: 
        list_of_clients.remove(connection) 
  
while True: 
  
    """Accepts a connection request and stores two parameters,  
    conn which is a socket object for that user, and addr  
    which contains the IP address of the client that just  
    connected"""
    conn, addr = server.accept() 
  
    """Maintains a list of clients for ease of broadcasting 
    a message to all available people in the chatroom"""
    list_of_clients.append(conn) 
  
    # prints the address of the user that just connected 
    print (addr[0] + " connected")
  
    # creates and individual thread for every user  
    # that connects 
    #start_new_thread(clientthread,(conn,addr))  
    threading.Thread(target=clientthread, args=(conn,addr,)).start()
    #threading.Thread(clientthread,(conn,addr)).start(None)   
  
conn.close() 
stream.stop_stream()
stream.close()
p.terminate()
server.close() 