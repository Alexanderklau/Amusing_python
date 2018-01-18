#coding: utf-8
import os, time, random
import logging
import commands
from datetime import datetime
import multiprocessing

#取得Directory的目录，依次去读取。
def create_directory():
    dir = []
    f = open("Directory.txt", "r")
    for i in f.read():
        return dir


print(create_directory())
