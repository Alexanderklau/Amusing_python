# coding: utf-8

__author__ = "lau.wenbo"


from checksum import create_checksum
from diskwalk import diskwalk
from os.path import getsize
import csv
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def findDupes(path):
    record = {}
    dup = {}
    d = diskwalk(path)
    files = d.paths()
    for file in files:
        try:
            #compound_key = (getsize(file),create_checksum(file))
            compound_key = (getsize(file), file.split("/")[-1])
            if compound_key in record:
                dup[file] = record[compound_key]
            else:
                record[compound_key]=file
        except:
            continue
    return dup


if __name__ == '__main__':
    path = sys.argv[1]
    csv_path = sys.argv[2]
    if not os.path.isdir(path) or not os.path.isdir(csv_path) or csv_path[-1] != "/":
        print u"参数不是一个有效的文件夹！"
        exit()
    else:
        path = path.decode("utf-8")
        print u"待检测的文件夹为{path}".format(path=path)
        with open(u"{csv_path}重复文件.csv".format(csv_path=csv_path),"w+") as csvfile:
            # 源文件 重复文件
            header = ["Source", "Duplicate"]
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            print u"开始遍历文件夹，寻找重复文件，请等待........."
            print u"开始写入CSV文件，请等待........"
            for file in findDupes(path).items():
                writer.writerow({"Source":file[1],"Duplicate":file[0]})
