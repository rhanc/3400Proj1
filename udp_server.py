import socket  
HOST = '127.0.0.1'
PORT = 5000
ExpectedSeqValue = 0
ActualSeqValue = 0
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
def checkValue(ExpectedSeqValue,ActualSeqValue,socket,addr):
    if ExpectedSeqValue == ActualSeqValue:
        print("Expected value found")
        print(f"Sending value: {ActualSeqValue}".encode())
        socket.sendto(ActualSeqValue.encode(),addr)
        ExpectedSeqValue = 1 - ExpectedSeqValue
    elif ExpectedSeqValue != ActualSeqValue:
        print("Expected value not found")
        value = 1 - ExpectedSeqValue
        socket.sendto(f"Resending the lask ACK: {value}".encode())

def runServer():
    data, addr = s.recvfrom(1024)
    ActualSeqValue,text = data.decode().split(":",1)
    value = int(ActualSeqValue)
    ActualSeqValue = value
    print(f"Received: '{data.decode()}' from {addr}")
    #s.sendto(data, addr)
    checkValue(ExpectedSeqValue,ActualSeqValue,socket,addr)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: 
    s.bind((HOST, PORT))
    print(f"Listening on port {PORT}")

    while True: 
        runServer()
    
