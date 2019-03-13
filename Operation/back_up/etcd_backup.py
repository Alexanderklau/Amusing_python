# coding: utf-8

__author__ = 'lau.wenbo'


import time
import commands
import ConfigParser
import json

basegetcmd = 'ETCDCTL_API=3 /usr/bin/etcdctl get "%s" --prefix=true --command-timeout=300s'
baseputcmd = "ETCDCTL_API=3 /usr/bin/etcdctl put"
cmdstop = "/usr/bin/systemctl stop sysdb"
cmdstart = "/usr/bin/systemctl start sysdb"
cmdaddnode = '/bin/python ./sysdb_rebuild.py '
keylist = ["createdIndex", "fs", "groups", "infi", "users", "monitor", "monlog"]
keyfile = "etcdKey.log"
kvfile = "etcdData.log"
global ips

ips = ""


class TimeoutError(Exception):
    pass


'''
def execute(cmd, timeout = 10):
	try:
		p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
		t_beginning = time.time()
		seconds_passed = 0
		while True:
			if p.poll() is not None:
				break
			seconds_passed = time.time() - t_beginning
			if timeout >= 0 and seconds_passed > timeout:
				p.terminate()
				raise TimeoutError(cmd, timeout)
			time.sleep(0.1)
		return (p.wait(), p.stdout.read())
	except TimeoutError, e:
		return (-1, "exceeded time %s seconds in executing: %s" % (e[1], e[0]))
'''


def execute(cmd):
    (status, output) = commands.getstatusoutput(cmd)
    return (status, output)

def read_config(config):
    with open(config, 'r') as f:
        temp = json.loads(f.read())
    return temp

def dumpAllData(path="./back_up/etcd/"):
    fKey = open(path + keyfile, "w")
    fData = open(path + kvfile, "w")
    for pre_key in keylist:
        cmd = basegetcmd % pre_key
        print "cmd: ", cmd
        for i in range(3):
            (status, output) = execute(cmd + ' --keys-only | tr -s "\n"')
            if (status == 0):
                print "[ok]"
                if len(output):
                    fKey.writelines(output)
                    fKey.writelines("\n")
            else:
                print output
            (status, output) = execute(cmd)
            if (status == 0):
                print "[ok]"
                if len(output):
                    fData.writelines(output)
                    fData.writelines("\n")
                break
            else:
                print output
                time.sleep(5)
                print "try again"
    fKey.close()
    fData.close()


def getEtcdkey(keyData):
    try:
        f = open(keyData)
        info = f.read()
        f.close()
        info = info.split('\n')
        return (0, info)
    except Exception, ex:
        print Exception, ":", ex
        return (-1, "")


def getEtcdinfo(kvData):
    try:
        f = open(kvData)
        info = f.read()
        f.close()
        info = info.split('\n')
        return (0, info)
    except Exception, ex:
        print Exception, ":", ex
        return (-1, "")


def getSysdbCluKey():
    cmd = 'ETCDCTL_API=3 /usr/bin/etcdctl get "" --from-key --keys-only  | grep infi-cluster | tr -s "\n"'
    (status, result) = execute(cmd)
    result = result.split('\n')
    if status != 0:
        print result
        print "get infi cluster info err!"
        exit(1)
    return result


def putAllData(path="./back_up/etcd/"):
    cleanSysdb()
    (ret, key) = getEtcdkey(path + keyfile)
    (ret, info) = getEtcdinfo(path + kvfile)
    for item in key:
        i = info.index(item)
        if len(info) == i + 1:
            break
        if item.strip() == '':
            break
        value = info[i + 1]

        value = value.replace('"', r'\"')
        value = '"' + value + '"'
        putcmd = baseputcmd + " " + item + " " + value
        (status, result) = execute(putcmd)
        if status != 0:
            print putcmd
            print result
            print "input error! please try again"
            exit(1)
        print putcmd + "\n" + "OK"
    print "导入etcd数据完成！"
    print "------------------------------"
    # print "请输入需要重新添加的sysdb节点ip，以逗号分隔(如:10.0.7.21,10.0.7.22,10.0.7.23):"
    # ips = raw_input()
    global ips
    ip_config = read_config("ip.json")
    ips = ip_config["add_ip"]
    cmd = cmdaddnode + ips
    (status, result) = execute(cmd)
    if status != 0:
        print "add sysdb node failed, please try again!"
        exit(1)

    cluKey = getSysdbCluKey()
    cmd = "ETCDCTL_API=3 /usr/bin/etcdctl put"
    for item in cluKey:
        print info
        try:
            i = info.index(item)
        except:
            print "no %s in old sysdb" % item
            exit(1)
        if len(info) == i + 1:
            break
        value = info[i + 1]

        value = value.replace('"', r'\"');
        value = '"' + value + '"'
        putcmd = cmd + " " + item + " " + value
        (status, result) = execute(putcmd)
        if status != 0:
            print result
            print "input cluster info error! please try again"
            exit(1)
        print putcmd + "\n" + "OK"
    print "添加sysdb节点成功！"


def modsysdbconf(ip):
    try:
        cf = ConfigParser.ConfigParser()
        cf.read("/etc/sysdb/sysdb.conf")
        cfd = open("/etc/sysdb/sysdb.conf", 'w')
        cf.set('nodes', 'nodes', ip)
        cf.write(cfd)
        cfd.close()
        return (0, "success!")
    except Exception, ex:
        return (-1, "修改sysdb配置文件失败！")


def clearsysdbconf(ips):
    cmdrm = '"rm /var/lib/sysdb/* -rf"'
    for ip in ips:
        cmd = 'ssh root@' + ip + ' ' + '"' + cmdstop + '"'
        (status, result) = execute(cmd)
        if status != 0:
            print "停止sysdb服务失败！"
            print result
            exit(1)

    for ip in ips:
        cmd = 'ssh root@' + ip + ' ' + cmdrm
        (status, result) = execute(cmd)
        if status != 0:
            print "清除sysdb配置文件失败！"
            print result
            exit(1)
    firstip = ips[0]
    (status, result) = modsysdbconf(firstip)
    if status != 0:
        print result
        exit(1)
    (status, result) = execute(cmdstart)
    if status != 0:
        print "启动sysdb服务失败！"
        print result
        exit(0)
    time.sleep(2)


def cleanSysdb():
    global ips
    ips = read_config("ip.json")
    iplist = ips["clear_ip"]
    clearsysdbconf(iplist)
    print "清除sysdb配置完成！"


def main(argv):
    if 3 == len(argv):
        if argv[1] == "backup":
            dumpAllData(argv[2])
        elif argv[1] == "restore":
            putAllData(argv[2])
        else:
            print "param error."
    else:
        print "param error."


if __name__ == "__main__":
    pass
    # cleanSysdb()