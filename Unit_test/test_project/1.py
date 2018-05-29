# coding: utf-8
__author__ = 'lau.wenbo'

record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print(cost)