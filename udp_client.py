

import socket 
import time
def runClient(seqNum, text,data):
    count = 0
    HOST = '127.0.0.1'
    PORT = 5000
    ACKTime = 2
    addr = (HOST,PORT)
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    client.settimeout(ACKTime)
    #client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
    #client.bind((HOST,PORT))
    seqNum = 0
    ACKData = ""
    Temp = ""
    while count < 5:
        seqNum = seqNum + 1
        text = f"Server Data: "+str(seqNum)
        data = text.encode()
        print(f'sending: {text}')
        input()
        while True:
            try:
                client.sendto(data,(HOST,PORT))
                print("Complete. Sequence Number: "+str(seqNum))
                ACKData, Temp = client.recvfrom(1024)
                ACKData = ACKData.decode()
                ACKData = ACKData.split(":",1)
                if ACKData[1] == f"ACK:{seqNum}":
                    print(f"Data packet found!")
                    break
                else:
                    print(f"Data ACK found, but ACK data is incorrect")
                    print("Actual: "+str(ACKData))
                    print("Expected: "+str(seqNum))
            except Exception as e:
                print(e)
                print("The request took too long and timedout.")
        # #data = struct.pack("!I",seqNum)+text.encode()
        # client.sendto(data,(HOST,PORT))
        # print("Complete. Sequence Number: "+str(seqNum))
        count = count + 1
    client.close()
seqNum = ""
 
data = "Hello"
runClient(seqNum, "",data)
print("Sent to server") 