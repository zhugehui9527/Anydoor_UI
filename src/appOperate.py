# -*- coding:utf-8 -*-
#######################################################
#filename:driver.py
#author:Jeff
#date:2016-09-21
#function:对日志进行操作处理
#######################################################
from Element import *
from Public.Public import *
import time,datetime

class appOperate():
	def __init__(self):
		# at = driver()
		# self.driver = at.get_driver()
		self.driver = Element()
		iOS_UserName = "//*[@value='一账通号/手机号/身份证号/邮箱']"
		iOS_PassWord = "//*[@value='密码']"
		Andr_UserName = "com.paic.example.simpleapp:id/user-id-input"
		Andr_PassWord = "com.paic.example.simpleapp:id/user-psd-input"
		config_path = '/Users/zengyuanchen/Documents/Project/Anydoor_UI/conf/monitor.ini'
		platformName = read_config(config_path, 'appium', 'platformName')
		self.platformName = platformName
		self.iOS_UserName = iOS_UserName
		self.iOS_PassWord = iOS_PassWord
		self.Andr_UserName = Andr_UserName
		self.Andr_PassWord = Andr_PassWord



	def wait_for_text(self,time_second,text):
		self.driver.load_page_timeout(time_second)
		pageSource = self.driver.page_source
		if text in pageSource:
			assert True
		else:
			assert False

	def loginByHost(self):
		try:
			self.driver.implicitly_wait(3)
			self.driver.by_id("一账通").click()
			self.driver.implicitly_wait(3)
			self.driver.by_id("宿主登陆").click()
			#"//UIAPickerWheel"
			# self.driver.send_keys(self.driver.by_name(''),'rymtest001')
			# self.driver.by_xpath("//UIAPickerWheel")
			self.driver.implicitly_wait(3)
			self.driver.by_id("选择登陆用户").click()
			self.driver.implicitly_wait(3)
			self.driver.by_id("确认").click()
			self.driver.implicitly_wait(3)
			self.driver.by_id("登陆").click()
			self.driver.implicitly_wait(8)
		except Exception,e:
			raise e

	def loginOut(self):
		try:
			self.driver.implicitly_wait(3)
			self.driver.by_id("无用户").click()
		except:
			raise

	#支持iOS和Android
	def loginByH5(self,userName,passWord):
		self.driver.implicitly_wait(3)
		self.driver.by_id("个人中心").click()
		if self.platformName.lower() =='ios':
			try:
				self.driver.implicitly_wait(3)
				#填写账号
				self.driver.by_xpath(self.iOS_UserName).click()
				self.driver.implicitly_wait(3)
				self.driver.by_xpath(self.iOS_UserName).clear()
				self.driver.implicitly_wait(3)
				self.driver.by_xpath(self.iOS_UserName).send_keys(userName)
				#填写密码
				self.driver.implicitly_wait(3)
				self.driver.by_xpath(self.iOS_PassWord).click()
				self.driver.implicitly_wait(3)
				self.driver.by_xpath(self.iOS_PassWord).clear()
				self.driver.implicitly_wait(3)
				self.driver.by_xpath(self.iOS_PassWord).send_keys(userName)
				self.driver.implicitly_wait(3)
				self.driver.by_id('登 录').click()

			except Exception,e:
				raise e
		elif self.platformName.lower() =='android':
			try:
				self.driver.implicitly_wait(3)
				# 填写账号
				self.driver.by_xpath(self.Andr_UserName).click()
				self.driver.implicitly_wait(3)
				self.driver.by_xpath(self.Andr_UserName).clear()
				self.driver.implicitly_wait(3)
				self.driver.by_xpath(self.Andr_UserName).send_keys(userName)
				# 填写密码
				self.driver.implicitly_wait(3)
				self.driver.by_xpath(self.Andr_PassWord).click()
				self.driver.implicitly_wait(3)
				self.driver.by_xpath(self.Andr_PassWord).clear()
				self.driver.implicitly_wait(3)
				self.driver.by_xpath(self.Andr_PassWord).send_keys(userName)
				self.driver.implicitly_wait(3)
				self.driver.by_id('登 录').click()
			except Exception, e:
				raise e
		else:
			print '请在配置文件中添加正确的platformName!!'

	def check_plugin(self, pluginName, expectResult):
		a = 0
		if appOperate.wait_for_text(3,pluginName):
			print "找到插件,准备点击!"
		else:
			try:
				print "没找到插件,准备滑动查找!"
				if a >=1:
					self.driver.swipe_right()
					a = 0
				else:
					self.driver.swipe_left()
					a = a+1
			except:
				raise


