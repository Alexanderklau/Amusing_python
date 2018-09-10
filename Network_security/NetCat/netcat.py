# coding: utf-8

__author__ = 'lau.wenbo'

import sys
import socket
import getopt
import threading
import subprocess


# 定义全局变量
listen = False
command = False
upload = False
execute  = ""
target = ""
upload_destination = ""
port = ""

def usage():
    print("BHP NET TOOL")
    print
    print("Usage: bhpnet -t target_host -p port")
    print("-l --listen")
