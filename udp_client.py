import socket 

HOST = ''
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: 
    s.sendto(b'Hello, world!', (HOST, PORT))
    data, addr = s.recvfrom(1024)

print(f"Received '{data.decode()}' from {addr}")