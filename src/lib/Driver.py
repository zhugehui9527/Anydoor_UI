# -*- coding:utf-8 -*-
#######################################################
#filename:Driver.py
#author:Jeff
#date:2016-09-21
#function:对日志进行操作处理
#######################################################
import threading
import subprocess
import requests,json
from urllib2 import URLError
from appium import webdriver
from conf.Run_conf import read_config
from src.Public.AppiumServer import AppiumServer
from selenium.common.exceptions import WebDriverException

  
"""
class MyDriver:
    global desired_caps,serverurl
    driver = None
    mutex = threading.Lock()
    ip = read_config('appium', 'ip')
    port = read_config('appium', 'port')
    bundleId = read_config('appium', 'bundleId')
    platformName = read_config('appium', 'platformName')
    platformVersion = read_config('appium', 'platformVersion')
    deviceName = read_config('appium', 'deviceName')
    noReset = read_config('appium', 'noReset')
    automationName = read_config('appium', 'automationName')
    app = read_config('appium', 'app')
    autoAcceptAlerts = read_config('appium', 'autoAcceptAlerts')
    unicodeKeyboard = read_config('appium','unicodeKeyboard')
    resetKeyboard = read_config('appium', 'resetKeyboard')
    autoWebview = read_config('appium', 'autoWebview')
    
    desired_caps = {}
    desired_caps['noReset'] = noReset
    desired_caps['autoAcceptAlerts'] = autoAcceptAlerts #弹窗自动确认关闭
    desired_caps['bundleId'] = bundleId
    desired_caps['platformName'] = platformName
    desired_caps['platformVersion'] = platformVersion
    desired_caps['deviceName'] = deviceName
    
    if platformName.lower() == 'android':
        desired_caps['unicodeKeyboard'] = unicodeKeyboard
        desired_caps['resetKeyboard'] = resetKeyboard
        desired_caps['autoWebview'] = autoWebview
    elif platformName.lower() == 'ios':
        desired_caps['automationName'] = automationName
        # desired_caps['autoLaunch'] = 'True'
    else:
        pass
    
    serverurl = 'http://' + ip + ':' + port + '/wd/hub'

    def _init__(self):
        pass

    @staticmethod
    def get_driver():
        try:
            if MyDriver.driver is None:
                MyDriver.mutex.acquire()

                if MyDriver.driver is None:

                    try:
                        MyDriver.driver = webdriver.Remote(serverurl,desired_caps)
                    except URLError:
                        MyDriver.driver = None

                MyDriver.mutex.release()

            return MyDriver.driver
        except WebDriverException:
            raise
  
    def is_runnnig(self):
        response = None
        url = self.serverurl + "/status"
        try:
            # response = urllib2.request_host(url)
            # response = urllib.request.urlopen(url, timeout=5)
            response = requests.get(url)
            response_dict = json.loads(response.text)
            if response_dict['status']== 0:
                return True
            else:
                return False
        except URLError:
            return False
        finally:
            if response:
                response.close()



class Singleton(object):
    '''
    #方法,实现__new__方法
    #并在将一个类的实例绑定到类变量_instance上,
    #如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回
    #如果cls._instance不为None,直接返回cls._instance
    '''
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class Borg(object):
    '''
    #方法2,共享属性;所谓单例就是所有引用(实例、对象)拥有相同的状态(属性)和行为(方法)
#同一个类的所有实例天然拥有相同的行为(方法),
#只需要保证同一个类的所有实例具有相同的状态(属性)即可
#所有实例共享属性的最简单最直接的方法就是__dict__属性指向(引用)同一个字典(dict)
#可参看:http://code.activestate.com/recipes/66531/
    '''
    _state = {}
    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob
"""
# config_path = '/Users/zengyuanchen/Documents/Project/Anydoor_UI/conf/monitor.ini'

