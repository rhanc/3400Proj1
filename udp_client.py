

import socket 
def runClient(seqNum, text,data,h,p):
    count = 0
    HOST = '127.0.0.1'
    PORT = 0
    addr = (HOST,PORT)
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    client.bind((HOST,PORT))
    seqNum = 0
    while count < 5:
        seqNum = seqNum + 1
        text = f"Server Data: "+str(seqNum)
        #data = struct.pack("!I",seqNum)+text.encode()
        data = text.encode()
        client.sendto(data,(HOST,PORT))
        print("Complete. Sequence Number: "+str(seqNum))
        count = count + 1
    client.close()
seqNum = ""
 
data = "Hello"
runClient(seqNum, "",data)
print("Sent to server") 