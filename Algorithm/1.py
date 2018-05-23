# coding: utf-8
__author__ = 'lau.wenbo'

import re

f_path = "2.txt"

with open(f_path, 'r') as r:
    lines = r.readlines()
    for i in lines:
        info = i.split(' ')
        name = info[0]
        ip = info[8].split('(')[0]

# with open(f_path, 'w') as w:
#     for l in lines:
#         info=l.split(' ')
#         print info
#         if ("xiaomi1" not in l) and ("10.0.20.132" not in l):
#             print "test"
#             w.write(l)


    #



