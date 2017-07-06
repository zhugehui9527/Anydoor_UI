# -*- coding:utf-8 -*-
#######################################################
# filename:Server.py
# author:Jeff
# date:2016-09-21
# function:对appium服务进行操作处理
#######################################################
import json
import requests
import time
from conf.Run_conf import read_config
from src.lib.Utils import Utils as U
from src.Public.Common import public as pc
from src.Public.Common import desired_caps as dc
from src.Public.Global import L

class Server(object):
	def __init__(self):
		self.serverIp = read_config(pc.appium, dc.ip)
		self.runmode = read_config(pc.runmode, pc.driver)
		L.logger.info('runmode = %s' % str(self.runmode))
	def start_server(self, device, Port):
		'''
		启动服务
		:param device:dict 类型的设备信息
		:param Port:int 类型
		:return:
		'''
		if not self.is_runnnig(Port):
			try:
				if self.runmode == pc.appium:
					cmd_str = 'appium -a {} -p {} -bp {} -U {}'.format(self.serverIp,Port,(Port+1),device['udid'])
				else:
					cmd_str = 'macaca server --verbose -p {}'.format(Port)
				# print ('*' * 80)
				# print (time.ctime(),' [', __name__, '::', self.start_server.__name__, '] :','*  启动命令: ' + cmd_str)
				L.logger.info('启动命令 : %s' % str(cmd_str))
				# print '*' * 80
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
					# print ('*'*80)
					# print (time.ctime(), ' [', __name__, '::', self.start_server.__name__, '] :', ' 启动成功,Port: ',Port)
					L.logger.info('启动成功 ,Port: %s' % str(Port))
			except Exception as e:
				# print ('device 中 未找到 [ udid ]')
				L.logger.warning('device 中 未找到 [ udid ]')
				raise e
		else:
			# print ('*' * 80)
			# print (time.ctime(), ' [', __name__, '::', self.start_server.__name__, '] :', '端口: %d 已正常启动' % Port)
			L.logger.info('端口: %d 已正常启动' % Port)

	def is_runnnig(self, Port):
		"""Determine whether server is running
			:return:True or False
		"""
		response = None
		# if self.runmode == pc.macaca:
		# 	url = 'http://' + self.serverIp + ':' + '8900' + "/wd/hub/status"
		# else:
		# 	url = 'http://' + self.serverIp + ':' + str(Port) + "/wd/hub/status"
		url = 'http://' + self.serverIp + ':' + str(Port) + "/wd/hub/status"
		try:

			response = requests.get(url)
			response_dict = json.loads(response.text)
			# print (time.ctime(), ' [', __name__, '::', self.is_runnnig.__name__, '] :','服务响应: ',response_dict)
			L.logger.info('服务响应: %s' % response_dict)
			# if response_dict['status'] == 0 and self.runmode ==pc.appium :
			# 	return True
			# elif response_dict['status'] == 1 and self.runmode == pc.macaca:
			if str(response.status_code).startswith('2'):
				return True
			else:
				return False
		except:
			return False
		finally:
			if response:
				response.close()

