# -*- coding:utf-8 -*-
#######################################################
#filename:Run_Unittest.py
#author:Jeff
#date:2016-09-21
#function:对日志进行操作处理
#######################################################
from Global import *
from Public.Log import *
from conf.Run_conf import *
from multiprocessing import Process
import threading
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

class AppiumServer(object):
	def __init__(self):
		global config_path,start_appium,serverIp,serverport
		config_path = '/Users/zengyuanchen/Documents/Project/Anydoor_UI/conf/monitor.ini'
		start_appium = read_config(config_path,'command','start_appium')
		serverIp = read_config(config_path,'appium','ip')
		serverport = read_config(config_path, 'appium', 'port')

	def start_server(self):
		t1 = RunServerOnMac(start_appium)
		p = Process(target=t1.start())
		p.start()
		logger.debug('服务启动完毕')

	def is_runnnig(self):
		"""Determine whether server is running
			:return:True or False
			"""
		response = None
		url = 'http://'+ serverIp +':'+serverport+ "/wd/hub/status"
		print url
		try:
			# response = urllib2.request_host(url)
			# response = urllib.request.urlopen(url, timeout=5)
			response = requests.get(url)
			response_dict = json.loads(response.text)
			if response_dict['status'] == 0:
				return True
			else:
				return False
		except URLError:
			return False
		finally:
			if response:
				response.close()

class RunServerOnMac(threading.Thread):

	def __init__(self, cmd):
		threading.Thread.__init__(self)
		self.cmd = cmd

	def run(self):
		print self.cmd
		os.system(self.cmd)

if __name__ == 'main':
	# appiumserver = AppiumServer()
	# appiumserver.start_server()
	os.system('appium -a 127.0.0.1 -p 4723')