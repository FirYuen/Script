#-*- encoding:utf-8 -*-
import socket, traceback
host= '' 
port = 6666  
  
  
s = socket.socket()  
s.bind((host, port))  
s.listen(5)  
conn, addr = s.accept()  
  
  
while True:  
    data = conn.recv(512)  
    print data+"\n"  
    if not data:  
        break;  
    #conn.sendall(data)  
conn.close()