import socket
import os
from _thread import start_new_thread
from datetime import datetime

if not os.path.exists(os.path.dirname(os.path.abspath(__file__))+"/log"):
    os.makedirs(os.path.dirname(os.path.abspath(__file__))+"/log")
    
currentClient=0
ServerSideSocket = socket.socket()
host = '0.0.0.0'
port = 2004
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Server is listening..')
ServerSideSocket.listen(5)

def multi_threaded_client(connection,address):
    global currentClient
    while True:
        data = connection.recv(4096)
        if data:
            rec=data.decode('utf-8').split("||")
            result="{}@{}:{}> {}".format(rec[0],address[0],address[1],rec[1]+ "\n")
            if not os.path.exists(os.path.dirname(os.path.abspath(__file__))+"/log/"+rec[0]):
                os.makedirs(os.path.dirname(os.path.abspath(__file__))+"/log/"+rec[0])
            now=datetime.now()
            fl="/log/{}/{}-{}-{}-.txt".format(rec[0],now.year,now.month,now.day)
            result="{}@{}:{} at {}:{}:{}> {}".format(rec[0],address[0],address[1],now.hour,now.minute,now.second,rec[1]+ "\n")

            with open(os.path.dirname(os.path.abspath(__file__))+fl, "a") as myfile:
                myfile.write(result)

            
        if not data:
            currentClient-=1
            print("{}:{}> DISCONNECTED, ACTUALLY THERE ARE {} CLIENT CONNECTED".format(address[0],address[1],currentClient))
            break
    connection.close()

while True:
    Client, address = ServerSideSocket.accept()
    currentClient+=1
    print("{}:{}> CONNECTED, ACTUALLY THERE ARE {} CLIENT CONNECTED".format(address[0],address[1],currentClient))
    start_new_thread(multi_threaded_client, (Client,address, ))
ServerSideSocket.close()

