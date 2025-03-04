import socket

HOST = ''
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: s.bind((HOST, PORT))
print(f"Listening on port {PORT}")

    while True: 
        data, addr = s.recvfrom(1024)
        print(f"Received: '{data.decode()}' from {addr}")
        s.sendto(data, addr)