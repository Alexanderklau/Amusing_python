# coding: utf-8
__author__ = 'lau.wenbo'


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from operator import itemgetter

lines = []
#read txt file line by line and stored in list
with open('top_info.txt', 'r') as f:
    lines = f.readlines()

print("the top info in doc is: \n")
print(lines, '\n')

lines_len = len(lines) - 7       #info need to process
arrays = [[0 for i in lines[6].split()] for i in range(lines_len)]

#gets into needs to process
for i in range(7, len(lines)):
    arrays[i-7] = lines[i].split()

print("sort info:")
arrays_sorted_by_cpu = sorted(arrays, key=itemgetter(8), reverse = True)
print(arrays_sorted_by_cpu,'\n')