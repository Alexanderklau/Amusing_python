# coding: utf-8
__author__ = 'lau.wenbo'


import os
import commands
output = os.popen("ps aux|head -1;ps aux|grep -v PID|sort -rn -k +4|head")
print(output.read())
# output = commands.getstatusoutput("ps aux|head -1;ps aux|grep -v PID|sort -rn -k +4|head")
# print(output)