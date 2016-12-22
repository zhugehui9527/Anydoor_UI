# -*- coding:utf-8 -*-
#######################################################
# filename:AppiumServer.py
# author:Jeff
# date:2016-09-21
# function:对appium服务进行操作处理
#######################################################
import json
import requests
import os, time
from conf.Run_conf import read_config
from multiprocessing import Pool
from src.lib.Utils import Utils

class AppiumServer(object):
	def __init__(self):
		self.serverIp = read_config('appium', 'ip')
		self.serverport = int(read_config('appium', 'port'))
		self.utils = Utils()
	
	def pool_run(self):
		'''
		线程池启动多线程
		:return:
		'''
		# result = []
		devices = self.utils.get_device()
		# print devices
		count = len(devices)
		
		pool = Pool(processes=count)
		pool_list = self.get_port(count)
		# 启动多个服务
		for i in range(count):
			self.start_server(devices[i],pool_list[i])
			# pool.apply_async(self.start_server, args=(devices[i], pool_list[i]))
		pool.close()
		pool.join()
		# for res in result:
		# 	print 'pool 运行结果: ' + str(res)
	
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
				# 启动appium服务
				cmd_str = 'appium -a {} -p {} -U {}'.format(self.serverIp,Port,device['udid'])
				print '启动命令: ' + cmd_str
				self.utils.cmd_subprocess(cmd_str)
				time.sleep(10)
				i = 0
				while not self.is_runnnig(Port):
					time.sleep(2)
					i = i + 2
					# 五分钟后超时跳出循环
					if i > 300:
						break
			except Exception as e:
				raise e
		else:
			print '端口: %d 已正常启动' % Port
		
	def run_server(self,device,port):
		self.start_server(device,port)
		from src.lib.Driver import Driver
		D = Driver(device,port)
		driver = D.get_driver()
		
	def is_using(self, port):
		'''
		detect whether port is using
		:param port:
		:return:
		'''
		cmd = "netstat -an | grep %s" % str(port)
		if os.popen(cmd).readlines():
			return True
		else:
			return False
	
	def get_port(self, count):
		'''
		get appium free port
		:return:
		'''
		port_list = []
		while True:
			if len(port_list) == count:
				break
			if not self.is_using(self.serverport) and (self.serverport not in port_list):
				port_list.append(self.serverport)
			else:
				self.serverport += 1
		# print '端口列表: %s' % port_list
		return port_list
	
	def is_runnnig(self, Port):
		"""Determine whether server is running
			:return:True or False
		"""
		response = None
		url = 'http://' + self.serverIp + ':' + str(Port) + "/wd/hub/status"
		# print '获取status 的地址: %s' % url
		# logger.debug('获取status 的地址: %s' % url)
		try:
			# response = urllib2.request_host(url)
			# response = urllib.request.urlopen(url, timeout=5)
			response = requests.get(url)
			response_dict = json.loads(response.text)
			print '启动服务响应: ', response_dict
			# logger.debug('响应信息: %s' % response_dict)
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
	port = 4723
	device = {'platformVersion': '10.1', 'deviceName': 'iPhone 5s'}
	appiumserver = AppiumServer()
	# appiumserver.start_server(device,port)
	# print appiumserver.get_port(2)
	appiumserver.start_server(device, port)
	# appiumserver.pool_run()
	print '*' * 40
