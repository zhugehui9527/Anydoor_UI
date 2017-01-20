# -*- coding:utf-8 -*-
#######################################################
#filename:Global.py
#author:Jeff
#date:2016-09-21
#function:处理全局文件变量
#######################################################
import os,time
class D:
	driver = None
	@classmethod
	def set_driver(cls,driver):
		print '*'*80
		print time.ctime(), ' [', __name__, '::', D.set_driver.__name__, '] :', ' driver =  ', driver
		cls.driver = driver
	
class L:
	logger = None
	@classmethod
	def set_logger(cls,logger):
		if logger:
			cls.logger = logger
		else:
			print time.ctime(), ' [', __name__, '::',L.set_logger.__name__, '[ error ] logger is null'
		
class S:
	device = None
	from conf.Run_conf import read_config
	project_path = read_config('testcase','project_path')
	
	@classmethod
	def set_device(cls,device):
		if device:
			cls.device = device
			device_dir = cls.project_path +'/output/'+ cls.device['udid']
			# print '* [', __name__, '::', S.set_device.__name__, '] :', ' device_dir = ',device_dir
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
