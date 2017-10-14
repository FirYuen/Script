#-*- encoding:utf-8 -*-
import socket
import thread,threading,time

sockIndex = 1

def connToServer ():
    global sockIndex
    conn = socket.socket()
    conn.connect(("192.168.60.23", 60001))
    conn.send(b'OspLog()')
    print sockIndex
    sockIndex = sockIndex + 1
    time.sleep(0.01)
    #conn.close()
    #while True:
        #rev = conn.recv(1024)
        #print 'get server msg:' + str(rev)
        #break
threads = []
times = 2000000

for i in range(0,times):
    t = threading.Thread(target=connToServer())
    threads.append(t)
for i in range(0,times):
    threads[i].start()
for i in range(0,times):
    threads[i].join()