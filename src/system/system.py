import socket
#!/usr/bin/env python2
#encoding: windows-1252

s = socket.socket (
    socket.AF_PACKET,
    socket.SOCK_RAW,
    socket.hosts(3)
)

s.bind(('eth0', 3))

while True:
    message = s.recv(1024)
    print(repr(message))