# -*- coding:utf-8 -*-
#######################################################
#filename:Driver.py
#author:Jeff
#date:2016-09-21
#function:对Driver进行操作处理
#######################################################
import time
from appium import webdriver
from conf.Run_conf import read_config
from src.Public.Common import desired_caps as dc
from src.Public.Common import platform as pf
from src.Public.Global import L

class Driver(object):
    def __init__(self,device,port):
        self.device =  device
        self.port = port
    
    def init(self):
        try:
            self.ip = read_config(dc.appium, dc.ip)
            self.bundleId = read_config(dc.appium, dc.bundleId)
            self.platformName = self.device[dc.platformName]
            # self.platformVersion = read_config(dc.appium, dc.platformName)
            self.appPackage = read_config(dc.appium,dc.appPackage)
            self.appActivity = read_config(dc.appium,dc.appActivity)
            self.noReset = read_config(dc.appium, dc.noReset)
            self.automationName = read_config(dc.appium, dc.automationName)
            self.app = read_config(dc.appium, dc.app)
            self.autoAcceptAlerts = read_config(dc.appium, dc.autoAcceptAlerts)
            self.unicodeKeyboard = read_config(dc.appium, dc.unicodeKeyboard)
            self.resetKeyboard = read_config(dc.appium, dc.resetKeyboard)
            # self.autoWebview = read_config(dc.appium, dc.autoWebview)
            self.url = 'http://' + str(self.ip) + ':' + str(self.port) + '/wd/hub'
            
            self.device[dc.noReset] = self.noReset
            self.device[dc.autoAcceptAlerts] = self.autoAcceptAlerts
            # print time.ctime(), ' [', __name__, '::', Driver.init.__name__, '] :', ' platformName =  ', self.platformName
            
            if self.platformName.lower() == pf.android:
                self.device[dc.unicodeKeyboard] = self.unicodeKeyboard
                self.device[dc.resetKeyboard] = self.resetKeyboard
                self.device[dc.appPackage] = self.appPackage
                self.device[dc.appActivity] = self.appActivity
                self.device[dc.app] =self.app
                # self.device[dc.autoWebview] = self.autoWebview
    
            elif self.platformName.lower() == pf.ios:
                # self.device[dc.platformVersion] = self.platformVersion
                self.device[dc.bundleId] = self.bundleId
                self.device[dc.automationName] = self.automationName
            else:
                # print time.ctime(), ' [', __name__, '::', Driver.init.__name__, '] :', '暂不支持的driver设置'
                L.logger.warning('暂不支持的driver设置')
        except Exception as e:
            L.logger.error(e)
            raise e
        else:
            L.logger.info('初始化成功!')
            # print time.ctime(), ' [', __name__, '::', Driver.init.__name__, '] :', ' 初始化成功!'
        
    def getDriver(self):
        L.logger.info('启动并获取driver对象')
        self.driver = webdriver.Remote(self.url, self.device)
        return self.driver



# if __name__ == '__main__':
#     # device = {'udid': '32E6D124-29B6-48A2-9B38-0A9D54121E10', 'deviceName': 'iPhone6s', 'platformName': 'iOS', 'platformVersion': '10.2'}
#     device =  {'udid': '0316032597351f04', 'deviceName': 'Android', 'platformName': 'Android'}
#     port = '4723'
#     D = Driver(device,port)
#     D.init()
#     driver = D.getDriver()