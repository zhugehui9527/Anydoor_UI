# -*- coding:utf-8 -*-
import os
import unittest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = 'Android'
        # desired_caps['app'] ='/usr/local/anydoor/app_package/PAAnydoor.apk'
        desired_caps['appPackage'] = 'com.paic.example.simpleapp'
        desired_caps['appActivity'] = '.SettingActivity'
        # desired_caps['app'] ='/usr/local/anydoor/app_package/paanydoor-3.8.0.40.apk'
        

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()
        
        
    def find_element(self,loc,wait=30):
        try:
            WebDriverWait(self.driver, wait).until(lambda driver: driver.find_element(*loc).is_displayed())
            print '查找元素: ' , loc
            return self.driver.find_element(*loc)
        except Exception :
            print '未找到元素'

    def test_add_contacts(self):
        try:
            sz =self.driver.get_window_size()
            width = sz.get('width')
            height = sz.get('height')
            print '获取窗口大小: ',(width,height)
            # 向上滑动
            # self.driver.swipe(width / 2, height * 2/4, 0, height * 1/4, 1000)
            sleep(5)
            self.driver.swipe(width / 2, height * 7 / 8, width / 2, height * 1 / 8, 1000)
            print '上滑动'
            self.driver.implicitly_wait(3)
            
            el = self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'loading')]")
            el.click()
            print '点击设置 loading'
            # sleep(5)
            print self.driver.contexts
            print '打印上下文'
            # com.paic.example.simpleapp:id/tableRow11
            print '当前上下文: ',self.driver.current_context
            # 向右滑动
            self.driver.swipe(width / 10, height * 9 / 10, width * 6 / 10, height * 9 / 10, 1000)
            print '向右滑动'
            # try:
            #     self.driver.swipe(width * 1/20, height * 18/20, width * 2/5, 0,1000)
            #     print 'swipe (%d,%d) (%d,%d)' % (width * 1/20, height * 18/20,width * 2/5, 0)
            # except Exception as e:
            #     print e

            # sleep(8)
            self.find_element((By.XPATH,"//android.widget.TextView[contains(@text,'个人中心')]"),15).click()
            print '个人中心'
            # self.find_element((By.CLASS_NAME,"//android.widget.TextView[contains(@text,'个人中心')]"),15).click()

            # self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'个人中心')]").click()
            print '当前上下文: ', self.driver.current_context
            # sleep(15)
            # self.driver.find_elements_by_class_name('android.widget.EditText')[0].send_keys('18602753065')
            # self.driver.find_element_by_accessibility_id('user-id-input').send_keys('18602753065')
            # self.driver.find_element_by_id('user-id-input').send_keys('18602753065')
            # sleep(5)
            # self.driver.find_element_by_accessibility_id()
            self.find_element((By.ID,'user-id-input'),30).send_keys('18602753065')
            print '输入账号'
            # self.driver.find_element_by_xpath("//android.widget.EditText[@contains(text,'一账通号/手机号/身份证号/邮箱')]").send_keys('18602753065')
            # sleep(3)
            # self.driver.find_elements_by_class_name('android.widget.EditText')[1].send_keys('qweqwe123')
            # sleep(5)
            self.find_element((By.ID,'user-psd-input'),20).send_keys('qweqwe123')
            print '输入密码'
            # self.driver.find_element_by_xpath("//android.widget.EditText[@contains(text,'密码')]").send_keys('qweqwe123')
            # sleep(3)
            self.find_element((By.ID,'login-button'),10).click()
            print '点击登录'

            print self.driver.page_source
            print  'page_source'
            sleep(3)
            # 关闭H5 com.paic.example.simpleapp:array/user_system
            self.find_element((By.ID, 'com.paic.example.simpleapp:array/user_system'), 30).click()
            print '关闭H5'

            sleep(3)
            # 右滑动
            self.driver.swipe(width * 9 / 10, height * 9 / 10, width * 1 / 10, height * 9 / 10, 1000)
            print '右滑动'
            sleep(5)
            pluginId = 'PA01100000000_02_YYG'
            ele_xpath =  "//android.view.ViewGroup[contains(@content-desc,'{}')]".format(pluginId)
            print 'xpath = ',ele_xpath
            self.find_element((By.XPATH,ele_xpath),30).click()
            print '点击插件: ',pluginId
            sleep(10)
            # try:
            #     self.find_element((By.ID,'PA01100000000_02_YYG'),10).click()
            #     print 'by ID'
            # except:
            #     print 'by xpath'
            #     self.find_element((By.XPATH,"//android.view.ViewGroup[contains(@content-desc,'PA01100000000_02_YYG')]"),10).click()
            #
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
