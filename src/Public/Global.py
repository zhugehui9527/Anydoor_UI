# -*- coding:utf-8 -*-
#######################################################
#filename:Global.py
#author:Jeff
#date:2016-09-21
#function:处理全局文件变量
#######################################################
import os
class D:
	# from src.lib.Driver import MyDriver
	# driver = MyDriver.get_driver()
	driver = None
	@classmethod
	def set_driver(cls,driver):
		cls.driver = driver
	
class L:

	# from src.lib.Log import LogSignleton
	# logsignleton = LogSignleton()
	# logger = logsignleton.logger
	logger = None
	@classmethod
	def set_logger(cls,logger):
		cls.logger = logger
		
class S:
	device = None
	from conf.Run_conf import read_config
	project_path = read_config('testcase','project_path')
	
	@classmethod
	def set_device(cls,device):
		if device:
			cls.device = device
			device_dir = cls.project_path +'/output/'+ cls.device['udid']
			log_dir = device_dir + '/log'
			report_dir = device_dir + '/html/filter'
			screen_dir = device_dir + '/screen'
			cls.mkdirs(log_dir)
			cls.mkdirs(report_dir)
			cls.mkdirs(screen_dir)
		
	@classmethod
	def mkdirs(cls,path):
		if not os.path.exists(path):
			os.makedirs(path,0777)
