# -*- coding:utf-8 -*-
#######################################################
# filename:Run.py
# author:Jeff
# date:2016-11-21
# function:驱动Excel、脚本 测试用例
#######################################################
import unittest
from conf.Run_conf import read_config
from multiprocessing import Pool
# from RunScript import run_pytest
from src.Public.AppiumServer import AppiumServer
from src.lib import ExcelRW
from src.Public.Common import public
from src.Public.Global import D,S,L
# from src.lib.Utils import utils
xls_file_path = read_config('testcase', 'xls_case_path')
xlsEngine = ExcelRW.XlsEngine(xls_file_path)
xlsEngine.open()  # 打开excel
case_sheet1 = xlsEngine.readsheet(public.case_sheet)
appium_server = AppiumServer()

def run(device, port):
	'''
	:param device: dict
	:param port: int
	:return:
	'''
	# 启动appium 服务
	appium_server.start_server(device, port)
	from src.lib.Driver import Driver
	# 实例化Dirver
	Dr = Driver(device, port)
	Dr.init() #初始化driver
	# 获取driver
	driver = Dr.start_driver()
	D.set_driver(driver)

	# 运行不同模式的测试用例
	run_mode()
	
def pool_run():
	'''
	线程池启动多线程
	:return:
	'''
	# result = []
	devices = appium_server.get_device()
	# print devices
	count = len(devices)
	
	pool = Pool(processes=count)
	pool_list = appium_server.get_port(count)
	# 启动多个服务
	for i in range(count):
		S.set_device(devices[i])
		print 'devices = ',devices[i]['udid']
		from src.lib.Log import LogSignleton
		logsignleton = LogSignleton()
		logger = logsignleton.logger
		L.set_logger(logger)
		
		run(devices[i], pool_list[i])
	# pool.apply_async(self.start_server, args=(devices[i], pool_list[i]))
	pool.close()
	pool.join()
	
def run_mode():
	'''
	runmod 选择运行模式,1:运行excel用例,0:运行脚本用例
	:return:
	'''
	runmod = str(read_config('runmode','mode'))
	if runmod == '1':
		# print '*' * 80
		print '* [',__name__,'::',run_mode.__name__,'] :',' 运行 Excel 测试用例 '
		print '*' * 80
		#驱动测试
		runner = unittest.TextTestRunner(verbosity=2)
		__Run_Case(runner)
	elif runmod == '0':
		# print '*' * 80
		print '* [', __name__, '::', run_mode.__name__, '] :', ' 运行 Script 测试用例 '
		print '*' * 80
		import RunScript
		RunScript.run_pytest()
		
def clean_process():
	'''
	清理线程
	:return:
	'''
	from src.Public import CleanProcess
	#结束服务进程
	cp = CleanProcess.Cp()
	cp.clean_process_all()

import RunExcel
def __get_test_suite(case_list):
	'''
	获取测试套
	:param case_list:
	:return:
	'''
	test_suite = unittest.TestSuite()
	
	run_excel_case = RunExcel.RunExcelCase(case_list, "function")
	test_suite.addTest(run_excel_case)
	return test_suite

def __Run_Case(runner):
	'''
	运行测试用例
	:param runner:
	:return:
	'''
	# 循环遍历测试用例列表
	for case_list in case_sheet1[1:]:
		test_suite = __get_test_suite(case_list)
		runner.run(test_suite)
	# 退出服务
	# D.driver.quit()
	# 生成测试报告
	RunExcel.get_html_report()

#执行 - 结束进程
pool_run()
clean_process()

