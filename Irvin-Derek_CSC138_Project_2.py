from socket import *
import threading
import thread

#client thread
def handler(clientSocket, addr):
      try:
         #get data through client socket   
         message = clientSocket.recv(2048)
         filename = message.split()[1]
         f = open(filename[1:])
         outputdata = f.read()
         #print file on server
         print outputdata
         #send file to client browser 
         clientSocket.send('\HTTP/1.1 200 OK\n\n')
         clientSocket.send(outputdata)
         #close the socket
         clientSocket.close()
      except IOError:
         #sends 404 error if file is not found
         print '404 not found'
         clientSocket.send('\HTTP/1.1 404 Not Found\n')
         clientSocket.close()

#main 
if __name__=='__main__':
#set up host and portNo
   Host = ''
   Port = 80
#initialize server Socket
   serverSocket = socket(AF_INET, SOCK_STREAM)
#bind to local host and port 80
   serverSocket.bind((Host, Port))
#start listening for client
   serverSocket.listen(1)
   print 'Server up on port 80\n'
   while True:
      print 'Ready to serve...\n'
      clientSocket, addr = serverSocket.accept()
      #start new thread for client socket 
      t = threading.Thread(target = handler, args=(clientSocket,addr))
      t.start()
      #waits for client thread to finish
      t.join()