# coding: utf-8

__author__ = 'Yemilice_lau'


from selenium import webdriver
import time


browser = webdriver.Chrome()

browser.get("http://10.0.9.28")

time.sleep(2)


# 输入帐号密码
browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[3]/div/div[2]/span[1]/input').send_keys("admin")
browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[3]/div/div[2]/span[2]/input').send_keys("123456")

# 点击登录
browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[3]/div/div[2]/span[2]/span[2]').click()

browser.implicitly_wait(3)

browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/div[2]/div[8]/img').click()

browser.implicitly_wait(3)

print(browser.current_url)

browser.refresh()

browser.switch_to.frame("dt_infinity_iframe")

browser.find_element_by_xpath('//*[@id="pool-mgm-act"]').click()

browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/a/span').click()

browser.find_element_by_xpath('//*[@id="createDiskGroupModal"]/div/div/div[2]/form/div[1]/div/input').send_keys("test_123")

browser.implicitly_wait(5)

browser.find_element_by_xpath('//*[@id="createDiskGroupModal"]/div/div/div[2]/form/div[4]/div/a').click()

browser.implicitly_wait(10)

boxs = browser.find_elements_by_xpath('//*[@id="checkNasNode"]')

for i in range(len(boxs)):
    boxs2 = browser.find_element_by_xpath('//*[@id="checkNasNode"]/div[{id}]/label/input'.format(id=i+1)).click()

time.sleep(5)

browser.implicitly_wait(5)

browser.find_element_by_xpath('//*[@id="addHostModal"]/div/div/div[1]/button[2]').click()

time.sleep(5)

browser.implicitly_wait(5)

browser.find_element_by_xpath('//*[@id="createDiskGroupModal"]/div/div/div[2]/form/div[4]/div[2]/a').click()

time.sleep(5)

browser.implicitly_wait(5)
# boxs2 = browser.find_element_by_xpath('//*[@id="checkNasNode"]/div[{id}]/label/input'.format(id=0)).click()
browser.find_element_by_xpath('//*[@id="addnodedisk"]/table/thead/tr/th[6]/input').click()

time.sleep(5)

browser.implicitly_wait(5)

browser.find_element_by_xpath('//*[@id="selectDiskModal"]/div/div/div[1]/button[2]').click()

time.sleep(5)

browser.implicitly_wait(5)

browser.find_element_by_xpath('//*[@id="createDiskGroupModal"]/div/div/div[1]/button[2]').click()

time.sleep(5)


browser.close()
