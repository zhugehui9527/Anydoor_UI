# -*- coding:utf-8 -*-
#######################################################
#filename:Public.py
#author:Jeff
#date:2016-09-21
#function:对配置文件进行操作处理
#######################################################
import logging
import os
import ConfigParser

file = os.getcwd()
global logger
logger = logging.getLogger('main')

#加载配置文件
def load_config(file_name):
	config = ConfigParser.ConfigParser()
	try:
		if os.path.exists(file_name):
			config.read(file_name)
			return config
	except:
		print "%s is not exits",file_name

#读取cfg文件中的seciton区域中的某一个option值并返回该值
def read_config(file_name,section_name,option):
	monitor_cfg = load_config(file_name)
	for section in monitor_cfg.sections():
		if section == section_name:
			value = monitor_cfg.get(section,option)
			return value










#
# logging.debug('debug_log')
# logging.info('info_log')
# logging.warning('warnging_log')
# logging.error('error_log')
# logging.critical('critical_log')
# log = logging.getLogger('root')
# print log.propagate
#
# try:
# 	raise Exception ,u'参数错误'
# except:
# 	log.exception('excepiton')
# class Log():
# 	def __init__(self):
# 		#获取当前项目的路径
# 		projectPath = os.getcwd()
# 		logpath = projectPath + '/output/log/'
# 		logging.basicConfig(level=logging.debug(),
# 		                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
# 		                    datefmt='%a, %d %b %Y %H:%M:%S',
# 		                    filename=os.path.join(logpath,'AnyDoor_UI.log'),
# 		                    filemode='w')
#
# 	def wlog(self):
# 		log = logging.getLogger()
# 		log.debug('debug_log')
# 		log.info('info_log')
# 		log.warning('warnging_log')
# 		log.error('error_log')
# 		log.critical('critical_log')
#
# if __name__ == '__main__':
# 	# 获取当前项目的路径
# 	projectPath = os.getcwd()
# 	logpath = projectPath + '/output/log/'
# 	logging.basicConfig(level=logging.DEBUG,
# 	                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
# 	                    datefmt='%a, %d %b %Y %H:%M:%S',
# 	                    filename=os.path.join(logpath, 'AnyDoor_UI.log'),
# 	                    filemode='w')
#
# 	log = logging.getLogger('root')
# 	log.debug('debug_log')