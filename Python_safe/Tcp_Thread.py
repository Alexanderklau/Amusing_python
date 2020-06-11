# coding: utf-8

__author__ = "lau.wenbo"


import optparse
import socket
from  socket import *
from threading import *

screenLock = Semaphore(value=1)
def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print('[+]%d/tcp' % tgtPort)
        print('[+] ' + str(results))
        connSkt.close()
    except:
        screenLock.acquire()
        print('[-]%d/tcp close' % tgtPort)
    finally:
        screenLock.release()
        connSkt.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve '%s': Unknwn host" %tgtHost)
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for: ' +tgtName[0])
    except:
        print('\n[+] Scan Results for: ' + tgtIP)

    setdefaulttimeout(1)

    print(tgtPorts)
    for tgtPort in tgtPorts:
        print(tgtPort)
        print("Scanning port " + tgtPort)
        connScan(tgtHost, int(tgtPort))

def main():
    parseer = optparse.OptionParser("usage%prog" + "-H <targeet host> -p <targeet port>")
    parseer.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parseer.add_option('-P', dest='tgtPort', type="string", help='specify target port[s] separated by comma')
    (options, args) = parseer.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print('[-] You Must specify a target host and ports[s].')
        exit(0)
    portScan(tgtHost, tgtPorts)

if __name__ == "__main__" :
    # 用法
    # python Tcp_Banner.py -H 192.168.50.1 -P 21,22,80,40,55
    main()