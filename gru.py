import socket
import sys
import traceback
from threading import Thread
import numpy
import pickle
i=0
def main():
   start_server()
def start_server():
   host = "127.0.0.1"
   port = 8000 # arbitrary non-privileged port

   
   gru_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   gru_client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   print("Socket created")
   try:
      gru_client.bind((host, port))
   except:
      print("Bind failed. Error : " + str(sys.exc_info()))
      sys.exit()
   gru_client.listen(1) # queue up to 6 requests
   print("Socket now listening ")
   # infinite loop- do not reset for every requests
   while True:
      connection, address = gru_client.accept()
      ip, port = str(address[0]), str(address[1])
      print("Connected with " + ip + ":" + port)
      count=int(pickle.loads(connection.recv(4096)))
      print(count)
      data= connection.recv(1024)
      data_arr= pickle.loads(data)
      sub_arr=numpy.array_split(data_arr,count)
      print("hi")
      try:
         Thread(target=client_Thread, args=(connection, ip, port, count, ans_arr)).start()
      except:
         print("Thread did not start.")
         traceback.print_exc()
      connection.close()


def client_Thread(connection, ip, port, count, ans_arr, max_buffer_size = 5120):
   is_active = True
   while is_active:
      ans=0
      j=0
      gru_minion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      gru_minion.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      print("Socket created")
      try:
         gru_minion.bind((host, port))
      except:
         print("Bind failed. Error : " + str(sys.exc_info()))
         sys.exit()
      gru_minion.listen(count) # queue up to  requests
      print("Socket now listening")
      i=0
      # infinite loop- do reset for every requests
      while True:
         connection2, address = gru_minion.accept()
         ip, port = str(address[0]), str(address[1])
         print("Connected with " + ip + ":" + port)
         print("hi")
         try:
            Thread(target=minion_thread, args=(connection2, ip, port,count, sub_arr, i)).start()
         except:
            print("Thread did not start.")
            traceback.print_exc()
         connection2.close()

      while j< count:
         ans=ans+ans_arr[j]
      connection.send(ans)
      client_input=connection.recv(1024)
      if "" in client_input:
         print("Client is requesting to quit")
         connection.close()
         print("Connection " + ip + ":" + port + " closed")
         is_active = False
      else:
         print("Processed result: {}".format(client_input))
         connection.sendall("-".encode("utf8"))


def minion_Thread(connection, ip, port, count, sub_arr, i, max_buffer_size = 5120):
   is_active = True
   while is_active:
      sender=pickle.dumps(sub_arr[i])
      connection.send(sender)
      ans_arr=numpy.zeros(count)
      ans_arr[i]=pickle.loads(connection.recv(4096))
      i=i+1
      return ans_arr
def process_input(input_str):
   print("Processing the input received from client")
   return "Hello " + str(input_str).upper()
if __name__ == "__main__":
   main() 