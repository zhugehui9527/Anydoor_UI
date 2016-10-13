# -*- coding:utf-8 -*-
#######################################################
#filename:Run_conf.py
#author:Jeff
#date:2016-09
#function:运行加载配置数据
#######################################################
import os
import ConfigParser
global conf_path
prjDir = os.path.split(os.path.realpath(__file__))[0]
conf_path = os.path.join(prjDir, "monitor.ini")


# def get_conf_path():
# 	conf_path = []
# 	path = os.getcwd() + '/monitor.ini'
# 	conf_path.append(path)
# 	print conf_path[0]
# 	return conf_path[0]
#加载配置文件
def load_config(file_path):
	config = ConfigParser.ConfigParser()
	try:
		if os.path.exists(file_path):
			config.read(file_path)
			return config
	except:
		print "%s is not exits",file_path

#读取cfg文件中的seciton区域中的某一个option值并返回该值
def read_config(section_name,option):
	monitor_cfg = load_config(conf_path)
	for section in monitor_cfg.sections():
		if section == section_name:
			value = monitor_cfg.get(section,option)
			return value

'''
from src.Public.Log import *
import os


Case_file = '..\\TestCase\\TestCase.xlsx'
conf_file = '..\\monitor.ini'
report_file = '..\\output\\html\\Test_Report_Filename.html'
log_file ='..\\output\\log\\AnyDoor_UI.log'

conf_path = os.getcwd() + '/monitor.ini'

def get_path():
	current_path = os.getcwd()
	return current_path


if __name__ == '__main__':
	print 'TestCase Running...'
	logsignleton = LogSignleton(conf_path)
	logger = logsignleton.get_logger()
	logger.debug('test')
	print os.path.abspath(conf_file)
	print os.path.abspath(Case_file)
	# Run_TestCase.run_testcase(data_file, conf_file, report_file)
	print 'TestCase Run End....'
	# print conf_path

'''