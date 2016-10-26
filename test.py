# -*- coding:utf-8 -*-
from appium import webdriver
import unittest
import HTMLTestRunner
import os,time

class UI(unittest.TestCase):
	def setUp(self):
		desired_caps = {}
		desired_caps['bundleId'] = 'com.pingan.rympush'
		desired_caps['platformName'] = 'iOS'
		desired_caps['platformVersion'] = '9.3'
		desired_caps['deviceName'] = 'iPhone 5s'
		desired_caps['autoLaunch'] = 'true'  # 是否自动启动
		# desired_caps['app'] = os.path.abspath('/usr/local/anydoor/app_package/PAAnydoorSDK_New.ipa')
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(60)

	def tearDown(self):
		self.driver.quit()

	def testLogin(self):
		self.driver.find_element_by_id('一账通').click()
		self.driver.find_element_by_id('宿主登陆').click()
		self.driver.find_element_by_id('选择登陆用户').click()
		self.driver.find_element_by_id('确认').click()
		self.driver.find_element_by_id('登陆').click()
		self.assertTrue(self.driver.find_element_by_id('登陆').is_enabled())
		# self.driver.find_element_by_id().is_enabled()
		# self.driver.find_element_by_id().is_displayed()

if __name__ == "__main__":
	current_path = os.getcwd()
	timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
	report_path = '\\Users\\zengyuanchen\\Documents\\Project\\Anydoor_UI\\src\\'+ timestr +'_report.html'
	# report_path = current_path + '/'+'report.html'
	suit = unittest.makeSuite()
	suit.addTest(UI('testLogin'))
	ReportObject = open(report_path, "wb")
	testRunner = HTMLTestRunner.HTMLTestRunner(stream=ReportObject, title='Report', description='IOS')
	testRunner.run(suit)
	ReportObject.close()