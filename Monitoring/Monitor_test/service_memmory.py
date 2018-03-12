#coding: utf-8
__author__ = 'lau.wenbo'

import psutil


memory = psutil.virtual_memory()
print memory.used
print memory.total
ab = float(memory.used)/float(memory.total)*100
print "%.2f%%" % ab
print psutil.swap_memory()