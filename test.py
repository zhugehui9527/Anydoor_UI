# -*- coding:utf-8 -*-
from appium import webdriver
from appium.webdriver.common import mobileby
from selenium.webdriver.common.by import By
import unittest
import HTMLTestRunner
import os,time

class UI(unittest.TestCase):
	def setUp(self):
		desired_caps = {}
		desired_caps['bundleId'] = 'com.pingan.rympush'
		desired_caps['platformName'] = 'iOS'
		desired_caps['platformVersion'] = '10.1'
		desired_caps['deviceName'] = 'iPhone 5s'
		desired_caps['noReset'] = 'True'
		# desired_caps['autoLaunch'] = 'true'  # 是否自动启动
		# desired_caps['app'] = os.path.abspath('/usr/local/anydoor/app_package/PAAnydoorSDK_New.ipa')
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(60)

	def tearDown(self):
		self.driver.quit()

	def testLogin(self):
		# self.driver.find_element_by_id('一账通').click()
		# self.driver.find_element_by_id('宿主登陆').click()
		# self.driver.find_element_by_id('选择登陆用户').click()
		# self.driver.find_element_by_id('确认').click()
		# self.driver.find_element_by_id('登陆').is_displayed()
		# self.driver.find_element_by_class_name()
		# self.driver.find_element_by_ios_uiautomation()
		self.driver.close_app()
		print self.driver.current_context()
		print self.driver.contexts()
		print self.driver.context()
		



		# WebDriverWait(self.driver, 20).until(lambda x: self.driver.find_element_by_id('宿主登陆'))
		# self.assertTrue(self.driver.find_element_by_id('登陆').is_enabled())
		# print 'get_screenshot_as_base64: ',self.driver.get_screenshot_as_base64()
		# print 'current_url: ',self.driver.current_url
		# print 'page_source: ',self.driver.page_source
		# self.driver.find_element_by_id().is_enabled()
		# self.driver.find_element_by_id().send_keys()

if __name__ == "__main__":
	current_path = os.getcwd()
	timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
	report_path =current_path+ timestr +'_report.html'
	# report_path = current_path + '/'+'report.html'
	loader = unittest.TestLoader()
	suite = loader.loadTestsFromTestCase(UI)
	ReportObject = open(report_path, "wb")
	testRunner = HTMLTestRunner.HTMLTestRunner(stream=ReportObject, title='Report', description='IOS')
	testRunner.run(suite)
	ReportObject.close()