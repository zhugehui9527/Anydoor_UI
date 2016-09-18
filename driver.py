# -*- coding:utf-8 -*-
from appium import webdriver
import os

class driver():
    def __init__(self):
        desired_caps = {}
        desired_caps['bundleId'] = 'com.niiwoo.test'
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3'
        desired_caps['deviceName'] = 'iPhone 6s'
        desired_caps['app'] = os.path.abspath('/Users/zhanghui/Documents/Finance/NiiWoo-Finance/build/Release-iphonesimulator/Finance.app')
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(60)

    def get_driver(self):
        return self.driver