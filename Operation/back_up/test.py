# coding: utf-8
__author__ = 'lau.wenbo'

import json
import commands

import os, sys
# 打开文件
path = "./back_up"
dirs = os.listdir( path )
for file in dirs:
    print file
