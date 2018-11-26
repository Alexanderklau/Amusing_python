# coding: utf-8
__author__ = 'lau.wenbo'

import sys
import os

"""
get file
determine whether a file exists!
"""

def main():
    sys.argv.append("")
    filename = sys.argv[1]
    if not os.path.isabs(filename):
        raise  SystemExit(filename + ' does not exists')
    elif not os.access(filename, os.R_OK):
        raise SystemExit(filename + ' is not accessible')
    else:
        print(filename + ' is accessiable')


if __name__ == '__main__':
    main()