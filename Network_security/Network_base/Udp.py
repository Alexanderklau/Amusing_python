# coding: utf-8

__author__ = 'lau.wenbo'

import socket

target_host = "www.baidu.com"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("AAAAAAAAAAA", (target_host,target_port))

data, addr = client.recvfrom(4096)

print(data)