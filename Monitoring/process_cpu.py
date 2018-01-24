# coding: utf-8
__author__ = 'lau.wenbo'

import psutil

p = psutil.Process()
pro_info = p.as_dict(attrs=['pid', 'name', 'username'])
print psutil.cpu_count()