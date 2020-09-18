# coding: utf-8

__author__ = "lau.wenbo"


import hashlib,sys
import os

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
<<<<<<< HEAD
=======


_FILE_SLIM = (100 * 1024 * 1024)  # 100MB


def file_md5(filename):
    calltimes = 0
    hmd5 = hashlib.md5()
    fp = open(filename, "rb")
    f_size = os.stat(filename).st_size
    if f_size > _FILE_SLIM:
        while (f_size > _FILE_SLIM):
            hmd5.update(fp.read(_FILE_SLIM))
            f_size /= _FILE_SLIM
            calltimes += 1  # delete
        if (f_size > 0) and (f_size <= _FILE_SLIM):
            hmd5.update(fp.read())
    else:
        hmd5.update(fp.read())

    return (hmd5.hexdigest(), calltimes)


if __name__ == '__main__':
    (hvalue, ctimes) = file_md5("./__init__.py")
    print(hvalue)
>>>>>>> e86329e7ec960a55619765e7287214dde46bc417
