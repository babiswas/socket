from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
from socket import gethostname,gethostbyname
from pickle import loads,dumps

def client(host,port):
    sk=socket(AF_INET,SOCK_STREAM)
    sk.connect((host,port))
    message=input("Add message")
    sk.sendall(dumps(message))
    while True:
       message=loads(sk.recv(4096))
       print(message)
       new_message=input("Enter message")
       sk.sendall(dumps(new_message))
       if new_message=="bye":
          break
    sk.close()

if __name__=="__main__":
   host=gethostname()
   host_ip=gethostbyname(host)
   client(host_ip,5000)
   
       