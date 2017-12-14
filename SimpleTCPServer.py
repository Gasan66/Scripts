import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
for i in range(10):
    pid = os.fork()
if pid == 0:
    while True:
        conn, addr = s.accept()
        data = conn.recv(1024)
        # file = open(str(path), 'r')
        # data = file.read().encode('utf8')
        print(data)
        conn.send(data)
        # file.close();
        conn.close()