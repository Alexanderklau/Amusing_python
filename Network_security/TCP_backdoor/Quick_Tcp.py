# coding: utf-8

'''
快速搭建一个TCP客户端
'''

__author__ = 'lau.wenbo'

import socket

target_host = "www.baidu.com"

target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host,target_port))

client.send("GET / HTTP1.1\r\host:baidu.com\r\n\r\n")

response = client.recv(4096)

print response