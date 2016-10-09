# -*- coding:utf-8 -*-
#######################################################
# filename:driver.py
# author:Jeff
# date:2016-09-21
# function:对日志进行操作处理
#######################################################
from src.Global import *
from src.Public.Public import *
from logging.handlers import RotatingFileHandler
import logging, time
import threading


class LogSignleton(object):
	'''单例模式'''
	def __init__(self,log_config):
		pass

	def __new__(cls,log_config):

		mutex = threading.Lock()
		mutex.acquire() #上锁,防止多线程下出问题
		if not hasattr(cls,'instance'):
			cls.instance = super(LogSignleton,cls).__new__(cls)
			cls.instance.log_filename = read_config(log_config,'logger','log_file')
			if cls.instance.log_filename is not None: # 判断是否为目录
				try:
					# 返回的是文件名,不包括前面的路径
					filename = os.path.basename(cls.instance.log_filename)
					# 返回的是目录名,不包括文件名
					filepath = os.path.dirname(cls.instance.log_filename)
					print filepath
					# splitext:分离文件名和后缀 split:分离文件路径和文件
					parent_path, ext = os.path.splitext(filename)
					# 定义时间显示格式
					tm = time.strftime('%Y%m%d%H%M%S', time.localtime())
					# 重新组装日志文件名
					filename = parent_path + '_' + tm + ext
					cls.instance.log_filename = filepath + '/' + filename
				except Exception as e:
					raise
			cls.instance.max_bytes_each = int(read_config(log_config,'logger','max_bytes_each'))
			cls.instance.backup_count = int(read_config(log_config,'logger','backup_count'))
			cls.instance.format = read_config(log_config,'logger','format')
			cls.instance.log_level_in_console = int(read_config(log_config,'logger','log_level_in_console'))
			cls.instance.log_level_in_logfile = int(read_config(log_config,'logger','log_level_in_logfile'))
			cls.instance.logger_name = read_config(log_config,'logger','logger_name')
			cls.instance.console_log_on = int(read_config(log_config,'logger','console_log_on'))
			cls.instance.logfile_log_on = int(read_config(log_config,'logger','logfile_log_on'))
			cls.instance.logger = logging.getLogger(cls.instance.logger_name)
			cls.instance.__config_logger()
		mutex.release() #释放锁
		return cls.instance

	def get_logger(self):
		return self.logger


	def __config_logger(self):
		fmt = self.format.replace('|','%')
		formatter = logging.Formatter(fmt)
		if self.console_log_on == 1: #如果开启控制台日志
			console = logging.StreamHandler()
			console.setFormatter(formatter)
			self.logger.addHandler(console)
			self.logger.setLevel(self.log_level_in_console)

		if self.logfile_log_on == 1: #如果开启文件日志
			rt_file_handler = RotatingFileHandler(self.log_filename,maxBytes=self.max_bytes_each,backupCount=self.backup_count)
			rt_file_handler.setFormatter(formatter)
			self.logger.addHandler(rt_file_handler)
			self.logger.setLevel(self.log_level_in_logfile)

	# 	# 传入日志路径并进行处理
	# 	log_file = self.log_file
	# 	# 判断是否为目录
	# 	try:
	# 		# 返回的是文件名,不包括前面的路径
	# 		filename = os.path.basename(log_file)
	# 		# 返回的是目录名,不包括文件名
	# 		filepath = os.path.dirname(log_file)
	# 		# splitext:分离文件名和后缀 split:分离文件路径和文件
	# 		parent_path, ext = os.path.splitext(filename)
	# 		# 定义时间显示格式
	# 		tm = time.strftime('%Y%m%d%H%M%S', time.localtime())
	# 		# 重新组装日志文件名
	# 		filename = parent_path + '_' + tm + ext
	# 	except Exception as e:
	# 		raise e
	#
	# 	# handler
	# 	# 设置日志输出到指定文件
	# 	logfile = logging.FileHandler(os.path.join(filepath, filename))
	# 	# 设置日志级别
	# 	logfile.setLevel(logging.DEBUG)
	# 	# 设置日志输出到控制台
	# 	control = logging.StreamHandler()
	# 	# 设置日志级别
	# 	control.setLevel(logging.DEBUG)
	#
	# 	# formatter
	#
	# 	# 设置日志输出格式
	# 	formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s')
	# 	# 设置日志输出到指定文件时的格式
	# 	logfile.setFormatter(formatter)
	# 	# 设置日志输出到控制台时的格式
	# 	control.setFormatter(formatter)
	#
	# 	# 绑定
	# 	self.logger.addHandler(control)
	# 	self.logger.addHandler(logfile)
	# 	pass
	# #
	# def get_my_logger(self):
	# 	"""get the logger
	# 	:return:logger
	# 	"""
	# 	return self.logger
	#
	# def get_log_path(self):
	# 	return self.log_file

#
# class MyLog:
# 	"""
#     This class is used to get log
#     lock log
#     """
#
# 	log = None
# 	mutex = threading.Lock()
#
# 	def __init__(self):
# 		pass
#
# 	@staticmethod
# 	def get_log():
# 		if MyLog.log is None:
# 			MyLog.mutex.acquire()
# 			# logpath = Log().get_log_path()
# 			MyLog.log = Log().GenerateLog()
# 			MyLog.mutex.release()
#
# 		return MyLog.log


if __name__ == '__main__':
	logsignleton = LogSignleton('/Users/zengyuanchen/Documents/Project/Anydoor_UI/conf/monitor.ini')
	loggers = logsignleton.get_logger()

	loggers.info('测试')
	loggers.debug('测试')
	loggers.error('测试')
	loggers.warning('测试')
	loggers.critical('测试')
