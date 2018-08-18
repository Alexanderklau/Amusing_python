# coding: utf-8

__author__ = 'lau.wenbo'

import re

strs = "X4MIN、餐补"

x = re.compile(r'\d+').findall(strs)[0]

print x