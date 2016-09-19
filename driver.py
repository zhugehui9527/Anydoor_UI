# -*- coding:utf-8 -*-
from appium import webdriver
import os

class driver():
    def __init__(self):
        desired_caps = {}
        desired_caps['bundleId'] = 'com.pingan.rympush'
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3'
        desired_caps['deviceName'] = 'iPhone 5s'
        # desired_caps['app'] = os.path.abspath('/usr/local/anydoor/app_package/PAAnydoorSDK_New.ipa')
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(60)

    def get_driver(self):
        return self.driver