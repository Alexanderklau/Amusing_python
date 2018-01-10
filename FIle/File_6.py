#coding: utf-8
import multiprocessing, Queue
import os
import time
from multiprocessing import Process
from time import sleep
from random import randint
q = multiprocessing.Queue()
# q = Queue.Queue(10)
fns=[os.path.join(root,fn) for root,dirs,files in os.walk(r"/home/lau/下载") for fn in files]
for f in fns:
    q.put(q)

print(q.get())