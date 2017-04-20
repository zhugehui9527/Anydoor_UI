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
from src.Public.Common import public as pc
from src.Public.Public import Img
from src.lib.Element import Element
from selenium.webdriver.common.by import By

reload(sys)
sys.setdefaultencoding('utf-8')

class AppOperate (object):
	def __init__(self,driver):
		self.pluginURL = read_config('plugin', 'plugin_url_iOS')
		self.platformName = S.device['platformName']
		self.iOS_UserName =  "//*[@value='一账通号/手机号/身份证号/邮箱']"
		self.iOS_PassWord = "//*[@value='密码']"
		self.Andr_UserName = "user-id-input"
		self.Andr_PassWord = "user-psd-input"
		self.username = read_config('login', 'login_username')
		self.password = read_config('login', 'login_password')
		self.driver = Element(driver)
		self.pluginList =[]
		self.runmode = read_config(pc.runmode, pc.driver)
		
	
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
				if not self.driver.by_id('一账通登录'):
					self.driver.swipe_right()  # 右滑动
					# time.sleep(3)
					self.driver.by_id("个人中心").click()
					time.sleep(3)
				self.driver.by_xpath(self.iOS_UserName).send_keys(userName)
				# time.sleep(3)
				L.logger.info('输入账号: %s' % userName)
				# 收起键盘
				self.driver.by_id('完成').click()
				# time.sleep(3)
				self.driver.by_xpath(self.iOS_PassWord).send_keys(passWord)
				# time.sleep(3)
				L.logger.info('输入密码: %s' % passWord)
				# 收起键盘
				self.driver.by_id('完成').click()
				# time.sleep(3)
				self.driver.by_xpath("//*[@value='登 录']").click()
				# time.sleep(3)
				
			except IOError as e:
				raise L.logger.error(e)

		elif self.platformName.lower() ==pf.android:
			try:
				if not self.driver.by_name('一账通登录'):
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
				time.sleep(3)
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
	
	def find_element_by_plugin_orign(self, pluginId):
		'''
		通过插件id 查找元素对象
		:param pluginId:
		:return:
		'''
		
		if self.platformName.lower() == pf.ios:
			return self.driver.find_element_orign(By.ID, pluginId)
		else:
			ele_xpath = "//android.view.ViewGroup[contains(@content-desc,'{}')]".format(pluginId)
			return self.driver.find_element_orign(By.XPATH, ele_xpath)
		
	def check_plugin_byImage(self,pluginId,x1,y1,x2,y2):

		L.logger.info('开始检查插件: %s' % pluginId)
		# 对插件第一个页面进行判断
		i = 5  # 左滑动次数
		j = 5  # 右滑动次数

		try:
			while ((self.find_element_by_plugin(pluginId) is None) and i > 0):
				L.logger.info('插件%s 未显示,左滑' % pluginId)
				self.driver.swipe_left()
				i = i - 1
			else:
				try:
					L.logger.info('找到插件: %s ,准备点击打开' % pluginId)
					self.find_element_by_plugin(pluginId).click()
					time.sleep(10)
					img = Img(self.driver)
					# 裁剪
					img.get_screen_by_size(x1,y1,x2,y2)
					dirpath = os.path.abspath(('./output/{}/screen').format(S.device['udid']))
					# 第一次跑需要把截图复制到项目的screen目录下
					isRewrite  = bool(read_config('screenshot','isRewrite'))
					if isRewrite:
						imagepath = img.copy_to_file(dirpath, pluginId, form='png') # 预期结果
						L.logger.info('无预期截图路径,生成新路径: %s' % imagepath)
					else:
						# screen目录下已有预期截图就可以把上面代码注释,下面的代码取消注释
						imagepath = dirpath + '/{}.png'.format(pluginId)
						L.logger.info('已有预期截图路径,不需要生成')
					L.logger.info('预期截图路径: %s ' % imagepath)
					loadimage = img.load_image(imagepath)

					if img.compare(loadimage, 0):
						L.logger.info('截图对比成功')
						return True
					else:
						L.logger.warning('截图对比失败')
						return False
				except Exception as e:
					L.logger.error(e)
					return False
				finally:
					self.closeH5_byPluginId(pluginId)
		finally:
			# 向右滑动
			while (i == 0 and j > 0):
				self.driver.swipe_right()
				j = j - 1
				L.logger.info('右滑动恢复左边查找')



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
			while ( (self.find_element_by_plugin(pluginId) is None) and i > 0):
				L.logger.info('插件%s 未显示,左滑' % pluginId)
				self.driver.swipe_left()
				i = i - 1
			else:
				try:
					L.logger.info('找到插件: %s ,准备点击打开' % pluginId)
					self.find_element_by_plugin(pluginId).click()
					L.logger.info('判断插件页面,是否包含: %s' % expectResult)
					#打开插件如果需要登录则进行登录

					if self.platformName.lower() == pf.ios and self.driver.find_element((By.ID,'一账通登录'),10) :
						self.loginByH5(self.username,self.password)
					k = 4 # 向上滑动次数
					while not self.wait_for_text(10, expectResult):
						k=k-1
						L.logger.warning('插件当前页面中未显示 %s,准备滑动' % expectResult)
						self.driver.swipe_up()

						if k==0:
							L.logger.error('插件页面中不包含 %s,返回False' % expectResult)
							return False

					L.logger.info('插件页面中包含 %s,返回True' % expectResult)
					return True
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
		backButtion = {'PA01100000000_02_PAZB':'//*[1]/*[1]/*[2]/*[1]/*[1]/*[1]/*[1]/*[2]/*[1]',
		               'PA02700000000_02_PAYX':'//*[1]/*[1]/*[2]/*[1]/*[1]/*[1]',
		               'PA02100000000_02_CJKX':'//*[1]/*[1]/*[2]/*[1]/*[1]/*[1]',
		               'PA02100000001_02_JF':'//*[1]/*[1]/*[2]/*[1]/*[1]/*[1]',
		               'PA01100000000_02_RYG':'//*[1]/*[1]/*[2]/*[1]/*[1]'}
		if self.platformName.lower() == pf.ios:
			if backButtion.has_key(pluginId):
				try:
					self.driver.by_xpath(backButtion[pluginId]).click()
				except:
					if pluginId == 'PA01100000000_02_PAZB':
						self.driver.by_xpath("//*[@name='com nav ic back']").click()
					else:
						self.closeH5()

				if pluginId == 'PA02700000000_02_PAYX':
					self.driver.by_xpath("//*[@name='关闭']").click()
			# if  pluginId == 'PA01100000000_02_PAZB':
			# 	try:
			# 		self.driver.by_xpath('//*[1]/*[1]/*[2]/*[1]/*[1]/*[1]/*[1]/*[2]/*[1]').click()
			# 	except:
			# 		self.driver.by_xpath("//*[@name='com nav ic back']").click()
			# elif pluginId == 'PA02700000000_02_PAYX':
			# 	self.driver.by_xpath("//*[1]/*[1]/*[2]/*[1]/*[1]/*[1]").click()
			# 	self.driver.implicitly_wait(5)
			# 	self.driver.by_xpath("//*[@name='关闭']").click()
			# elif pluginId == 'PA02100000000_02_CJKX' or pluginId == 'PA02100000001_02_JF':
			# 	self.driver.by_xpath('//*[1]/*[1]/*[2]/*[1]/*[1]/*[1]').click()
			# elif pluginId == 'PA01100000000_02_RYG':
			# 	self.driver.by_xpath("//*[1]/*[1]/*[2]/*[1]/*[1]").click()
			else:
				self.closeH5()
		else:
			self.closeH5()
			
	def closeH5(self):
		'''
		关闭H5界面
		:return: True
		'''
		backAction_ios = ["//*[@name='closeButton']",
		              "//*[@name='关闭']",
		              "//*[@name='返回']",
		              "//*[@name='com nav ic back']"]

		backAction_Anr = ['com.paic.example.simpleapp:array/user_system',
		                  'back',
		                  'quit']
		# ios 关闭H5
		if self.platformName.lower() == pf.ios:
			for back in backAction_ios:
				ele = self.driver.by_xpath(back)
				L.logger.info('closeH5 找到元素:%s ' % back)
				if ele:
					ele.click()
					break
		else:
			# Android 关闭H5
			for back in backAction_Anr:
				el = self.driver.by_id(back)
				if el:
					el.click()
					break

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
		# if self.runmode == pc.macaca:
		# 	while not (self.driver.find_element((By.ID, text), time_second) or
		# 		        self.driver.find_element((By.NAME, text), time_second)):
		# 		L.logger.warning('轮询超时,未找到元素:[ %s ]' % text)
		# 		time.sleep(2)
		# 		i += 2
		# 		if i >= time_second:
		# 			return False
		# 	else:
		# 		L.logger.info('界面存在此元素:[ %s ]' % text)
		# 		return True

		# '''
		if self.runmode == pc.appium:
			while str(text) not in (self.driver.page_source()):
				L.logger.warning('轮询超时,未找到元素:[ %s ]' % text)
				time.sleep(2)
				i +=2
				if i>=time_second:
					L.logger.warning('轮询超时,未找到元素:[ %s ]' % text)
					# page_source = str(self.driver.page_source()).replace('<','&lt;')
					# page_source = page_source.replace('>','&gt;')
					# # L.logger.warning('轮询超时,pageSource: <xmap>%s</xmap>' % page_source) #<pre></pre>
					# L.logger.warning('轮询超时,pageSource: %s' % page_source)
					return False
			else:
				L.logger.info('界面存在此元素:[ %s ]' % text)
				return True
		else:
			if not (self.driver.find_element((By.ID, text), time_second) or
				        self.driver.find_element((By.NAME, text),time_second)):
				L.logger.warning('轮询超时,未找到元素:[ %s ]' % text)
				return False
			else:
				L.logger.info('界面存在此元素:[ %s ]' % text)
				return True

			# '''
	def get_screen_shot_base64(self):
		return self.driver.screenshot_as_base64()
	
	def get_screen_shot(self):
		'''
		sceen shot
		:return:
		'''
		timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
		filepath = os.path.abspath('./output/sceenshot/') + timestr + '.png'
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
