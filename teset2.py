# -*- coding:utf-8 -*-
import src.Public.Log as Log
import urllib2
import requests
import json
import logging

from appium import webdriver

log = Log.LogSignleton()
log.logger.debug('test')
# loggers = logging.getLogger('test')
# loggers.debug('检查appium服务是否启动')
url ='http://127.0.0.1:4723/wd/hub'
response_re = requests.get(url+'/status')
print '开始前状态:',response_re.text
desired_caps = {}
desired_caps['bundleId'] = 'com.pingan.rympush'
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '9.3'
desired_caps['deviceName'] = 'iPhone 5s'
# webdriver.Remote(url,desired_caps)

# response = urllib2.urlopen(url+'/status')
response_text = response_re.text
response_dict = json.loads(response_text)
print response_dict
# response_re = requests.get(url)
print '开始后状态',response_dict['status']