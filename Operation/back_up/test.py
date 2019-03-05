# coding: utf-8
__author__ = 'lau.wenbo'

import json
import commands
import time
import psutil as ps
import os, sys


str = "{'mgr_node': 1, 'sys_node': 1, 'mon_node': 1, 'nas_node': 255, 'hbeatip': u'10.0.6.214', 'ip': u'10.0.6.214', 'mds_node': 1, 'storage_node': 1}"
print(eval(str))