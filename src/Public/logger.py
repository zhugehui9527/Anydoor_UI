# -*- coding:utf-8 -*-
#######################################################
#filename:driver.py
#author:Jeff
#date:2016-09-21
#function:对日志进行操作处理
#######################################################
import logging
import os
import time

from src.Public.Public import *


def GenerateLog(log_file):
	logger.setLevel(logging.DEBUG)
	#判断是否为目录
	try :
		#返回的是文件名,不包括前面的路径
		filename = os.path.basename(log_file)
		#返回的是目录名,不包括文件名
		filepath = os.path.dirname(log_file)
		#splitext:分离文件名和后缀 split:分离文件路径和文件
		parent_path,ext = os.path.splitext(filename)
		#定义时间显示格式
		tm = time.strftime('%Y%m%d%H%M%S',time.localtime())
		#重新组装日志文件名
		filename = parent_path + '_' +tm + ext
	except Exception as e:
		raise e

	#handler
	#设置日志输出到指定文件
	logfile = logging.FileHandler(os.path.join(filepath,filename))
	#设置日志级别
	logfile.setLevel(logging.DEBUG)
	#设置日志输出到控制台
	control = logging.StreamHandler()
	#设置日志级别
	control.setLevel(logging.DEBUG)

	#formatter
	#设置日志输出格式
	formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s')
	#设置日志输出到指定文件时的格式
	logfile.setFormatter(formatter)
	#设置日志输出到控制台时的格式
	control.setFormatter(formatter)

	#绑定
	logger.addHandler(control)
	logger.addHandler(logfile)
	pass




# class Log():
# 	def __init__(self):
# 		#读取log配置信息
# 		project_path = os.getcwd()
# 		self.log_path = os.path.join((project_path + '/output/log/'), 'AnyDoor_UI.log')
# 		self.config_path = os.path.join((project_path + '/conf/'), 'monitor.ini')
# 		self.log_level = read_config(self.config_path, 'logger', 'level')
# 		# self.log_format = read_config(self.config_path, 'logger', 'format')
# 		self.log_datefmt = read_config(self.config_path, 'logger', 'datefmt')
# 		self.log_filemode = read_config(self.config_path, 'logger', 'filemode')
# 		self.log_keys = read_config(self.config_path, 'logger', 'keys')
# 		#将读取的log配置信息加载进logging使之生效
# 		logging.basicConfig(filename=self.log_path,
# 		                    level=self.log_level,
# 		                    format='%(asctime)s : %(filename)s[line:%(lineno)d] [ %(levelname)s ] %(message)s',
# 		                    datefmt=self.log_datefmt,
# 		                    filemode=self.log_filemode)
#
# 	#实例化并返回一个logger对象
# 	def instance(self):
# 		# global logger
# 		if logger is None:
# 			load_config(self.config_path)
# 			logger  = logging.getLogger(self.log_keys)
# 			return logger
#
# 	def debug(self,msg):
# 		return self.instance().debug(msg)
#
# 	def info(self,msg):
# 		return self._instance().info(msg)
#
# 	def warning(self,msg):
# 		return self._instance().warning(msg)
#
# 	def error(self,msg):
# 		return self._instance().error(msg)
#
# 	def critical(self,msg):
# 		return self._instance().critical(msg)


if __name__ == '__main__':
	project_path = os.getcwd()
	log_path = os.path.join((project_path + '/output/log/'), 'AnyDoor_UI.log')
	GenerateLog(log_path)
	logger.debug('测试')
	logger.info('测试')
	logger.error('测试')
	logger.warning('测试')
	logger.critical('测试')