class Driver(object):
    '''单例模式'''

    def __new__(cls,devices,port):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Driver, cls).__new__(cls)
            # cls.instance.ip = read_config( 'appium', 'ip')
            # cls.instance.bundleId = read_config( 'appium', 'bundleId')
            # cls.instance.serverurl = 'http://' + cls.instance.ip + ':' + str(port) + '/wd/hub'
            cls.instance.desired_caps = {}
            cls.instance.devices = devices
            cls.instance.port = port
        return cls.instance
    
    def init(self):
        self.ip = read_config('appium', 'ip')
        # self.port = read_config('appium', 'port')
        self.bundleId = read_config('appium', 'bundleId')
        self.platformName = read_config('appium', 'platformName')
        self.platformVersion = read_config('appium', 'platformVersion')
        self.deviceName = read_config('appium', 'deviceName')
        self.noReset = read_config('appium', 'noReset')
        self.automationName = read_config('appium', 'automationName')
        self.app = read_config('appium', 'app')
        self.autoAcceptAlerts = read_config('appium', 'autoAcceptAlerts')
        self.unicodeKeyboard = read_config('appium', 'unicodeKeyboard')
        self.resetKeyboard = read_config('appium', 'resetKeyboard')
        self.autoWebview = read_config('appium', 'autoWebview')
        self.instance.serverurl = 'http://' + self.ip  + ':' + str(self.port) + '/wd/hub'
    
    
    def getDesired_caps(self):
        # self.init()
        from src.Public.Common import desired_caps as dc
        # self.desired_caps[dc.bundleId] = self.bundleId
        self.desired_caps[dc.noReset] = self.noReset
        self.desired_caps[dc.autoAcceptAlerts] = self.autoAcceptAlerts
        self.desired_caps[dc.bundleId] = self.bundleId
        self.desired_caps[dc.platformName] = self.platformName
        self.desired_caps[dc.platformVersion] = self.platformVersion
        self.desired_caps[dc.deviceName] = self.deviceName
        if self.platformName.lower() == 'android':
            self.desired_caps[dc.unicodeKeyboard] = self.unicodeKeyboard
            self.desired_caps[dc.resetKeyboard] = self.resetKeyboard
            self.desired_caps[dc.autoWebview] = self.autoWebview
            
        elif self.platformName.lower() == 'ios':
            self.desired_caps[dc.automationName] = self.automationName
            
        else:
            pass
        # print '*' * 80
        print '* [',__name__,'::',self.getDesired_caps.__name__,']',self.desired_caps
        print '*' * 80
        return self.desired_caps
         
    def start_driver(self):
        # mutex = threading.Lock()
        # mutex.acquire()  # 上锁,防止多线程下出问题
        try:
            # self.getDesired_caps()
            self.driver = webdriver.Remote(self.serverurl,self.getDesired_caps())
            # print '*' * 80
            print '[ driver 启动]'
            print '*' * 80
            return self.driver
        except URLError:
            raise
        # mutex.release()  # 释放锁
         
        

    def get_driver(self):
        return self.start_driver

    def is_runnnig(self):
        """
        Determine whether server is running
        :return:True or False
            """
        response = None
        url = self.serverurl + "/status"
        try:
            # response = urllib2.request_host(url)
            # response = urllib.request.urlopen(url, timeout=5)
            response = requests.get(url)
            response_dict = json.loads(response.text)
            if response_dict['status']== 0:
                return True
            else:
                return False
        except URLError:
            return False
        finally:
            if response:
                response.close()




if __name__ == '__main__':
    import os,time
    from multiprocessing import Process
    print '启动服务'
    cmd = 'appium -a 127.0.0.1 -p 4723 -bp 4724'
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
 
    # subprocess.Popen('appium -a 127.0.0.1 -p 4723',shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    ddriver = Driver()
    while not ddriver.is_runnnig():
        time.sleep(2)
    print '启动成功'
    # mydriver = MyDriver()
    # driver = mydriver.get_driver()
