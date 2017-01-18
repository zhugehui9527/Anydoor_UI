# -*- coding:utf-8 -*-
#######################################################
# filename:AppiumServer.py
# author:Jeff
# date:2016-09-21
# function:对appium服务进行操作处理
#######################################################
import json
import requests
import time
from conf.Run_conf import read_config
from src.lib.Utils import Utils as U

class AppiumServer(object):
	def __init__(self):
		self.serverIp = read_config('appium', 'ip')

	def start_server(self, device, Port):
		'''
		启动appium服务
		:param device:dict 类型的设备信息
		:param Port:int 类型
		:return:
		'''
		# print '启动appium'
		if not self.is_runnnig(Port):
			try:
				
				cmd_str = 'appium -a {} -p {} -U {}'.format(self.serverIp,Port,device['udid'])
				print '*' * 80
				print time.ctime(),' [', __name__, '::', self.start_server.__name__, '] :','*  启动appium命令: ' + cmd_str
				print '*' * 80
				U.cmd_subprocess(cmd_str) # 启动appium服务
				# U.cmd_output(cmd_str)
				# import os
				# os.system(cmd_str)

				i = 0
				while not self.is_runnnig(Port):
					time.sleep(2)
					i = i + 2
					# 五分钟后超时跳出循环
					if i > 30:
						break
				else:
					print '*'*80
					print time.ctime(), ' [', __name__, '::', self.start_server.__name__, '] :', ' 启动appium成功,Port: ',Port
			except Exception as e:
				print 'device 中 未找到 [ udid ]'
				raise e
		else:
			print '*' * 80
			print time.ctime(), ' [', __name__, '::', self.start_server.__name__, '] :', '端口: %d 已正常启动' % Port

	def is_runnnig(self, Port):
		"""Determine whether server is running
			:return:True or False
		"""
		response = None
		url = 'http://' + self.serverIp + ':' + str(Port) + "/wd/hub/status"

		try:
		
			response = requests.get(url)
			response_dict = json.loads(response.text)
	
			if response_dict['status'] == 0:
				return True
			else:
				return False
		except:
			return False
		finally:
			if response:
				response.close()
	
	


if __name__ == '__main__':
	print '*' * 40
	print '*' * 40
