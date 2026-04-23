import socket

for port in range(20,100):
    s = socket.socket()
    if s.connect_ex(("127.0.0.1", port)) == 0:
        print("OPEN:", port)
