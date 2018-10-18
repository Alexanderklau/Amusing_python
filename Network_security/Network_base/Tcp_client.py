# coding: utf-8
__author__ = 'lau.wenbo'

import socket

target_host = "0.0.0.0"
target_port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send("GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")

response = client.recv(4096)

print(response)
