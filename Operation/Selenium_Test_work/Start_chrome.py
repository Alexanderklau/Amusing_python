# coding: utf-8

__author__ = 'Yemilice_lau'

'''
开启一个谷歌浏览器
'''

from selenium import webdriver
import time


browser = webdriver.Chrome()

browser.get("http://10.0.9.28/#/login")

time.sleep(2)

# print(browser.page_source)
browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[3]/div/div[2]/span[1]/input').send_keys("admin")
browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[3]/div/div[2]/span[2]/input').send_keys("123456")
# browser.find_element_by_type("text").send_keys("123456")
# browser.find_element_by_name("password").send_keys("123456")

browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[3]/div/div[2]/span[2]/span[2]').click()

time.sleep(2)



