# -*- coding:utf-8 -*-
#######################################################
# filename:driver.py
# author:Jeff
# date:2016-09-21
# function:对日志进行操作处理
#######################################################
from src.Global import *
from src.Public.Public import *
import logging, time
import threading


class Log():
	def __init__(self):
		project_path = '/Users/zengyuanchen/Documents/Project/Anydoor_UI'
		log_file = os.path.join((project_path + '/output/log/'), 'AnyDoor_UI.log')
		global logger
		logger = logging.getLogger('main')
		self.logger = logger
		self.log_file = log_file

	# self.logger.setLevel(logging.DEBUG)

	# 传入日志路径并进行处理
	def GenerateLog(self):
		log_file = self.log_file
		# 判断是否为目录
		try:
			# 返回的是文件名,不包括前面的路径
			filename = os.path.basename(log_file)
			# 返回的是目录名,不包括文件名
			filepath = os.path.dirname(log_file)
			# splitext:分离文件名和后缀 split:分离文件路径和文件
			parent_path, ext = os.path.splitext(filename)
			# 定义时间显示格式
			tm = time.strftime('%Y%m%d%H%M%S', time.localtime())
			# 重新组装日志文件名
			filename = parent_path + '_' + tm + ext
		except Exception as e:
			raise e

		# handler
		# 设置日志输出到指定文件
		logfile = logging.FileHandler(os.path.join(filepath, filename))
		# 设置日志级别
		logfile.setLevel(logging.DEBUG)
		# 设置日志输出到控制台
		control = logging.StreamHandler()
		# 设置日志级别
		control.setLevel(logging.DEBUG)

		# formatter
		# 设置日志输出格式
		formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s')
		# 设置日志输出到指定文件时的格式
		logfile.setFormatter(formatter)
		# 设置日志输出到控制台时的格式
		control.setFormatter(formatter)

		# 绑定
		self.logger.addHandler(control)
		self.logger.addHandler(logfile)
		pass

	def get_my_logger(self):
		"""get the logger
		:return:logger
		"""
		return self.logger

	def get_log_path(self):
		return self.log_file


class MyLog:
	"""
    This class is used to get log
    lock log
    """

	log = None
	mutex = threading.Lock()

	def __init__(self):
		pass

	@staticmethod
	def get_log():
		if MyLog.log is None:
			MyLog.mutex.acquire()
			# logpath = Log().get_log_path()
			MyLog.log = Log().GenerateLog()
			MyLog.mutex.release()

		return MyLog.log


if __name__ == '__main__':
	logtest = Log()
	logtest.GenerateLog()
	loggers = logtest.get_my_logger()

	loggers.info('测试')
	loggers.debug('测试')
	loggers.error('测试')
	loggers.warning('测试')
	loggers.critical('测试')
