#coding=utf8
#######################################################
#filename:Interface_Test.py
#author:defias
#date:2015-7
#function:
#######################################################
from src.appOperate import AppOperate
from conf.Run_conf import read_config
from src.Global import logger
from src.Common import operate_api
from src.Element import Element
from ReadElement import ReadElement
from src.Public import ExcelRW
from src.Common import public
import unittest,time

class ReadApi(unittest.TestCase):
	
	def __init__(self):
		'''
		:param case_list: 此参数为公共案例库和sheet1 中用例所公用列表入参
		'''
		# self.case_list=case_list
		self.platformName = read_config('appium', 'platformName')
		self.appOperate = AppOperate()
		self.wd = Element()
		self.readElement = ReadElement()
		self.xls_file_path = read_config('testcase', 'xls_case_path')
		self.xlsEngine = ExcelRW.XlsEngine(self.xls_file_path)
		self.xlsEngine.open()  # 打开excel
		# self.element_name_list = self.xlsEngine.readcol(element_by_excel.element_sheet_name,1) #读取元素表第一列
		self.publicCaseList = self.xlsEngine.readsheet(public.public_case_sheet)
		
	def readApiList(self,case_list=[]): #case_list是一维数组
		logger.debug('case_list :%s' % case_list)
		
		# for cases in case_list:
		# 	if cases:
		# 		logger.debug('cases: %s ' % cases)
		# 		logger.debug('当前支持的平台类型: %s ' % cases[4])
		# 		self.callApi(cases)
		#
		#
		if case_list:
			try:
				self.callApi(case_list)
			except Exception as e:
				logger.error(e)
		# 	# if len(case_list[4])==0 or ('ios' in case_list and self.platformName.lower()=='ios') or ('android' in case_list and self.platformName.lower()=='android'):
		# 	# 	if 'ios' in case_list:
		# 	# 		logger.warning('该方法仅限于ios执行!')
		# 	# 	elif 'android' in case_list:
		# 	# 		logger.warning('该方法仅限于Android执行!')
		# 	# 	else:
		# 	# 		pass
		# 	# 	self.callApi(case_list)
		# 	# else:
		# 	# 	logger.warning('case_list为空')
		#
		else:
			logger.warning('%s 表为空' % case_list)
		
	def callApi(self,case_list):
		'''
		:description:通过字典api_dict管理api,并调用api,api定义则在operate_api类中
		:param case_list:
		:return:
		'''
		logger.debug('callApi执行中')
		# case_list[6]= PageObject(页面元素),case_list[7] =Parameter（传入参数）
		# element_text = self.readElement.find_element(self.readElement.read_element_text(case_list[5]))
		# pageObject_text = case_list[6]
		# param_text = case_list[7]
		# api_text = case_list[3]
		
		api_dict = {
					operate_api.assertTrueCheckPlugin:lambda :self.assertTrue(self.appOperate.check_plugin(case_list[6],case_list[7]),'断言check_plugin'),
					operate_api.assertTrue:lambda :self.assertTrue(self.appOperate.wait_for_text(int(case_list[7]),case_list[6]),'断言wait_for_text'),
		            operate_api.sendkeys:lambda :self.appOperate.sendKeys(self.readElement.find_element(self.readElement.read_element_text(case_list[5])),case_list[7]),
		            operate_api.click:lambda :self.appOperate.click(self.readElement.find_element(self.readElement.read_element_text(case_list[5])),'click'),
		            operate_api.swipe2left:lambda :self.wd.swipe_left(),
		            operate_api.swipe2right:lambda :self.wd.swipe_right(),
		            operate_api.hidekeyboard:lambda :self.wd.hide_keyboard(case_list[7]),
		            operate_api.waitFortext:lambda :self.appOperate.wait_for_text(int(case_list[7]),case_list[6]),
		            operate_api.sleep:lambda :time.sleep(int(case_list[7])),
		            operate_api.publicCase:lambda :self.callCase(case_list[7]),
					operate_api.checkPlugin:lambda :self.appOperate.check_plugin(case_list[6],case_list[7]),
		            operate_api.closeH5:lambda :self.appOperate.closeH5(),
		            operate_api.closeH5ByPluginId:lambda :self.appOperate.closeH5_byPluginId(case_list[6]),
		            operate_api.getScreenShot:lambda :self.appOperate.get_screen_shot(),
		            operate_api.getPluginList:lambda :self.appOperate.getPluginList()
		    
		            }
		if api_dict.has_key(case_list[3]):
			logger.debug('Action_Keyword 操作:[ %s ]' % case_list[3])
			return api_dict[case_list[3]]()
		else:
			logger.warning('请检查Action_Keyword中的api是否输入正确!')
			
	def callPublicCase(self,casename):
		'''
		:description:判断casename是否在公共案例库中,如有则执行公共案例库
		:param casename:
		:return:
		'''
		logger.debug('callCase 执行中')
		currentCase = ''
		# y=0
		# for x in range(len(self.publicCaseList)):
		# 	if self.publicCaseList[x][0]==casename:
		# 		y=x
		# 	else:
		# 		pass
		# 	logger.debug('当前用例列表: %s' % self.publicCaseList[y])
		# 	if self.publicCaseList[y[0]:
		# 		self.readApiList(self.publicCaseList[y])
		
		# 遍历公共案例库
		for publicCase in self.publicCaseList:
			# logger.debug('当前用例列表索引: %s ' % publicCase)
			#
			# if currentCase:
			# 	currentCase = publicCase[0]
			# else:
			# 	if casename == publicCase[0]:
			# 		currentCase =publicCase[0]
			# 	else:
			# 		pass
			# logger.debug('当前用例名称为: %s ' % currentCase)
			# logger.debug('当前用例列表为: %s ' % publicCase)
			# if casename ==publicCase[0]:
			# 	logger.debug('当前用例列表为: %s ' % publicCase)
			if casename in publicCase[0]:
				logger.debug('公共案例库中存在此方法: %s' % casename)
				logger.debug('当前用例列表为: %s ' % publicCase)
				self.readApiList(publicCase)
			else:
				pass
	
	
	def callCase(self,caselists):
		'''
		:description:读取案例库
		:param caselist: 为二维数组
		:return:
		'''
		cases =[]
		for caselist in caselists[1:]:
			if operate_api.publicCase == caselist[3]:
				logger.debug('==='*40)
				logger.debug('当前行列表: %s' % caselist)
				logger.debug('当前用例名称: %s' % caselist[0])
				logger.debug('===' * 40)
				self.callPublicCase(caselist[7])
				if not caselist[0]:
					cases.append(caselist[0])
			else:
				logger.debug('===' * 40)
				logger.debug('当前行列表: %s' % caselist)
				logger.debug('当前用例名称: %s' % caselist[0])
				logger.debug('===' * 40)
				self.readApiList(caselist)
				if not caselist[0]:
					cases.append(caselist[0])
		logger.debug('用例列表为: %s' % cases)
		return cases
	
	# def getCaselist(self,caselists):
	# 	cases = []
	# 	for caslist in caselists[1:]:
	#
	
	
if __name__ == '__main__':
	readapi = ReadApi()
	readapi.callPublicCase('SwipeToClickPersonalCenter')
	# for publicCase in readapi.publicCaseList:
		