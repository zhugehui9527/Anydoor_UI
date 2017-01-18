# -*- coding:utf-8 -*-
#######################################################
#filename:Utils.py
#author:Jeff
#date:2016-12-12
#function:常用模块封装
import subprocess
import threading
import os
from conf.Run_conf import read_config

class Utils:
	def __init__(self):
		pass
	
	@staticmethod
	def cmd_subprocess(cmd):
		'''执行shell命令'''
		return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
	@staticmethod
	def cmd_output(cmd):
		return subprocess.check_output(cmd)
	
	
			
class cmd_tt(threading.Thread):
	'''
	run cmd on mac
	'''
	def __init__(self, cmd):
		threading.Thread.__init__(self)
		self.cmd = cmd

	def run(self):
		os.system(self.cmd)
		
	# def cmd_Popen(self):
	# 	os.popen(self.cmd)
		
if __name__ == '__main__':
	cmd = 'appium -v'
	t=Utils.cmd_subprocess(cmd).communicate()
	for i in  t:
		print i
		