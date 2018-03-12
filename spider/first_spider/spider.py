#coding: utf-8
__author__ = "Yemilice_lau"

import urllib2


def downloads(url, num_retries=2):
    global html
    print "Downloading.....{0}".format(url)
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return downloads(url, num_retries-1)
    return html



downloads('http://httpstat.us/500')




