# -*- coding:utf-8 -*-
#######################################################
#filename:self.driver.py
#author:Jeff
#date:2016-09-21
#function:对日志进行操作处理
#######################################################
from Element import Element
from Public.Public import *
from Global import logger
import time,requests,json,sys
reload(sys)
sys.setdefaultencoding('utf-8')

class AppOperate (object):
	def __init__(self):
		# super(AppOperate,self).__init__()
		# global driver
		iOS_UserName = "//*[@value='一账通号/手机号/身份证号/邮箱']"
		iOS_PassWord = "//*[@value='密码']"
		Andr_UserName = "com.paic.example.simpleapp:id/user-id-input"
		Andr_PassWord = "com.paic.example.simpleapp:id/user-psd-input"
		config_path = '/Users/zengyuanchen/Documents/Project/Anydoor_UI/conf/monitor.ini'
		platformName = read_config(config_path, 'appium', 'platformName')
		self.pluginURL = read_config(config_path, 'plugin', 'plugin_url_iOS')
		self.platformName = platformName
		self.iOS_UserName = iOS_UserName
		self.iOS_PassWord = iOS_PassWord
		self.Andr_UserName = Andr_UserName
		self.Andr_PassWord = Andr_PassWord
		self.driver = Element()
		self.pluginList =[]
		# global logger
		# logsignleton = LogSignleton(config_path)
		# logger = logsignleton.logger

	def loginByHost(self):
		'''
		一账通登陆
		:return:True
		'''
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
			self.driver.implicitly_wait(10)
			# self.driver.swipe_right()
			# self.assertIsNotNone(self.driver.by_id('个人中心'),'登陆成功 ')
			# self.driver.swipe_left()
		except Exception as e:
			logger.warning(e)

	def loginOut(self):
		'''
		注销登陆
		:return: True
		'''
		try:
			self.driver.implicitly_wait(3)
			self.driver.by_id("无用户").click()
			return True
		except Exception as e:
			logger.warning(e)
			return False

	#支持iOS和Android
	def loginByH5(self,userName,passWord):
		appOperate = AppOperate()
		self.driver.implicitly_wait(3)
		# logger.debug('进入个人中心')
		# self.driver.swipe_right()
		self.driver.implicitly_wait(3)
		self.driver.by_id("个人中心").click()
		self.driver.implicitly_wait(10)
		if self.platformName.lower() =='ios' and appOperate.wait_for_text(40,'一账通登录'):
			try:
				self.driver.implicitly_wait(10)
				#填写账号
				self.driver.by_xpath(self.iOS_UserName).click()
				logger.debug('点击账号输入框')
				self.driver.implicitly_wait(3)
				self.driver.by_xpath(self.iOS_UserName).clear()
				logger.debug('清除输入框文本内容')
				self.driver.implicitly_wait(3)
				self.driver.by_xpath(self.iOS_UserName).send_keys(userName)
				logger.debug('输入账号: %s' % userName)
				#填写密码
				self.driver.implicitly_wait(3)
				self.driver.by_xpath(self.iOS_PassWord).click()
				self.driver.implicitly_wait(3)
				self.driver.by_xpath(self.iOS_PassWord).clear()
				logger.debug('清除输入框文本内容')
				self.driver.implicitly_wait(3)
				self.driver.by_xpath(self.iOS_PassWord).send_keys(passWord)
				logger.debug('输入密码: %s' % passWord)
				time.sleep(5)
				self.driver.implicitly_wait(10)
				#收起键盘
				self.driver.by_id('完成').click()
				self.driver.by_xpath("//UIALink[@name='登 录']").click()
				self.driver.load_page_timeout(30)
				# self.assertIn('个人中心',self.driver.page_source(),'登录成功')
			except IOError as e:
				raise logger.error(e)

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
				self.driver.keyevent(4)
				self.driver.by_name("登 录 Link").click()
				self.driver.implicitly_wait(10)
			except Exception as e:
				logger.error(e)
		else:
			logger.error('请在配置文件中添加正确的platformName!!')

	def check_plugin(self, pluginId, expectResult):
		'''
		对插件进行校验
		:param pluginId:
		:param expectResult:
		:return:True
		'''
		global appOperate
		appOperate = AppOperate()
		# if self.driver.by_id(pluginId).is_enabled():
		if appOperate.wait_for_text(3,pluginId):
			logger.debug('找到插件:%s ,准备点击' % pluginId)
		elif not appOperate.wait_for_text(3,pluginId):
			try:
				logger.debug('没找到插件:%s ,准备滑动' % pluginId)
				self.driver.swipe_left()
				self.driver.implicitly_wait(3)
			except:
				logger.error('滑动后,仍找不到插件!')
		elif not appOperate.wait_for_text(3,pluginId):
			try:
				logger.debug('没找到插件:%s ,准备滑动' % pluginId)
				self.driver.swipe_right()
				self.driver.implicitly_wait(3)
			except:
				logger.error('滑动后,仍找不到插件!')

		try:
			self.driver.by_id(pluginId).click()
			time.sleep(3)
			self.driver.implicitly_wait(20)
			#判断是否有弹窗,有弹窗就点击确定关闭弹窗
			# appOperate.isAlert()
			logger.debug('判断插件页面,是否包含: %s' % expectResult)
			if appOperate.wait_for_text(40,expectResult):
				logger.debug('插件页面中包含 %s,返回True' % expectResult)
				return True
			else:
				logger.error('插件页面中不包含 %s,返回False' % expectResult)
				return False

		except Exception as e:
			logger.error(e)
			return False
		finally:
			logger.debug('关闭H5页面!')
			if pluginId == 'PA01100000000_02_KB' or pluginId == 'PA01100000000_02_PAZB':
				self.driver.by_id('关闭').click()
			elif pluginId == 'PA02100000000_02_WXYJ':
				self.driver.by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAImage[1]').click()
			else:
				appOperate.closeH5()

	def closeH5(self):
		'''
		关闭H5界面
		:return: True
		'''
		try:
			self.driver.implicitly_wait(3)
			if self.driver.by_id('closeButton'):
				self.driver.by_id('closeButton').click()
			elif self.driver.by_id('关闭'):
				self.driver.by_id('关闭').click()
			elif self.driver.by_id('返回'):
				self.driver.by_id('返回').click()
			elif self.driver.by_id('htmlbackhome'):
				self.driver.by_id('htmlbackhome').click()
			else:
				logger.warning('关闭H5页面失败!')
				return False
			return True
		except Exception as e:
			logger.warning(e)
			return False

	def getPluginList(self):
		try:
			logger.debug('开始获取插件列表。。。')
			response = requests.get(self.pluginURL)
			response_dict = json.loads(response.text)
			logger.debug('当前插件总数: %d', len(response_dict['body']['data']))
			logger.debug('当前插件列表: ')
			for pluginInfo in response_dict['body']['data']:
				self.pluginList = pluginInfo
				logger.debug('%s---%s---%s' % (
				pluginInfo['title'], pluginInfo['pluginUid'], pluginInfo['needLogin']))

		except Exception as e:
			logger.warning(e)

	def isAlert(self):
		'''
		判断是否有弹窗,如果有弹窗在点击确定关闭
		:return: True
		'''
		try:
			if self.driver.by_id('“https://mobilesdk.pingan.com.cn”想使用您当前的位置').is_enabled():
			# if appOperate.wait_for_text(10,'“https://mobilesdk.pingan.com.cn”想使用您当前的位置'):
				self.driver.by_id('好').click()
			else:
				logger.debug('没找到Alert弹窗')
		except Exception as e:
			logger.error(e)


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
			logger.error(e)


	def wait_for_text(self,time_second,text):
		'''
		轮询页面资源查找需要的文本信息
		:param time_second:
		:param text:
		:return:True
		'''
		i = 1
		# self.driver.load_page_timeout(int(time_second))
		# pageSource = self.driver.page_source()
		# logger.debug("打印出来pageSource : %s" % pageSource)
		logger.debug("开始轮询元素: %s" % text)
		while text not in str(self.driver.page_source()):
			time.sleep(1)
			i +=1
			if i>=time_second:
				logger.warning('轮询超时,未找到元素: %s' % text)
				return False
		else:
			logger.debug('界面存在此元素: %s' % text)
			return True



if __name__ == '__main__':
	appOperates = AppOperate()
	appOperates.getPluginList()
	# appOperates.loginByH5('18589091413','Solution123')
	# ss = appOperates.wait_for_text(30,'我的资产')
	# print ss
	# assert ss
