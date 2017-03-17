# -*- coding:utf-8 -*-
#######################################################
#filename:Global.py
#author:Jeff
#date:2016-09-21
#function:处理全局文件变量
#######################################################
import os,time
import sys
sys.path.append("../../")

class D:
	'''传递driver'''
	driver = None
	@classmethod
	def set_driver(cls,driver):
		if driver:
			cls.driver = driver
		print '*'*80
		print time.ctime(), ' [', __name__, '::', D.set_driver.__name__, '] :', ' driver =  ', driver
		
		
	
class L:
	'''传递logger'''
	logger = None
	@classmethod
	def set_logger(cls,logger):
		if logger:
			cls.logger = logger
		else:
			print time.ctime(), ' [', __name__, '::',L.set_logger.__name__, '[ error ] logger is null'
		
class S:
	device = None
	@classmethod
	def set_device(cls,device):
		'''传递device'''
		if device:
			cls.device = device
			device_dir = os.path.abspath('./output/'+ cls.device['udid'])
			# print '* [', __name__, '::', S.set_device.__name__, '] :', ' device_dir = ',device_dir
			log_dir = os.path.abspath(device_dir + '/log')
			report_dir = os.path.abspath(device_dir + '/html/filter')
			screen_dir = os.path.abspath(device_dir + '/screen')
			cls.mkdirs(log_dir)
			cls.mkdirs(report_dir)
			cls.mkdirs(screen_dir)
		
	@classmethod
	def mkdirs(cls,path):
		'''创建目录'''
		if not os.path.exists(path):
			os.makedirs(path,0777)

class Q:
	'''传递sql'''
	sql = None
	@classmethod
	def set_sql(cls,sql):
		cls.sql = sql