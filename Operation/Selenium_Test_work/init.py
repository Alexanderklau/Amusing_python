# coding: utf-8

__author__ = 'Yemilice_lau'


from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()

browser.get("http://10.0.9.28/#/infinity/setup")

browser.implicitly_wait(10)

browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/input').send_keys("10.0.9.28")

time.sleep(2)

input = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/input')

input.send_keys(Keys.ENTER)

browser.implicitly_wait(10)

time.sleep(5)

browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div/div/div/div/div[2]/span/span/div').click()

browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div').click()

time.sleep(3)

browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/div').click()



