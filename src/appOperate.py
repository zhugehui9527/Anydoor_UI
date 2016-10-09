# -*- coding:utf-8 -*-
#######################################################
#filename:driver.py
#author:Jeff
#date:2016-09-21
#function:对日志进行操作处理
#######################################################
from Element import *
from Global import *
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class appOperate (Element):
	def __init__(self):
		# super(appOperate,self).__init__()
		# global driver
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
		#driver 由外部传入
		#driver主动调入
		self.driver = get_Driver()
		self.logger = get_Logger()

	def wait_for_text(self,time_second,text):
		'''
		遍历页面资源查找需要的文本信息
		:param time_second:
		:param text:
		:return:
		'''
		self.driver.load_page_timeout(time_second)
		pageSource = self.driver.page_source()
		self.logger.debug("打印出来pageSource : %s" % pageSource)
		if text in str(pageSource):
			self.logger.debug('遍历结果: %s' % text)
			assert True
		else:
			self.logger.debug(text)
			assert False



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
			self.driver.implicitly_wait(8)
			return True
		except Exception as e:
			self.logger.warning(e)
			return False

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
			self.logger.warning(e)
			return False

	#支持iOS和Android
	def loginByH5(self,userName,passWord):
		self.driver.implicitly_wait(3)
		self.logger.debug('进入个人中心')
		self.driver.swipe_right()
		self.driver.implicitly_wait(3)
		self.driver.by_id("个人中心").click()
		self.driver.implicitly_wait(10)
		if self.platformName.lower() =='ios':
			try:
				self.driver.implicitly_wait(3)
				#填写账号
				self.driver.by_xpath(self.iOS_UserName).click()
				self.logger.debug('点击账号输入框')
				self.driver.implicitly_wait(3)
				self.driver.by_xpath(self.iOS_UserName).clear()
				self.logger.debug('清除输入框文本内容')
				self.driver.implicitly_wait(3)
				self.driver.by_xpath(self.iOS_UserName).send_keys(userName)
				self.logger.debug('输入账号: %s' % userName)
				#填写密码
				self.driver.implicitly_wait(3)
				self.driver.by_xpath(self.iOS_PassWord).click()
				self.driver.implicitly_wait(3)
				self.driver.by_xpath(self.iOS_PassWord).clear()
				self.logger.debug('清除输入框文本内容')
				self.driver.implicitly_wait(3)
				self.driver.by_xpath(self.iOS_PassWord).send_keys(passWord)
				self.logger.debug('输入密码: %s' % passWord)
				time.sleep(5)
				self.driver.implicitly_wait(10)
				#收起键盘
				self.driver.by_id('完成').click()
				self.driver.by_xpath("//UIALink[@name='登 录']").click()
				self.driver.load_page_timeout(30)
				if self.driver.by_id('我的资产'):
					print '登陆成功'
				else:
					print "登陆失败"
				# self.driver.implicitly_wait(10)


			except IOError,e:
				raise self.logger.error(e)

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
			except Exception, e:
				raise e
		else:
			print '请在配置文件中添加正确的platformName!!'

	def check_plugin(self, pluginId, expectResult):
		'''
		对插件进行校验
		:param pluginId:
		:param expectResult:
		:return:
		'''
		if self.driver.by_id(pluginId).is_enabled():
			self.logger.debug('找到插件:%s ' % pluginId)
		else:
			try:
				self.logger.debug('没找到插件:%s ,准备滑动' % pluginId)
				for x in range(2):
					if x == 0:
						self.driver.swipe_right()
					else:
						self.driver.swipe_left()
			except:
				raise


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
				self.logger.warning('关闭H5页面失败!')
				return False
			return True
		except Exception as e:
			self.logger.warning(e)
			return False


if __name__ == '__main__':
	appOperates = appOperate()
	appOperates.loginByH5('18589091413','Solution123')

