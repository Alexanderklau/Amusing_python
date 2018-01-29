# coding: utf-8
__author__ = 'lau.wenbo'

import sys, getopt


opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
input_file=""
output_file=""
for op, value in opts:
    if op == "-i":
        input_file = value
    elif op == "-o":
        output_file = value
    elif op == "-h":
        usage()
        sys.exit()
