# -*- coding:utf8 -*-
import os, os.path
import commands
import logging
import time
from datetime import datetime
from functools import wraps
import time
from multiprocessing import Pool


Path = r"/media"

print([os.path.join(root,fn) for root,dirs,files in os.walk(Path) for fn in files])