#!/usr/bin/env python
# _*_coding:utf-8_*_

import os
import sys
import statvfs


def main():
    '''deamon'''
    if 'linux' not in sys.platform:
        print 'sorry! system opreation not supply!'
        sys.exit(3)

    mount = []
    result = []
    label = []
    status = 0

    with open('/proc/mounts') as f:
        for v in f:
            v = v.split()
            mountName = v[1]
            if v[0] in mount:
                continue
            mount.append(v[0])
            try:
                vfs = os.statvfs(mountName)
            except OSError:
                print 'mounted device error, plase check %s' % mountName
                sys.exit(3)
            totalSpace = vfs[statvfs.F_BLOCKS] * vfs[statvfs.F_BSIZE] / (1024 * 1024 * 1024)
            if totalSpace == 0:
                continue
            availSpace = vfs[statvfs.F_BAVAIL] * vfs[statvfs.F_BSIZE] / (1024 * 1024 * 1024)
            availInode = vfs[statvfs.F_FFREE]
            totalInode = vfs[statvfs.F_FILES]
            usedSpace = totalSpace - availSpace
            usedInode = totalInode - availInode
            usedSpacePer = float(usedSpace) / totalSpace * 100
            usedInodePer = float(usedInode) / totalInode * 100
            usedSpacePercent = "{0:.0f}%".format(usedSpacePer)
            usedInodePercent = "{0:.0f}%".format(usedInodePer)
            if usedSpacePer >= 90 or usedInodePer >= 90:
                status = 2
            elif usedSpacePer >= 80 or usedInodePer >= 80:
                status = 1
            info = '%s=%sGB,%s inode=%s;' % (mountName, availSpace, usedSpacePercent, usedInodePercent)
            if info not in result:
                result.append(info)
                label.append('%s=%s;%s;%s;0;%s ' % (mountName, availSpace, 0, availSpace * 2, availSpace * 4))
    print 'free space:%s|%s' % (''.join(result), ''.join(label))
    sys.exit(status)


if __name__ == '__main__':
    main()