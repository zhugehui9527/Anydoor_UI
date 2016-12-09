# -*- coding:utf-8 -*-
#######################################################
# filename:driver.py
# author:Jeff
# date:2016-09-21
# function:对日志进行操作处理
#######################################################
# from src.Global import *
# from src.Public.Public import *
from conf.Run_conf import read_config
from conf.Run_conf import load_config
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler
import logging, time
import threading,sys
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
# conf_path = '/Users/zengyuanchen/Documents/Project/Anydoor_UI/conf/monitor.ini'
# class MyLog(object):
# 	'''This class is used to get log'''
# 	log = None
# 	mutex = threading.Lock()
#
# 	def __init__(self):
# 		pass
#
# 	@staticmethod
# 	def get_logger():
# 		if MyLog.log is None:
# 			MyLog.mutex.acquire()
# 			MyLog.log = LogSignleton(conf_path)
# 			MyLog.mutex.release()
#
# 		return MyLog.log


class LogSignleton(object):
	def __init__(self):
		'''单例模式'''
		pass

	def __new__(cls):

		mutex = threading.Lock()
		mutex.acquire() #上锁,防止多线程下出问题
		if not hasattr(cls,'instance'):
			cls.instance = super(LogSignleton,cls).__new__(cls)
			# cls.instance.log_filename = read_config('logger','log_file')

			cls.instance.log_filename = read_config('logger','log_file')
			# if cls.instance.log_filename is not None: # 判断是否为目录
			# 	try:
			# 		# 返回的是文件名,不包括前面的路径
			# 		filename = os.path.basename(cls.instance.log_filename)
			# 		# 返回的是目录名,不包括文件名
			# 		filepath = os.path.dirname(cls.instance.log_filename)
			# 		print filepath
			# 		# splitext:分离文件名和后缀 split:分离文件路径和文件
			# 		parent_path, ext = os.path.splitext(filename)
			# 		# 定义时间显示格式
			# 		tm = time.strftime('%Y%m%d%H%M%S', time.localtime())
			# 		# 重新组装日志文件名
			# 		filename = parent_path + '_' + tm + ext
			# 		cls.instance.log_filename = filepath + '/' + filename
			# 	except Exception:
			# 		raise
			cls.instance.max_bytes_each = int(read_config('logger','max_bytes_each'))
			cls.instance.backup_count = int(read_config('logger','backup_count'))
			cls.instance.format = read_config('logger','format')
			cls.instance.log_level_in_console = int(read_config('logger','log_level_in_console'))
			cls.instance.log_level_in_logfile = int(read_config('logger','log_level_in_logfile'))
			cls.instance.logger_name = read_config('logger','logger_name')
			cls.instance.console_log_on = int(read_config('logger','console_log_on'))
			cls.instance.logfile_log_on = int(read_config('logger','logfile_log_on'))
			cls.instance.handles_mode = int(read_config('logger','handles_mode'))
			cls.instance.rw_mode = str(read_config('logger','rw_mode'))
			cls.instance.logger = logging.getLogger(cls.instance.logger_name)
			cls.instance.__config_logger()
		mutex.release() #释放锁
		return cls.instance

	def get_logger(self):
		return logging.getLogger(self.logger_name)

	def __config_logger(self):
		fmt = self.format.replace('|','%')
		formatter = logging.Formatter(fmt)
		if self.console_log_on == 1: #如果开启控制台日志
			console = logging.StreamHandler()
			console.setFormatter(formatter)
			self.logger.addHandler(console)
			self.logger.setLevel(self.log_level_in_console)

		if self.logfile_log_on == 1: #如果开启文件日志
			file_handle_dict = {'0':lambda :logging.FileHandler(self.log_filename,mode=self.rw_mode), #mode =a,接着日志继续写
			               '1':lambda :RotatingFileHandler(self.log_filename,maxBytes=self.max_bytes_each,backupCount=self.backup_count),
			               '2':lambda :TimedRotatingFileHandler(self.log_filename,when='D',interval=1)}
			
			if file_handle_dict.has_key(str(self.handles_mode)):
				file_handle = file_handle_dict[str(self.handles_mode)]()
			else:
				#不需要滚动,直接覆盖上一个日志
				file_handle = logging.FileHandler(self.log_filename)
			file_handle.setFormatter(formatter)
			self.logger.addHandler(file_handle)
			self.logger.setLevel(self.log_level_in_logfile)
			file_handle.close()
			
			#根据文件大小进行日志滚动:RotatingFileHandler
			# rt_file_handler = RotatingFileHandler(self.log_filename,maxBytes=self.max_bytes_each,backupCount=self.backup_count)
			# rt_file_handler.setFormatter(formatter)
			# self.logger.addHandler(rt_file_handler)
			# self.logger.setLevel(self.log_level_in_logfile)
			
			# #根据时间进行日志滚动:TimedRotatingFileHandler
			# tr_file_handler = TimedRotatingFileHandler(self.log_filename,when='D',interval=1)
			# tr_file_handler.setFormatter(formatter)
			# self.logger.addHandler(tr_file_handler)
			# self.logger.setLevel(self.log_level_in_logfile)
	
	
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
	@staticmethod
	def get_filter_log(logpath, casename, start_filter='', end_fileter=''):
		'''
		:desc:过滤日志,通过指定的日志路径logpath,开始过滤关键字:start_filter,结束关键字:end_fileter,过滤出日志并重新写入
			到以测试用例名称:casename 命名的日志路径中
		:param logpath:
		:param casename:
		:param start_filter:
		:param end_fileter:
		:return:
		'''
		log_file_path = os.path.split(logpath)[0]
		log_fileter_path = os.path.split(log_file_path)[0] + '/html/filter/{}.log'.format(casename)
		go_on_id = 0
		with open(log_fileter_path, 'w') as s:
			
			with open(logpath) as f:
				log_text = f.read()#读取整个log内容
				f.seek(0,0)#光标返回到行首
				kw_count = log_text.count(start_filter)
				print '过滤关键字: %s,包含个数 : %s' % (start_filter,str(kw_count))
				if kw_count > 0:
					for x in range(kw_count):
						for line in f:
							# 记录开始行
							if start_filter in line:
								go_on_id = 1
								s.write(line)
							elif go_on_id == 1:
								if end_fileter not in line:
									s.write(line)
								else:
									s.write(line)
									# go_on_id = 2
									#结束循环
									break
			f.close()
		s.close()
	
	# return log_fileter_path

#
# class MyLog(object):
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
# 			MyLog.log = None
# 			MyLog.mutex.release()
#
# 		return MyLog.log
		
	


if __name__ == '__main__':
	print os.path.realpath(sys.argv[0])
	prjDir = os.path.split(os.path.realpath(__file__))[0]
	print prjDir
	conf_path = os.path.join(prjDir, "monitor.ini")
	print conf_path
	# logsignleton = LogSignleton('/Users/zengyuanchen/Documents/Project/Anydoor_UI/conf/monitor.ini')
	# loggers = logsignleton.get_logger()
	#
	# loggers.info('测试')
	# loggers.debug('测试')
	# loggers.error('测试')
	# loggers.warning('测试')
	# loggers.critical('测试')
