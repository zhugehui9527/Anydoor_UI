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
        print "开始宿主一账通登录。。。"
        self.driver.by_name("一账通").click()
        self.driver.by_name("宿主登陆").click()
        self.driver.by_name("选择登陆用户").click()
        self.driver.by_name("确认").click()
        self.driver.implicitly_wait(30)

if __name__=='__main__':
    unittest.main()