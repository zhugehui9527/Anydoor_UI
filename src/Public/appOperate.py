# -*- coding:utf-8 -*-
#######################################################
#filename:self.Driver.py
#author:Jeff
#date:2016-09-21
#function:对日志进行操作处理
#######################################################
import json
import os
import re
import sys
import time
import requests

from conf.Run_conf import read_config
from src.Public.Global import L,S
from src.Public.Common import desired_caps as Dc
from src.Public.Common import platform as pf
from src.lib.Element import Element
from selenium.webdriver.common.by import By

reload(sys)
sys.setdefaultencoding('utf-8')

class AppOperate (object):
	def __init__(self,driver):
		iOS_UserName = "//*[@value='一账通号/手机号/身份证号/邮箱']"
		iOS_PassWord = "//*[@value='密码']"
		Andr_UserName = "user-id-input"
		Andr_PassWord = "user-psd-input"
		self.pluginURL = read_config('plugin', 'plugin_url_iOS')
		self.platformName = S.device['platformName']
		self.iOS_UserName = iOS_UserName
		self.iOS_PassWord = iOS_PassWord
		self.Andr_UserName = Andr_UserName
		self.Andr_PassWord = Andr_PassWord
		self.driver = Element(driver)
		self.pluginList =[]
		
	
	def loginByHost(self):
		'''
		一账通登陆
		:return:True
		'''
		try:
			if self.platformName.lower() == pf.ios:
				self.driver.by_id("一账通").click()
				time.sleep(3)
				self.driver.by_id("宿主登陆").click()
				time.sleep(3)
				self.driver.by_id("选择登陆用户").click()
				time.sleep(3)
				self.driver.by_id("确认").click()
				time.sleep(3)
				self.driver.by_id("登陆").click()
				time.sleep(3)
			else:
				# TODO 待添加Android
				L.logger.info('待添加Android')

		except Exception as e:
			L.logger.warning(e)

	def loginOut(self):
		'''
		注销登陆
		:return: True
		'''
		try:
			if str(S.device[Dc.platformName]) == pf.ios:
				self.driver.by_id("无用户").click()
			else:
				self.driver.by_id('rb_no_user').click()
			return True
		except Exception as e:
			L.logger.warning(e)
			return False
		
	#支持iOS和Android
	def loginByH5(self,userName,passWord):

		if self.platformName.lower() == pf.ios:
			try:
				self.driver.swipe_right()  # 右滑动
				time.sleep(3)
				self.driver.by_id("个人中心").click()
				time.sleep(3)
				self.driver.by_xpath(self.iOS_UserName).send_keys(userName)
				time.sleep(3)
				L.logger.info('输入账号: %s' % userName)
				# 收起键盘
				self.driver.by_id('完成').click()
				time.sleep(3)
				self.driver.by_xpath(self.iOS_PassWord).send_keys(passWord)
				time.sleep(3)
				L.logger.info('输入密码: %s' % passWord)
				# 收起键盘
				self.driver.by_id('完成').click()
				time.sleep(3)
				self.driver.by_xpath("//*[@value='登 录']").click()
				time.sleep(3)
				
			except IOError as e:
				raise L.logger.error(e)

		elif self.platformName.lower() ==pf.android:
			try:
				self.driver.swipe_up() # 向上滑动
				# self.driver.implicitly_wait(3)
				time.sleep(3)
				self.driver.by_xpath("//android.widget.Button[contains(@text,'loading')]").click()
				# self.driver.implicitly_wait(3)
				time.sleep(3)
				self.driver.swipe_right()  # 右滑动
				# self.driver.implicitly_wait(3)
				time.sleep(3)
				# 点击个人中心
				self.driver.by_xpath("//android.widget.TextView[@text='个人中心']").click()
				# self.driver.implicitly_wait(3)
				time.sleep(3)
				# 填写账号
				self.driver.by_id(self.Andr_UserName).send_keys(userName)
				# self.driver.implicitly_wait(3)
				time.sleep(2)
				# 填写密码
				self.driver.by_id(self.Andr_PassWord).send_keys(passWord)
				# self.driver.implicitly_wait(3)
				time.sleep(2)
				# 点击登录
				self.driver.by_id("login-button").click()
				# self.driver.implicitly_wait(3)
				time.sleep(3)
				
			except Exception as e:
				L.logger.error(e)
		else:
			L.logger.error('请在配置文件中添加正确的platformName!!')
		
	
	def pluginNum_contain(self,contain):
		pageSource = self.driver.page_source()
		contain_list = re.findall(contain,pageSource)
		contain_count = contain_list.count(contain)
		L.logger.info('包含: %s 的个数是: %d' % (contain,contain_count))
		return contain_count
	
	def find_element_by_plugin(self,pluginId):
		'''
		通过插件id 查找元素对象
		:param pluginId:
		:return:
		'''
		
		if self.platformName.lower() == pf.ios:
			return self.driver.find_element((By.ID, pluginId),10)
		else:
			ele_xpath = "//android.view.ViewGroup[contains(@content-desc,'{}')]".format(pluginId)
			return self.driver.find_element((By.XPATH, ele_xpath),10)
		
	def check_plugin(self, pluginId, expectResult):
		'''
		对插件进行校验
		:param pluginId:
		:param expectResult:
		:return:True
		'''
		
		L.logger.info('开始检查插件: %s' % pluginId)
		# 对插件第一个页面进行判断
		i = 5  # 左滑动次数
		j = 5  # 右滑动次数
		
		try:
			while (not (self.find_element_by_plugin(pluginId)) and i > 0):
				L.logger.info('插件%s 未显示,左滑' % pluginId)
				self.driver.swipe_left()
				i = i - 1
			else:
				try:
					L.logger.info('找到插件: %s ,准备点击打开' % pluginId)
					self.find_element_by_plugin(pluginId).click()
					L.logger.info('判断插件页面,是否包含: %s' % expectResult)
					if self.wait_for_text(30, expectResult):
						L.logger.info('插件页面中包含 %s,返回True' % expectResult)
						return True
					else:
						L.logger.error('插件页面中不包含 %s,返回False' % expectResult)
						return False
				except Exception as e:
					L.logger.error(e)
					return False
				finally:
					self.closeH5_byPluginId(pluginId)
		finally:
			# 向右滑动
			while(i==0 and j>0):
				self.driver.swipe_right()
				j=j-1
				L.logger.info('右滑动恢复左边查找')
			
			
	def closeH5_byPluginId(self,pluginId):
		'''通过插件ID来判断关闭H5的方式(iOS 有某几个插件关闭H5比较特别)'''
		L.logger.info('关闭H5页面!')
		if self.platformName.lower() == pf.ios:
			if  pluginId == 'PA01100000000_02_PAZB':
				try:
					self.driver.by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeButton[1]').click()
				except:
					self.driver.by_xpath("//*[@name='com nav ic back']").click()
			elif pluginId == 'PA02700000000_02_PAYX':
				self.driver.by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]").click()
				self.driver.implicitly_wait(5)
				self.driver.by_xpath("//*[@name='关闭']").click()
			elif pluginId == 'PA02100000000_02_CJKX':
				self.driver.by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]').click()
			# elif pluginId == 'PA01100000000_02_RYG':
			# 	self.driver.by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]").click()
			else:
				self.closeH5()
		else:
			self.closeH5()
			
	def closeH5(self):
		'''
		关闭H5界面
		:return: True
		'''
		# ios 关闭H5
		if self.platformName.lower() == pf.ios:
			try:
				if self.driver.by_id('closeButton'):
					self.driver.by_id('closeButton').click()
				elif self.driver.by_id('关闭'):
					self.driver.by_id('关闭').click()
				elif self.driver.by_id('返回'):
					self.driver.by_id('返回').click()
				elif self.driver.by_id('com nav ic back'):
					self.driver.by_id('com nav ic back').click()
				else:
					L.logger.warning('通过[ by id ]关闭H5失败')
			
			except:
					if self.driver.by_xpath("//*[@name='closeButton']"):
						self.driver.by_xpath("//*[@name='closeButton']").click()
					elif self.driver.by_xpath("//*[@name='关闭']"):
						self.driver.by_xpath("//*[@name='关闭']").click()
					elif self.driver.by_xpath("//*[@name='返回']"):
						self.driver.by_xpath("//*[@name='返回']").click()
					elif self.driver.by_xpath("//*[@name='com nav ic back']"):
						self.driver.by_xpath("//*[@name='com nav ic back']").click()
					else:
						L.logger.warning('暂不支持的关闭方式,xpah关闭H5失败')

		else:
			# Android 关闭H5
			el = self.driver.by_id('com.paic.example.simpleapp:array/user_system')
			if el:
				el.click()
			elif self.driver.by_id('back'):
				self.click(self.driver.by_id('back'),'点击返回id: back')
			elif self.driver.by_id('quit'):
				self.click(self.driver.by_id('quit'), '点击返回id: quit')
			else:
				pass
				
	
	def getPluginList(self):
		pluginInfoList = []
		try:
			L.logger.info('开始获取插件列表。。。')
			response = requests.get(self.pluginURL)
			response_dict = json.loads(response.text)
			L.logger.info('当前插件总数: %d', len(response_dict['body']['data']))
			L.logger.info('当前插件列表: ')
			for pluginInfo in response_dict['body']['data']:
				self.pluginList = pluginInfo
				L.logger.info('%s---%s---%s' % (
				pluginInfo['title'], pluginInfo['pluginUid'], pluginInfo['needLogin']))
				pluginInfoList.append(pluginInfo['pluginUid'])
		except Exception as e:
			L.logger.warning(e)
			# raise e
		finally:
			return pluginInfoList

	def isAlert(self):
		'''
		判断是否有弹窗,如果有弹窗在点击确定关闭
		:return: True
		'''
		try:
			if self.driver.by_id('“https://mobilesdk.pingan.com.cn”想使用您当前的位置').is_enabled():
			# if self.wait_for_text(10,'“https://mobilesdk.pingan.com.cn”想使用您当前的位置'):
				self.driver.by_id('好').click()
			else:
				L.logger.info('没找到Alert弹窗')
		except Exception as e:
			L.logger.error(e)


	def is_exist(self, by_type , by_value):
		'''
		To determine whether an element is exits
        :return: TRUE or FALSE
        '''
		bytype_lower =str(by_type).lower()
		try:
			if bytype_lower == 'id':
				self.driver.by_id(by_value)
				return True
			if bytype_lower == 'xpath':
				self.driver.by_xpath(by_value)
				return True
			if bytype_lower == 'name':
				self.driver.by_name(by_value)
				return True
			if bytype_lower == 'classname':
				self.driver.by_classname(by_value)
				return True
		except Exception as e:
			L.logger.error(e)


	def wait_for_text(self,time_second,text):
		'''
		轮询页面资源查找需要的文本信息
		:param time_second:
		:param text:
		:return:True
		'''
		i = 1
		L.logger.info("开始轮询元素: %s" % text)
		while str(text) not in str(self.driver.page_source()):
			time.sleep(2)
			i +=2
			if i>=time_second:
				L.logger.warning('轮询超时,未找到元素:[ %s ]' % text)
				L.logger.warning('轮询超时,pageSource: <xmp>%s</xmp> ' % self.driver.page_source())
				return False
		else:
			L.logger.info('界面存在此元素:[ %s ]' % text)
			return True
	
	
	
	def get_screen_shot_base64(self):
		return self.driver.screenshot_as_base64()
	
	def get_screen_shot(self):
		'''
		sceen shot
		:return:
		'''
		timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
		filepath = os.path.abspath('../output/sceenshot/') + timestr + '.png'
		return self.driver.screenshot_as_file(filepath)
	
	def click(self,element_object,msg=None):
		L.logger.info(msg)
		return element_object.click()
	
	def sendKeys(self,element_object,sendtext):
		L.logger.info('输入内容: %s' % sendtext)
		# self.click(element_object,'click')
		# self.clear(element_object,'clear')
		return element_object.send_keys(sendtext)
	
	def clear(self,element_object,msg=None):
		L.logger.info(msg)
		return element_object.clear()
	
	
if __name__ == '__main__':

	pass
