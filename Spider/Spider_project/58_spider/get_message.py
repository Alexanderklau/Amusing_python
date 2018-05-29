# coding: utf-8
__author__ = "Yemilice_lau"


from lxml import etree
import requests
import time

class Get_message(object):

    def __init__(self):
        self.house_url = []
        self.page_url = []

    def Get_page_url(self, url):
        global messages, pn_page
        xpath_command = '//*[@id="bottom_ad_li"]/div[2]/a[3]/@href'
        try:
            messages = self.obtainment_process(url = url, xpah_command=xpath_command)
        except Exception, e:
            print Exception,":",e
        for message in messages:
            pn = message.split('pn')[1]
            pn_page = pn.replace('/', '')

        for i in range(1,int(pn_page) + 1):
            self.page_url.append("http://cd.58.com/chuzu/0/pn{0}/".format(i))

        return self.page_url

    def Get_house_url(self, page_url):
        pass

    def Get_house_message(self, house_url):
        pass

    def obtainment_process(self, url, xpah_command):
        try:
            a = requests.get(url).content
        except Exception as e:
            print Exception, ":", e
        selector = etree.HTML(a, parser=None, base_url=None)
        message = selector.xpath(xpah_command)
        return message



