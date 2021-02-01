# coding: utf-8

__author__ = 'Yemilice_lau'


from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()

browser.get("http://10.0.8.72/#/infinity/setup")

browser.implicitly_wait(10)

# 初始化输入IP
browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/input').send_keys("2001:db8:1:8:8fa6:20f4:aeb:8e25,2001:db8:1:8:8fa6:20f4:aeb:8e92,2001:db8:1:8:f816:3eff:fe35:4940")


# 找到INPUT 然后去回车
input = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/input')

# 回车
input.send_keys(Keys.ENTER)

# 等待元素加载
browser.implicitly_wait(30)

# 等待元素加载完成
time.sleep(15)

# 下一步
browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/span/span/div').click()

# 内部管理网络
# /html/body/div[4]/div/div/div/div[2]/div/div/div/div[2]
# /html/body/div[4]/div/div
# /html/body/div[4]/div/div/div/div[2]/div/div/div/div[1]
browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div').click()

time.sleep(3)

# 选择内部管理网络
browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div/div/div/div[1]').click()


# # 数据同步网络
browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div').click()

time.sleep(3)

browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/div/div[1]').click()

# # 外部访问网络
browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[4]/div/div').click()

time.sleep(3)

browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[1]').click()

time.sleep(2)

browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div/div/div/div/div[2]/span[2]/span/div').click()

time.sleep(2)

browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div[3]/div[1]/div[2]/div[3]/div/div/input').send_keys("123456")

time.sleep(0.5)

browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div[3]/div[1]/div[2]/div[4]/div/div/input').send_keys("123456")

time.sleep(0.5)

browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div/div/div/div/div[2]/span[2]/span/div').click()

time.sleep(0.5)

browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div/div/div/div/div[2]/span[2]/button').click()


#
# time.sleep(5)
#
# browser.implicitly_wait(10)
#
# browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[1]').click()
#
# browser.implicitly_wait(10)
#
# browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div/div/div/div/div[2]/span[2]/span/div').click()