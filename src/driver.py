# -*- coding:utf-8 -*-
#######################################################
#filename:driver.py
#author:Jeff
#date:2016-09-21
#function:对日志进行操作处理
#######################################################
import os
# from src.Public.Public import *
from selenium.common.exceptions import WebDriverException
import threading
import requests,json
from urllib2 import URLError
from appium import webdriver
from conf.Run_conf import read_config
# from Global import conf_path
import urllib,urllib2
import sys


class MyDriver:
    global desired_caps,serverurl
    driver = None
    # conf_path = get_conf_path()
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
    desired_caps = {}
    desired_caps['bundleId'] = bundleId
    desired_caps['platformName'] = platformName
    desired_caps['platformVersion'] = platformVersion
    desired_caps['deviceName'] = deviceName
    desired_caps['automationName'] = automationName
    desired_caps['noReset'] = noReset
    desired_caps['autoAcceptAlerts'] = autoAcceptAlerts #弹窗自动确认关闭
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
        """Determine whether server is running
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



"""
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

class DriverSignleton(object):
    '''单例模式'''
    def __init__(self, config_path):
        pass

    def __new__(cls, config_path):
        mutex = threading.Lock()
        mutex.acquire()  # 上锁,防止多线程下出问题
        if not hasattr(cls, 'instance'):
            cls.instance = super(DriverSignleton, cls).__new__(cls)
            cls.instance.ip = read_config( 'appium', 'ip')
            cls.instance.port = read_config( 'appium', 'port')
            cls.instance.bundleId = read_config( 'appium', 'bundleId')
            cls.instance.platformName = read_config( 'appium', 'platformName')
            cls.instance.platformVersion = read_config( 'appium', 'platformVersion')
            cls.instance.deviceName = read_config( 'appium', 'deviceName')
            cls.instance. app = read_config( 'appium', 'app')

            desired_caps = {}
            desired_caps['bundleId'] = cls.instance.bundleId
            desired_caps['platformName'] = cls.instance.platformName
            desired_caps['platformVersion'] = cls.instance.platformVersion
            desired_caps['deviceName'] = cls.instance.deviceName
            # desired_caps['app'] = os.path.abspath(app')
            cls.instance.serverurl = 'http://' + cls.instance.ip + ':' + cls.instance.port + '/wd/hub'
            cls.instance.desired_caps = desired_caps
            # cls.instance.__start_driver()
            cls.instance.driver = cls.instance.__start_driver()
            cls.config_path = config_path
        mutex.release()  # 释放锁
        return cls.instance


    def __start_driver(self):
        driversignleton = DriverSignleton(self.conf_path)
        if not driversignleton.is_runnnig():
            # # 加锁
            # self.mutex.acquire()

             # if appdriver.driver is None:
            try:
                print self.serverurl
                print self.desired_caps
                self.driver = webdriver.Remote(self.serverurl,self.desired_caps)

                print self.driver
            except URLError:
                self.driver = None
                # #释放锁
                # self.mutex.release()
            return self.driver


    def get_driver(self):
        return self.driver


    def is_runnnig(self):
        """Determine whether server is running
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
    # ddriver = DriverSignleton('/Users/zengyuanchen/Documents/Project/Anydoor_UI/conf/monitor.ini')
    # cc = ddriver.is_runnnig()
    # print cc
    mydriver = MyDriver()
    driver = mydriver.get_driver()
