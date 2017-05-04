#coding=utf8
#######################################################
#filename:ReadApi.py
#author:Jeff
#date:2016-11
#function:读取api相关功能和封装
#######################################################
import time,unittest,os
from ReadElement import ReadElement
from conf.Run_conf import read_config
from src.Public.Common import operate_api
from src.Public.appOperate import AppOperate
from src.lib.Element import Element
from src.Public.Global import L,S
import sys
sys.path.append("../../")

class ReadApi(unittest.TestCase):
	def __init__(self,driver):
		self.platformName = S.device['platformName']
		self.appOperate = AppOperate(driver)
		self.wd = Element(driver)
		self.readElement = ReadElement(driver)
		self.screen_shot_isTrue = bool(read_config('screenshot','screen_shot_isTrue'))
		self.screen_shot_path = os.path.abspath('./output/{}/screen/{}.png')

	def screen_shot(self,case):
		'''
		截图方法由截图开关控制
		:return:
		'''
		try:
			# timestamp = time.mktime(time.localtime())
			# 截图路径
			if case[0]:
				screen_shot_path = self.screen_shot_path.format(S.device['udid'],case[0])
			else:
				screen_shot_path = self.screen_shot_path.format(S.device['udid'], case[1])
			if self.screen_shot_isTrue:
				L.logger.debug('截图开关已打开,截图保存路径: %s' % screen_shot_path)
				self.wd.screenshot_as_file(screen_shot_path)
			else:
				pass
		except Exception as e:
			L.logger.error(e)

	def readApiList(self,case_list=[]): #case_list是一维数组
		L.logger.debug('case_list :%s' % case_list)
		if case_list:
			try:
				self.callApi(case_list)
				return True
			except Exception as e:
				L.logger.error(e)
				# API调用失败截图
				self.screen_shot(case_list)
				return False

	def callApi(self,case_list):
		'''
		:description:通过字典api_dict管理api,并调用api,api定义则在operate_api类中
		:param case_list:
		:return:
		'''
		L.logger.debug('callApi执行中')
		# 所有支持的api
		api_dict = {
					operate_api.assertTrueCheckPlugin:lambda :self.assertTrue(self.appOperate.check_plugin(case_list[6],case_list[7]),case_list[2]),
					operate_api.assertTrue:lambda :self.assertTrue(self.appOperate.wait_for_text(int(case_list[7]),case_list[6]),case_list[2]) ,
					operate_api.assertFalse:lambda :self.assertFalse(self.appOperate.wait_for_text(int(case_list[7]),case_list[6]),case_list[2]),
		            operate_api.sendkeys:lambda :self.appOperate.sendKeys(self.readElement.find_element(self.readElement.read_element_text(case_list[5])),case_list[7]),
		            operate_api.click:lambda :self.appOperate.click(self.readElement.find_element(self.readElement.read_element_text(case_list[5])),case_list[2]),
		            operate_api.swipe2left:lambda :self.wd.swipe_left(),
		            operate_api.swipe2right:lambda :self.wd.swipe_right(),
					operate_api.swipe2up: lambda: self.wd.swipe_up(),
					operate_api.swipe2down: lambda: self.wd.swipe_down(),
		            operate_api.hidekeyboard:lambda :self.wd.hide_keyboard(case_list[7]),
		            operate_api.waitFortext:lambda :self.appOperate.wait_for_text(int(case_list[7]),case_list[6]),
		            operate_api.sleep:lambda :time.sleep(int(case_list[7])),
					operate_api.checkPlugin:lambda :self.appOperate.check_plugin(case_list[6],case_list[7]),
		            operate_api.closeH5:lambda :self.appOperate.closeH5(),
		            operate_api.closeH5ByPluginId:lambda :self.appOperate.closeH5_byPluginId(case_list[6]),
		            operate_api.getScreenShot:lambda :self.appOperate.get_screen_shot(),
		            operate_api.getPluginList:lambda :self.appOperate.getPluginList()

		            }
		if api_dict.has_key(case_list[3]):
			L.logger.debug('Action_Keyword 操作:[ %s ]' % case_list[3])
			return api_dict[case_list[3]]()  #返回api对应的操作对象
		else:
			L.logger.error('请检查Action_Keyword中的api是否输入正确!')
			# raise

if __name__ == '__main__':
	pass
	# readapi = ReadApi()
	# readapi.callPublicCase('SwipeToClickPersonalCenter')
	# for publicCase in readapi.publicCaseList:
