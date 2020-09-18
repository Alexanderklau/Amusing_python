# coding: utf-8

__author__ = "lau.wenbo"


from checksum import create_checksum,file_md5
from diskwalk import diskwalk
from os.path import getsize
import csv
import sys


def findDupes(path):
    record = {}
    dup = {}
    d = diskwalk(path)
    files = d.paths()
    for file in files:
        try:
            compound_key = (getsize(file),file_md5(file))
            if compound_key in record:
                dup[file] = record[compound_key]
            else:
                record[compound_key]=file
        except:
            continue
    return dup


if __name__ == '__main__':
    file_list = dict()
    v = list()
    with open("test.csv","a+") as csvfile:
        header = ["源文件", "重复文件"]
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for file in  findDupes("/Users/yemilice/").items():
            writer.writerow({"源文件":file[1],"重复文件":file[0]})
