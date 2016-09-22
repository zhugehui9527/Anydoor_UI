# -*- coding:utf-8 -*-
#######################################################
#filename:driver.py
#author:Jeff
#date:2016-09-21
#function:对日志进行操作处理
#######################################################
import logging
import os

from appium import webdriver
from src.Public.Public import *
from conf import Run_conf
import sys

class driver():
    def __init__(self):
        config_path = Run_conf.conf_file
        print config_path
        ip = read_config(config_path,'appium','ip')
        port = read_config(config_path,'appium','port')
        bundleId = read_config(config_path,'appium','bundleId')
        platformName = read_config(config_path,'appium','platformName')
        platformVersion = read_config(config_path,'appium','platformVersion')
        deviceName = read_config(config_path,'appium','deviceName')
        app = read_config(config_path,'appium','app')
        try :
            desired_caps = {}
            desired_caps['bundleId'] = bundleId
            desired_caps['platformName'] = platformName
            desired_caps['platformVersion'] = platformVersion
            desired_caps['deviceName'] = deviceName
            # desired_caps['app'] = os.path.abspath(app')
            serverIp= 'http://' + ip + ':' + port + '/wd/hub'
            self.driver = webdriver.Remote(serverIp, desired_caps)
        except Exception as e:
            logging.exception(e)
            raise
        # desired_caps = {}
        # desired_caps['bundleId'] = 'com.pingan.rympush'
        # desired_caps['platformName'] = 'iOS'
        # desired_caps['platformVersion'] = '9.3'
        # desired_caps['deviceName'] = 'iPhone 5s'
        # # # desired_caps['app'] = os.path.abspath('/usr/local/anydoor/app_package/PAAnydoorSDK_New.ipa')
        # # self.driver = webdriver.Remote('http://'+ ip + ":" + port +'/wd/hub', desired_caps)
        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(60)

    def get_driver(self):
        return self.driver