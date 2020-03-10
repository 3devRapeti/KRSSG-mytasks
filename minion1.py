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
      print("connected successfully")
   except:
      print("Connection Error")
      sys.exit()
   print("Please enter 'quit' to exit")
   data= gru.recv(1024)
   data_arr= pickle.loads(data)
   ans=0
   print("hi")
   for i in range(len(data_arr)):
      ans=ans+data_arr[i]
   ans=pickle.dumps(ans)
   gru.send(ans)
   gru.sendall(message.encode("utf8"))
   if gru.recv(5120).decode("utf8") == "-":
      pass # null operation
   message = input(" -> ")
   gru.send(b'--quit--')
if __name__ == "__main__":
   main()
