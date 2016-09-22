# -*- coding:utf-8 -*-
from src.Public.Public import *
from src.Public.logger import Log

project_path = os.getcwd()
config_path = os.path.join((project_path + '/conf/'),'monitor.ini')

print "INFO: ", logging.INFO
print "DEBUG: ", logging.DEBUG
print "WARN: ", logging.WARN
print "Error: ", logging.ERROR
print "CRITICAL: ", logging.CRITICAL





# from appium import webdriver
# # from selenium import webdriver
# class UI(unittest.TestCase):
# 	def setUp(self):
# 		desired_caps = {}
# 		desired_caps['bundleId'] = 'com.pingan.rympush'
# 		desired_caps['platformName'] = 'iOS'
# 		desired_caps['platformVersion'] = '9.3'
# 		desired_caps['deviceName'] = 'iPhone 5s'
# 		desired_caps['autoLaunch'] = 'true'  # 是否自动启动
# 		# desired_caps['app'] = os.path.abspath('/usr/local/anydoor/app_package/PAAnydoorSDK_New.ipa')
# 		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 		self.driver.implicitly_wait(60)
#
# 	def tearDown(self):
# 		self.driver.quit()
#
# 	def testLogin(self):
# 		# self.driver.find_elements_by_tag_name('一账通')
# 		self.driver.find_element_by_id('一账通').click()
# 		self.driver.find_element_by_id('宿主登陆').click()
#
# if __name__ == "__main__":
# 	# suite = unittest.TestLoader().loadTestsFromTestCase(UI)
# 	# unittest.TextTestRunner(verbosity=2).run(suite)  # 执行case集
# 	logging.debug('debug message')