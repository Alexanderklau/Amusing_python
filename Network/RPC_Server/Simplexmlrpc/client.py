
# coding: utf-8

__author__ = "lau.wenbo"


from xmlrpclib import ServerProxy
if __name__ == '__main__':
    s = ServerProxy("http://127.0.0.1:3344")
    print s.get_string("hello")