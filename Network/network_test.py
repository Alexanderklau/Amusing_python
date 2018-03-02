# coding: utf-8
__author__ = 'lau.wenbo'


import sys, socket

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

print("Server is running on port {}; press Ctrl-C to terminator".format(port))

while 1:
    clientsock, clientaddr = s.accept()
    clientfile = clientsock.makefile("rw", 0)
    clientfile.write("Welcome, " + str(clientaddr) + "\n")
    clientfile.write("Please enter a string: ")
    line = clientfile.readline().strip()
    clientfile.write("You entered {} characters.\n".format(len(line)))
    clientfile.close()
    clientsock.close()


