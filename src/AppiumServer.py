# -*- coding:utf-8 -*-
#######################################################
#filename:Run_Unittest.py
#author:Jeff
#date:2016-09-21
#function:对日志进行操作处理
#######################################################
import json
import os
import subprocess
import sys
import threading

import requests

from conf.Run_conf import read_config
from src.Public.Global import L

reload(sys)
sys.setdefaultencoding('utf-8')

logger = L.logger
class RunServerOnMac(threading.Thread):
	'''
	run cmd on mac
	'''
	def __init__(self, cmd):
		threading.Thread.__init__(self)
		self.cmd = cmd

	def run(self):
		logger.debug('命令: %s' % self.cmd)
		os.system(self.cmd)

class AppiumServer(object):
	def __init__(self):
		# self.start_appium = read_config('command','start_appium')
		self.serverIp = read_config('appium','ip')
		self.serverport = str(read_config('appium', 'port'))

	def start_server(self):
		# print 'start_server 。。。'
		if not self.is_runnnig():
			try:
				
				import os,time
				
				cmd_str = 'appium -a {} -p {} -bp 4700'.format(self.serverIp,self.serverport)
				print cmd_str
				cmd(cmd_str)
				time.sleep(20)
				# while not self.is_runnnig():
				# 	time.sleep(2)
				# 	print 'sleep 2s'
				return self.serverport
			except Exception as e:
				raise e
		else:
			logger.debug('服务已正常启动')
			# print '服务已正常启动'
		
	def main(self):
		return self.start_server()
	
	def is_runnnig(self):
		"""Determine whether server is running
			:return:True or False
			"""
		response = None
		url = 'http://'+ self.serverIp +':'+ self.serverport + "/wd/hub/status"
		# print '获取status 的地址: %s' % url
		logger.debug('获取status 的地址: %s' % url)
		try:
			# response = urllib2.request_host(url)
			# response = urllib.request.urlopen(url, timeout=5)
			response = requests.get(url)
			response_dict = json.loads(response.text)
			print '响应',response_dict
			logger.debug('响应信息: %s' % response_dict)
			if response_dict['status'] == 0:
				return True
			else:
				return False
		except:
			return False
		finally:
			if response:
				response.close()
				
def cmd(cmd):
	return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


		
if __name__ == 'main':
	appiumserver = AppiumServer()
	appiumserver.main()
	