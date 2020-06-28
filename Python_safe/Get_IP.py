# coding: utf-8

__author__ = "lau.wenbo"


# 更新一个关联IP的脚本

import pygeoip

gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')


def printRecord(tgt):
    rec = gi.record_by_addr(tgt)
    city = rec['city']
    region = rec['city']
    country = rec['country_name']
    print("[*] Target: {tgt}".format(tgt=tgt))
    print("{city}, {region}, {country}".format(city=city,region=region,country=country))


if __name__ == "__main__":
    tgt = '173.255.226.98'
    printRecord(tgt)