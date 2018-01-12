#!/usr/bin/env python
import os

f = open("file.txt")
data = [line.strip() for line in f]
data2 = [os.path.join(root,fn) for root,dirs,files in os.walk("/home/lau") for fn in files]
print(list(set(data) ^ set(data2)))
