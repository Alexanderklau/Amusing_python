# coding: utf-8

__author__ = "lau.wenbo"


from scapy.all import *

def CalTSN(tgt):
    seqNum = 0
    preNum = 0
    diffSeq = 0
    for x in range(1, 5):
        if preNum != 0:
            preNum = seqNum
        pkt = IP(dst=tgt) / TCP()
        ans = sr1(pkt, verbose=0)
        seqNum = ans.getlayer(TCP).seq
        diffSeq = seqNum - preNum
        print(diffSeq)
    return seqNum + diffSeq

if __name__ == "__main__":
    tgt = "192.168.1.106"
    seqNum = calTSN(tgt)
    print(seqNum + 1)