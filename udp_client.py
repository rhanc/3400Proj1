# import socket as s 
# HOST = '127.0.0.1'  
# PORT = 5000
# expectedValue = 0
# message = "Hello World"
# socket = s.socket(s.AF_INET, s.SOCK_DGRAM) 
# address = (HOST,PORT)
# def CheckValues(seqActual, seqExpected):
#     result = False
#     if seqActual == seqExpected:
#         print("Correct ACK value: "+seqActual)
#         seqActual = 1 - seqActual
#         result = True
#     elif seqActual != seqExpected:
#         print("Incorrect value") 
#     return result
# def runClient(sValue,message,socket,address):
#     #data
#     #dataACK
#     #addr
#     #socket = 0
#     result = True
#     if result == True:
#         while result == True:
#             MessageResult = f"{sValue,message}"
#             socket.sendto(MessageResult.encode(),address)
#             try:
#                 data, addr = socket.recvfrom(1024)
#                 dataACK = data.decode().split(":")
#                 dataACK = int(dataACK)
#                 result = CheckValues(dataACK, sValue)
#                 if result == True:
#                     break
#             except:
#                 print("Request timedout")
#     socket.close()


# runClient(expectedValue,message,socket,address)

# # with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: 
    
# #     s.sendto(b'Hello, world!', (HOST, PORT))
# #     data, addr = s.recvfrom(1024)

# # print(f"Received '{data.decode()}' from {addr}")

import socket,time,struct
def runClient(seqNum, text,data,client):
    count = 0
    seqNum = 0
    while count < 5:
        seqNum = seqNum + 1
        text = f"Server Data: "+str(seqNum)
        #data = struct.pack("!I",seqNum)+text.encode()
        data = text.encode()
        print("Complete. Sequence Number: "+str(seqNum))
seqNum = ""
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
HOST = '127.0.0.1'
PORT = 5000
addr = (HOST,PORT)
data = "Hello"
runClient(seqNum, "",data,client)
print("Sent to server")