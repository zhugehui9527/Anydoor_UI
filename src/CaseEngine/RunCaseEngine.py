#coding=utf8
#######################################################
#filename:RunCaseEngine.py
#author:Jeff
#date:2016-9
#function:
#######################################################
'''
from CaseEngine import CaseEngine
from ElementEngine import ElementEngine
from src.Global import logger
from src.Common import *


class RunCaseEngine(object):
	def __init__(self,operate_row,operate_type,operate_value,operate_method,operate_index='',param=''):
		self.operate_type = operate_type
		self.operate_value = operate_value
		self.operate_method = operate_method
		self.operate_index = operate_index
		self.param = param
		self.operate_row = operate_row
		self.case_engine = CaseEngine(operate_row,operate_type,operate_value,operate_index)

	def operate(self):
		operate_dict={operate_api.click:lambda: self.case_engine.click(),
		              operate_api.sendkeys:lambda: self.case_engine.sendkeys(),
		              operate_api.swipe2left:lambda: self.case_engine.swipe_left(),
		              operate_api.swipe2right:lambda: self.case_engine.swipe_right(),
		              operate_api.assertTrue:lambda: self.case_engine.assertTrue(),
		              operate_api.assertFalse:lambda: self.case_engine.assertFalse(),
		              operate_api.waitFortext:lambda: self.case_engine.waitFortext()
		              }
		# logger.debug('operate_dict = %s' % operate_dict )
		if operate_dict.has_key(str(self.operate_method).lower()):
			logger.debug('找到方法 : %s ' % self.operate_method)
			return operate_dict[self.operate_method]()

class RunElementEngine(object):
	def __init__(self,operate_row,operate_type,operate_value,operate_index=''):
		self.operate_type = operate_type
		self.operate_value = operate_value
		self.operate_index = operate_index
		self.operate_row = operate_row
		self.element_engine = ElementEngine

	def get_element_sheet(self):
		operate_dict = {operate_api.click: lambda: self.case_engine.click(),
		                operate_api.sendkeys: lambda: self.case_engine.sendkeys(),
		                operate_api.swipe2left: lambda: self.case_engine.swipe_left(),
		                operate_api.swipe2right: lambda: self.case_engine.swipe_right(),
		                operate_api.assertTrue: lambda: self.case_engine.assertTrue(),
		                operate_api.assertFalse: lambda: self.case_engine.assertFalse(),
		                operate_api.waitFortext: lambda: self.case_engine.waitFortext()
		                }
		element_sheet_dict={element_by_excel.login_low_button: lambda: self.element_engine

		}
		# logger.debug('operate_dict = %s' % operate_dict )
		if operate_dict.has_key(str(self.operate_method).lower()):
			logger.debug('找到方法 : %s ' % self.operate_method)
			return operate_dict[self.operate_method]()

'''