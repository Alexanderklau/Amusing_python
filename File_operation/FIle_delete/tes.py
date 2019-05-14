# coding: utf-8
__author__ = 'Yemilice_lau'

import re

a = 'Filesystem               Size  Used Avail Use% Mounted on \n \
    /dev/mapper/centos-root   17G  2.0G   16G  12% /'

print a.split('\n')[1].split('%')