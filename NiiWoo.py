# -*- coding:utf-8 -*-
import unittest
from driver import driver
from Element import *

class NiiWoo(unittest.TestCase):
    def setUp(self):
        self.driver = Element()
    def tearDown(self):
        self.driver.quit()

    def testLogin(self):
        self.driver.by_name("我").click()
        self.driver.by_name("登录").click()
        self.driver.by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").click()
        self.driver.by_name("清除文本").click()
        self.driver.by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys("13188880011")
        self.driver.by_xpath("//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]").send_keys("test123")
        self.driver.by_name("登 录").click()
if __name__=='__main__':
    unittest.main()