# coding: utf-8

__author__ = "lau.wenbo"


import hashlib,sys

# 分块读MD，速度快

def create_checksum(path):
    fp = open(path)
    checksum = hashlib.md5()
    while True:
        buffer = fp.read(8192)
        if not buffer: break
        checksum.update(buffer)
    fp.close()
    checksum = checksum.digest()
    return checksum
