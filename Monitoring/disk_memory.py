#coding: utf-8
__author__ = 'lau.wenbo'

import psutil

#磁盘使用率
disk = psutil.disk_partitions()
for i in disk:
    print "磁盘：%s   分区格式:%s"%(i.device,i.fstype)
    disk_use = psutil.disk_usage(i.device)
    print "使用了：%sM,空闲：%sM,总共：%sM,使用率\033[1;31;42m%s%%\033[0m,"\
          %(disk_use.used/1024/1024,disk_use.free/1024/1024,
            disk_use.total/1024/1024,disk_use.percent)