# coding: utf-8

__author__ = 'Yemilice_lau'


import commands
import re
import sys


def execute(cmd):
    (status, output) = commands.getstatusoutput(cmd)
    return (status, output)


def work(copydir, mountdir):
        (_, z) = execute("cat /proc/mounts")
        try:
                check_dir = copydir.split("/")[1]
                reobj = re.search(check_dir, z).group(0)
                print "mount! next!"
                resy = execute("rsync -artogpclDP {mountdir} {copydir}".format(mountdir=mountdir, copydir=copydir))
                print "end rsync! exit"
        except:
                print "not mount"
                exit()


if __name__ == "__main__":
        mountdir = sys.argv[1]
        copydir = sys.argv[2]
        work(copydir, mountdir)
