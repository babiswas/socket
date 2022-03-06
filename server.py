from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
from threading import Thread
from socket import gethostname,gethostbyname
from pickle import loads
from pickle import dumps


def handle(conn):
   while True:
      try:
         message=loads(conn.recv(4096))
         print(message)
         conn.send(dumps(message))
         if message=="bye":
           conn.close()
      except Exception as e:
         conn.close()
   
      

def create_server(host,port):
    sk=socket(AF_INET,SOCK_STREAM)
    sk.bind((host,port))
    sk.listen(5)
    while True:
       conn,addr=sk.accept()
       th=Thread(target=handle,args=[conn,])
       th.start()
    conn.close()

if __name__=="__main__":
   host=gethostname()
   ip=gethostbyname(host)
   create_server(host,5000)
   
   
       