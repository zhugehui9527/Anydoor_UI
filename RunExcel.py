# -*- coding:utf-8 -*-
from src.ExcelOperate.ReadApi import ReadApi
from conf.Run_conf import read_config
from src.Public import ExcelRW
from src.Common import public
from src.Element import Element
import unittest


xls_file_path = read_config('testcase', 'xls_case_path')
xlsEngine = ExcelRW.XlsEngine(xls_file_path)
xlsEngine.open()  # 打开excel
readApi = ReadApi()
case_sheet1 = xlsEngine.readsheet(public.case_sheet)
readApi.callCase(case_sheet1)

class RunExcel(unittest.TestCase):
	def setup_class(cls):
		cls.driver = Element()
		
	def teardown_class(cls):
		cls.driver.quit()
		
	def getTest_case(self):
		suite = unittest.TestSuite()
		for case_list in case_sheet1[1:]:
			suite.addTest(case_list[0])
		return suite
	
if __name__ == '__main__':
	runexcel = RunExcel()
	suite = runexcel.getTest_case()
	suite.run()