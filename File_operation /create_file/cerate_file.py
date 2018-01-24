#coding: utf-8
__author__ = 'lau.wenbo'


import os,sys

base = './test'
i = 1
for j in range(100):
    file_name = base+str(i)
    os.mkdir(file_name)
    i=i+1