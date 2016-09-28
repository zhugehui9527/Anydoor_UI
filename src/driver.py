# -*- coding:utf-8 -*-
#######################################################
#filename:driver.py
#author:Jeff
#date:2016-09-21
#function:对日志进行操作处理
#######################################################
import os
from appium import webdriver
from src.Public.Public import *
from conf.Run_conf import *
import threading
from urllib2 import URLError
import urllib,urllib2
from Global import *
import sys


class appdriver:
    config_path = '/Users/zengyuanchen/Documents/Project/Anydoor_UI/conf/monitor.ini'
    ip = read_config(config_path, 'appium', 'ip')
    port = read_config(config_path, 'appium', 'port')
    bundleId = read_config(config_path, 'appium', 'bundleId')
    platformName = read_config(config_path, 'appium', 'platformName')
    platformVersion = read_config(config_path, 'appium', 'platformVersion')
    deviceName = read_config(config_path, 'appium', 'deviceName')
    app = read_config(config_path, 'appium', 'app')

    desired_caps = {}
    desired_caps['bundleId'] = bundleId
    desired_caps['platformName'] = platformName
    desired_caps['platformVersion'] = platformVersion
    desired_caps['deviceName'] = deviceName
    # desired_caps['app'] = os.path.abspath(app')
    serverIp = 'http://' + ip + ':' + port + '/wd/hub'
    driver = None
    mutex = threading.Lock()


    def __init__(self):
        pass
        # desired_caps = {}
        # desired_caps['bundleId'] = 'com.pingan.rympush'
        # desired_caps['platformName'] = 'iOS'
        # desired_caps['platformVersion'] = '9.3'
        # desired_caps['deviceName'] = 'iPhone 5s'
        # # # desired_caps['app'] = os.path.abspath('/usr/local/anydoor/app_package/PAAnydoorSDK_New.ipa')
        # # self.driver = webdriver.Remote('http://'+ ip + ":" + port +'/wd/hub', desired_caps)
        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    @staticmethod
    def get_driver():
        try:
            if appdriver.driver is None:
                # 加锁
                appdriver.mutex.acquire()

                # if appdriver.driver is None:
                try:
                    print appdriver.serverIp
                    print appdriver.desired_caps
                    appdriver.driver = webdriver.Remote(appdriver.serverIp,appdriver.desired_caps)
                    print appdriver.driver
                except URLError:
                    appdriver.driver = None
                #释放锁
                appdriver.mutex.release()
                return appdriver.driver
        except Exception:
            raise


    def is_runnnig(self):
        """Determine whether server is running
            :return:True or False
            """
        response = None
        url = appdriver.serverIp + "/status"
        try:
            response = urllib2.request_host(url)
            # response = urllib.request.urlopen(url, timeout=5)
            if str(response.getcode()).startswith("2"):
                return True
            else:
                return False
        except URLError:
            return False
        finally:
            if response:
                response.close()





# class Mydriver:
#     """
#     This class is used to get log
#     lock log
#     """
#
#     driver = None
#     mutex = threading.Lock()
#
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def getdriver():
#
#         if Mydriver.driver is  None:
#
#             Mydriver.mutex.acquire()
#             Mydriver.driver = appdriver().get_driver()
#             Mydriver.mutex.release()
#
#         return Mydriver.driver


if __name__ == '__main__':

    dd = appdriver.is_runnnig()
    if dd:
        print 'ss'