# coding: utf-8

__author__ = 'lau.wenbo'

import socket
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.settimeout(1)
try:
  sk.connect(('www.sharejs.com',80))
  print 'Server port 80 OK!'
except Exception:
  print 'Server port 80 not connect!'
sk.close()