# coding: utf-8
__author__ = 'Yemilice_lau'

f = open('../access-log', 'a+')
for i in range(1, 10):
    f.write('Hello, world!de + {i}\n'.format(i=i))
f.close()