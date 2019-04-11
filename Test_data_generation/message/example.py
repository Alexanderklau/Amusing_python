# -*- coding: utf-8 -*-
__author__ = 'yemilice_lau'
import random

print random.randint(1, 10)
# print random.choice(int(123))
x = ['123','333','666']
print '-'.join(x)

from operator import mul
print reduce(mul, range(1, 6))

