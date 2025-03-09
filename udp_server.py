# import socket  
# HOST = '127.0.0.1'
# PORT = 5000
# ExpectedSeqValue = 0
# ActualSeqValue = 0
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind((HOST, PORT))
# def checkValue(ExpectedSeqValue,ActualSeqValue,socket,addr):
#     if ExpectedSeqValue == ActualSeqValue:
#         print("Expected value found")
#         print(f"Sending value: {ActualSeqValue}".encode())
#         socket.sendto(ActualSeqValue.encode(),addr)
#         ExpectedSeqValue = 1 - ExpectedSeqValue
#     elif ExpectedSeqValue != ActualSeqValue:
#         print("Expected value not found")
#         value = 1 - ExpectedSeqValue
#         socket.sendto(f"Resending the lask ACK: {value}".encode())

# def runServer():
#     data, addr = s.recvfrom(1024)
#     ActualSeqValue,text = data.decode().split(":",1)
#     value = int(ActualSeqValue)
#     ActualSeqValue = value
#     print(f"Received: '{data.decode()}' from {addr}")
#     #s.sendto(data, addr)
#     checkValue(ExpectedSeqValue,ActualSeqValue,socket,addr)

# print(f"Listening on port {PORT}")

# while True: 
#     runServer()
 

import socket
import struct
def bindServer(s):
   server.bind((HOST,PORT))
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
    #print(f"Received: '{data.decode()}' from {addr}")
HOST = '127.0.0.1'
PORT = 0
data = ""
addr = "" 
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server.bind((HOST,PORT))
bindServer(server)
# print(f"Listening on port {PORT}")
printMessage(f"Listening on port {PORT}")
runServer(data,addr,server)
# while True:
#    data, addr = server.recvfrom(1024)
#    print(f"Received: '{data.decode()}' from {addr}")