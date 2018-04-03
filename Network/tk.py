# coding: utf-8
__author__ = 'lau.wenbo'

import socket, sys

port = 233
host = "127.0.0.1"
filename = sys.argv[1]


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

s.sendall(filename + "\r\n")

while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)