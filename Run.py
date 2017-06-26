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
from src.Public.Server import Server
from src.Public.GetDevices import GetDevices
from src.lib import ExcelRW
from src.Public.Common import public
from src.Public.Global import D,S,L,Data
from src.lib.Driver import Driver
from src.lib.Element import Element
import time,os

# from src.lib.Utils import utils
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def run_mode():
	'''
	runmod 选择运行模式,1:运行excel用例,0:运行脚本用例
	:return:
	'''
	runmod = str(read_config('runmode','mode'))
	if runmod == '1':
		print ('*' * 80)
		L.logger.info(' 运行 Excel 测试用例 ')
		xls_file_path = PATH('./TestCase/Excel/TestCase.xlsx')
		print ('*' * 80)
		print (time.ctime(), ' [', __name__, '::', '用例路径: ', xls_file_path)
		xlsEngine = ExcelRW.XlsEngine(xls_file_path)
		xlsEngine.open()  # 打开excel
		global case_sheet1
		case_sheet1 = xlsEngine.readsheet(public.case_sheet)
		#驱动测试
		runner = unittest.TextTestRunner()
		__Run_Case(runner)

	elif runmod == '0':
		# print '*' * 80
		# print (time.ctime()+' [', __name__, '::'+run_mode.__name__+'] :'+' 运行 Script 测试用例 ')
		# print ('*' * 80)
		L.logger.info(' 运行 Script 测试用例 ')
		import RunScript
		RunScript.run_pytest()
	else:
		pass

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
	# print time.ctime(), ' [', __name__, '::', __get_test_suite.__name__, '] :', ' 获取suite '
	print ('*' * 80)
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
	# print time.ctime(), ' [', __name__, '::', __Run_Case.__name__, '] :', ' 开始进行用例遍历 '
	# print '*' * 80
	L.logger.debug(' 循环遍历测试用例 ')
	# from src.lib.Utils import SQL
	# # sql实例化并传递
	# sql = SQL()
	# Q.set_sql(sql)
	# 循环遍历测试用例列表
	for case_list in case_sheet1[1:]:
		#判断是否是独有操作,如果不是对应平台的独有操作就跳过循环
		if str(case_list[4]).lower() != str(S.device['platformName']).lower() and len(case_list[4]) !=0:
			continue
		test_suite = __get_test_suite(case_list)
		runner.run(test_suite)
		# 插入用例名和设备udid
		# Q.sql.insert_per(case_list[0],S.device['udid'],'','','')

	wd=Element(driver)
	# wd.close_app()# 退出app
	wd.quit() # 退出服务
	# 生成测试报告
	RunExcel.get_html_report()

def Run_one(device,port,index):
	user_datas = [[768486, 768486, 768487], [768488, 768488, 768489], [768490, 768490, 768491]]
	Data.set_data(user_datas[index])
	S.set_device(device)

	from src.lib.Log import LogSignleton
	logsignleton = LogSignleton()
	logger = logsignleton.logger
	L.set_logger(logger)
	# 启动appium 服务
	A = Server()
	A.start_server(device, port)

	# print ('*' * 80)
	L.logger.debug(' 运行设备 device : %s  ' % device)
	# 实例化Dirver
	Dr = Driver(device, port)
	Dr.init()  # 初始化driver
	global driver
	driver = Dr.getDriver()
	D.set_driver(driver)
	# print ('*' * 80)
	L.logger.debug(' 运行设备 driver : %s  ' % driver)

	run_mode() # 运行模式

if __name__ == '__main__':
	try:
		# clean_process()
		G = GetDevices()
		devices = G.get_device()
		count = len(devices)
		ports = G.get_port(count)
		# print ('*' * 80)

		print (time.ctime()+' 设备数: %s' % count +', 端口列表: %s' % ports)
		p = Pool(processes=count) # set the processes max number 3

		# 多线程并发
		for i in range(count):
			result = p.apply_async(Run_one,(devices[i],ports[i],i,))

		p.close() # 关闭进程,不再添加新的进程
		p.join() # 进程等待执行完毕
		if result.successful():
			# print ('*' * 80)
			if count > 1:
				print( '多设备并发执行成功')
			else:
				print('单设备执行成功')
		clean_process()
	except Exception as e:
		raise e

	# print ('*' * 80)
	print( '所有代码执行完毕!')
	import sys
	sys.exit(0)
