# coding: utf-8

__author__ = "lau.wenbo"


import optparse
from  socket import *

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        print('[+]%d/tcp' % tgtPort)
        connSkt.close()
    except:
        print('[-]%d/tcp close' % tgtPort)

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

    for tgtPorts in tgtPorts:
        print("Scanning port " + tgtPorts)
        connScan(tgtHost, int(tgtPorts))