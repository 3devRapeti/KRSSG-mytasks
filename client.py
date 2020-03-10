import socket
import sys
import traceback
from threading import Thread
import pickle
def main():
   gru = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   host = "127.0.0.1"
   port = 8000

   try:
      gru.connect((host, port))
   except:
      print("Connection Error")
      sys.exit()
   num=count=0
   count=input("please enter the number of minions-")
   gru.send(pickle.dumps(count))
   num=int(input("please enter the number of elements you want to send-"))
   u = []
   print("please enter your array of numbers")
   for i in range(num):
      ele=int(input())
      u.append(ele)
      i=i+1
   sender=pickle.dumps(u)
   gru.send(sender)
   output=pickle.loads(gru.recv(1024))
   print(output)
   print("Please enter 'quit' to exit")
   message = input(" -> ")
   while message != 'quit':
      gru.sendall(message.encode("utf8"))
      if gru.recv(5120).decode("utf8") == "-":
         pass # null operation
      message = input(" -> ")
   gru.send(b'--quit--')
if __name__ == "__main__":
   main()