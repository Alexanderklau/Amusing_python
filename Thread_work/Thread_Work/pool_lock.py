# coding: utf-8

__author__ = 'Yemilice_lau'


"""
一个线程池框架
"""

from socket import AF_INET, SOCK_STREAM, socket
from concurrent.futures import ThreadPoolExecutor


# 假装跑一个服务器client
def echo_client(sock, client_addr):
    '''
    Handle a client connection
    '''
    print('Got connection from', client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print('Client closed connection')
    sock.close()

# 假装跑一个server
def echo_server(addr):
    # 最大128
    pool = ThreadPoolExecutor(128)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        pool.submit(echo_client, client_sock, client_addr)

echo_server(('',15000))