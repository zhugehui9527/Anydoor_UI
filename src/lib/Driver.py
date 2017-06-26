# -*- coding:utf-8 -*-
#######################################################
#filename:Driver.py
#author:Jeff
#date:2016-09-21
#function:对Driver进行操作处理
#######################################################
import time
from appium import webdriver
from macaca import WebDriver as WD
from conf.Run_conf import read_config
from src.Public.Common import desired_caps as dc
from src.Public.Common import  public as pc
from src.Public.Common import platform as pf
from src.Public.Global import L,S

class Driver(object):
    def __init__(self,device,port):
        self.device =  device
        self.port = port

    def init(self):
        try:
            self.runmode = read_config(pc.runmode, pc.driver)
            self.bundleId = read_config(pc.appium, dc.bundleId)
            self.platformName = self.device[dc.platformName]
            self.app = read_config(pc.appium, dc.app)
            self.appActivity = read_config(pc.appium, dc.appActivity)
            self.noReset = read_config(pc.appium, dc.noReset)
            self.autoAcceptAlerts = read_config(pc.appium, dc.autoAcceptAlerts)
            self.unicodeKeyboard = read_config(pc.appium, dc.unicodeKeyboard)
            self.resetKeyboard = read_config(pc.appium, dc.resetKeyboard)
            self.newCommandTimeout = read_config(pc.appium, dc.newCommandTimeout)
            self.automationName = read_config(pc.appium, dc.automationName)
            self.udid = S.device[dc.udid]
            self.device[dc.udid] = self.udid
            if self.runmode == pc.macaca:
                self.ip = read_config(pc.macaca, dc.hostname)
                self.reuse = read_config(pc.macaca, dc.reuse)
                self.url = {'hostname':'localhost','port':self.port}
            else:
                self.ip = read_config(pc.appium, dc.ip)
                self.appPackage = read_config(pc.appium, dc.appPackage)
                self.device[dc.newCommandTimeout] = self.newCommandTimeout
                self.device[dc.noReset] = self.noReset
                self.device['useNewWDA'] = 'true'
                self.device['wdaLocalPort'] = str(int(self.port) + 3000)
                self.device['commandTimeouts'] = '120000'
                # self.device['xcodeConfigFile'] = '/Users/zengyuanchen/Documents/Project/appium-xcuitest-driver/appium-xcuitest-driver/WebDriverAgent/WebDriverAgent.xcodeproj'
                self.url = 'http://' + str(self.ip) + ':' + str(self.port) + '/wd/hub'

            # self.url = 'http://' + str(self.ip) + ':' + str(self.port) + '/wd/hub'
            # self.url = 'http://' + str(self.ip) + ':8900/wd/hub'


            # print time.ctime(), ' [', __name__, '::', Driver.init.__name__, '] :', ' platformName =  ', self.platformName

            if self.platformName.lower() == pf.android:
                self.device[dc.appActivity] = self.appActivity
                self.device[dc.app] =self.app
                if self.runmode == pc.appium:
                    self.device[dc.unicodeKeyboard] = self.unicodeKeyboard
                    self.device[dc.resetKeyboard] = self.resetKeyboard
                    self.device[dc.appPackage] = self.appPackage
                    self.device[dc.autoAcceptAlerts] = self.autoAcceptAlerts
                # self.device[dc.autoWebview] = self.autoWebview

            elif self.platformName.lower() == pf.ios:
                # self.device[dc.platformVersion] = self.platformVersion
                self.device[dc.bundleId] = self.bundleId
                if self.runmode == pc.appium:
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

        if self.runmode == pc.macaca:
            L.logger.info('启动并获取macaca driver对象')
            self.driver = WD(self.device,url=self.url)
            self.driver.init()

        else:
            L.logger.info('启动并获取appium driver对象')
            self.driver = webdriver.Remote(self.url, self.device)
        L.logger.info('session_id: %s',self.driver.session_id)
        if self.driver.session_id:
            return self.driver
        else:
            raise ValueError,'设备未连接或者设备未启动,请检查设备配置'



# if __name__ == '__main__':
#     # device = {'udid': '32E6D124-29B6-48A2-9B38-0A9D54121E10', 'deviceName': 'iPhone6s', 'platformName': 'iOS', 'platformVersion': '10.2'}
#     device =  {'udid': '0316032597351f04', 'deviceName': 'Android', 'platformName': 'Android'}
#     port = '4723'
#     D = Driver(device,port)
#     D.init()
#     driver = D.getDriver()
