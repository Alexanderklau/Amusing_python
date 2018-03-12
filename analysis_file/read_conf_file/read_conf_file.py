# coding: utf-8
__author__ = 'lau.wenbo'


# import ConfigParser
#
#
# cf = ConfigParser.RawConfigParser()
#
# print "use RawConfigParser() read"
# cf.read("test2.conf")
# print cf.get("portal", "url")
#
# print "use RawConfigParser() write"
# cf.set("portal", "url2", "%(host)s:%(port)s")
# print cf.get("portal", "url2")


import ConfigParser

cf = ConfigParser.ConfigParser()

print "use ConfigParser() read"
cf.read("test2.conf")
print cf.get("portal", "url")

print "use ConfigParser() write"
cf.set("portal", "url2", "%(host)s:%(port)s")
print cf.get("portal", "url2")