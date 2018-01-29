# -*- coding:utf8 -*-
# !/user/bin/python
# !conding=utf8
import os
s = os.sep
root = "/home"

for i in os.listdir(root):
    if os.path.isfile(os.path.join(root,i)):
        print i