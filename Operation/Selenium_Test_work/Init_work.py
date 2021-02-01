# coding: utf-8

__author__ = 'Yemilice_lau'



from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By

# 初始化的步骤
class InitInfinity:
    def __init__(self, url, ip):
        self.url = url
        self.ip = ip
        self.browser = webdriver.Chrome()

    # 访问指定的网页
    def GetWebsite(self):
        try:
            self.browser.get(self.url)
        except:
            self.browser.quit()

    # 输入IP
    def EnterIP(self):
        # wait 10s
        self.WaitWork()
        try:
            self.browser.find_element_by_class_name("ant-input").send_keys(self.ip)
        except:
            self.browser.quit()

    # 键入ip
    def InputWait(self):
        try:
            input = self.browser.find_element_by_class_name("ant-input")
            input.send_keys(Keys.ENTER)
        except:
            self.browser.quit()

    # IP等待元素消失,20s，大概
    def IPWait(self, timeout=20):
        try:
            ui.WebDriverWait(self.browser, timeout).until_not(EC.visibility_of_element_located((By.CLASS_NAME, "ant-empty-description")))
        except:
            self.browser.quit()

    # inter manager 全点击，第一个
    def InterManager(self):
        self.WaitWork()
        num = len(self.ip.split(','))

        # 拼凑内部管理网络的xpath
        for i in range(1, num+1):
            xpath = '//*[@id="app"]/div/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[{num}]/div[1]/div[2]/div'.format(num=i)
            self.browser.find_element_by_xpath(xpath).click()
            clickxpath = '/html/body/div[{num}]/div/div/div/div[2]/div/div/div/div[2]'.format(num= 2 + i)
            self.browser.find_element_by_xpath(clickxpath).click()


    # 数据平面网络设置
    def DataPlaneManager(self):
        # 同上
        self.WaitWork()
        num = len(self.ip.split(','))
        for i in range(1, num+1):
            xpath = '//*[@id="app"]/div/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[{num}]/div[1]/div[3]/div'.format(num=i)
            self.browser.find_element_by_xpath(xpath).click()
            clickxpath = '/html/body/div[{num}]/div/div/div/div[2]/div/div/div/div[1]'.format(num= 5 + i)
            self.browser.find_element_by_xpath(clickxpath).click()
        # pass

    # 外部访问网络
    def ExternalInterManager(self):
        # 同上
        self.WaitWork()
        num = len(self.ip.split(','))
        for i in range(1, num+1):
            xpath = '//*[@id="app"]/div/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[{num}]/div[1]/div[4]/div'.format(num=i)
            self.browser.find_element_by_xpath(xpath).click()
            clickxpath = '/html/body/div[{num}]/div/div/div/div[2]/div/div/div/div[1]'.format(num= 5 + i)
            self.browser.find_element_by_xpath(clickxpath).click()

    # 帐号密码
    def SendPassword(self):
        self.WaitWork()
        password = "123456"
        self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div[3]/div[1]/div[2]/div[3]/div/div/input').send_keys(password)
        self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div[3]/div[1]/div[2]/div[4]/div/div/input').send_keys(password)

    # 下一步 next
    def Next(self):
        self.browser.find_element_by_class_name("arrow-right").click()

    # 等待元素
    def WaitWork(self):
        self.browser.implicitly_wait(10)

    #start 开始
    def start(self):
        self.WaitWork()
        self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/span[2]/button/span[1]').click()


if __name__ == '__main__':
    p = InitInfinity("http://10.0.8.72/#/infinity/setup", "2001:db8:1:8:8fa6:20f4:aeb:8e25,2001:db8:1:8:8fa6:20f4:aeb:8e92,2001:db8:1:8:f816:3eff:fe35:4940")
    p.GetWebsite()
    p.EnterIP()
    p.InputWait()
    p.IPWait()
    p.Next()
    p.InterManager()
    p.ExternalInterManager()
    p.Next()
    p.SendPassword()
    p.Next()
    p.start()