
 

import socket
import struct
HOST = ''
PORT = 5000
data = ""
addr = "" 
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
def bindServer(s,HOST,PORT):
   s.bind((HOST,PORT))
def printMessage(message):
   print(message)
def showResult(addr, ActualSeqValue,nums):
   print(f"Got data. Server Address: {addr} | Numbers: {ActualSeqValue} | Data: {nums.decode(errors='ignore')}")
def runServer(data,addr,server):
   ActualSeqValue = 0
   nums = 0
   result = False
   while True:
    data, addr = server.recvfrom(1024)
    result = (len(data)<4)
    if result == True:
       continue
    ActualSeqValue,nums = struct.unpack("!I", data[:4])[0],data[4:]
    showResult(addr, ActualSeqValue,nums) 

bindServer(server,HOST,PORT) 
printMessage(f"Listening on port {PORT}")
runServer(data,addr,server) 