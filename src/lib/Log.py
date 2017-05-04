# -*- coding:utf-8 -*-
#######################################################
# filename:Log.py
# author:Jeff
# date:2016-09-21
# function:对日志进行操作处理
#######################################################

from conf.Run_conf import read_config
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler
from src.Public.Global import S
import logging, time
import os,sys
sys.path.append("../../")

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

device = S.device
udid = device['udid']

class LogSignleton(object):
	def __init__(self):
		self.log_filename = PATH('../../output/{}/log/AnyDoor_UI.log'.format(udid))
		self.max_bytes_each = int(read_config('logger', 'max_bytes_each'))
		self.backup_count = int(read_config('logger', 'backup_count'))
		self.format = read_config('logger', 'format')
		self.log_level_in_console = int(read_config('logger', 'log_level_in_console'))
		self.log_level_in_logfile = int(read_config('logger', 'log_level_in_logfile'))
		self.logger_name = read_config('logger', 'logger_name')
		self.console_log_on = int(read_config('logger', 'console_log_on'))
		self.logfile_log_on = int(read_config('logger', 'logfile_log_on'))
		self.handles_mode = int(read_config('logger', 'handles_mode'))
		self.rw_mode = str(read_config('logger', 'rw_mode'))
		self.logger = logging.getLogger(self.log_filename)
		self.__config_logger()

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

	@staticmethod
	def get_filter_log(casename, start_filter='', end_fileter=''):
		'''
		:desc:过滤日志,通过指定的日志路径logpath,开始过滤关键字:start_filter,结束关键字:end_fileter,过滤出日志并重新写入
			到以测试用例名称:casename 命名的日志路径中
		:param logpath:
		:param casename:
		:param start_filter:
		:param end_fileter:
		:return:
		'''
		logpath = PATH('../../output/{}/log/AnyDoor_UI.log'.format(udid))
		log_filter_path = PATH('../../output/{}/html/filter/{}.log'.format(udid,casename))
		# print log_filter_path
		# from Utils import SQL
		# S = SQL()
		# S.insert_per(casename,udid,)
		go_on_id = 0
		with open(log_filter_path, 'w') as s:
			with open(logpath) as f:
				log_text = f.read()#读取整个log内容
				f.seek(0,0)#光标返回到行首
				kw_count = log_text.count(start_filter)
				print time.ctime(), ' [', __name__, '::', LogSignleton.get_filter_log.__name__, '] :', '过滤关键字: %s,包含个数 : %s' % (start_filter,str(kw_count))
				if kw_count > 0:
					for x in range(kw_count):
						for line in f:
							# line = line
							# 记录开始行
							if start_filter in line:
								go_on_id = 1
								s.write('<br>')
								s.write(line)
								# s.write('</br>')
							elif go_on_id == 1:
								if end_fileter not in line:
									s.write('<br>')
									s.write(line)
									# s.write('</br>')
								else:
									s.write('<br>')
									s.write(line)
									# s.write('</br>')
									# go_on_id = 2
									#结束循环
									break
			f.close()
		s.close()

if __name__ == '__main__':
	pass
