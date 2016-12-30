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
from src.lib.Utils import Utils

class AppiumServer(object):
	def __init__(self):
		self.serverIp = read_config('appium', 'ip')
		self.serverport = int(read_config('appium', 'port'))
		self.Get_Android = 'adb devices'
		self.Get_iOS = 'instruments -s devices'
		self.utils = Utils()

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
				print '*' * 80
				print '* [', __name__, '::', self.start_server.__name__, '] :','*  启动appium命令: ' + cmd_str
				print '*' * 80
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
				print 'device 中 未找到 [ udid ]'
				raise e
		else:
			print '端口: %d 已正常启动' % Port

		
		
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
			# print '*' * 80
			print '* [', __name__, '::', self.start_server.__name__, '] :','启动服务响应: ', response_dict
			print '*' * 80
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
	
	def get_device(self):
		'''
		获取真实设备列表
		:param deviceName:
		:param deviceType:
		:return:
		'''
		# 存储设备信息
		device = []
		iOS = {}
		Android = {}
		iOS_Monitor = {}
		# value_ios = os.popen(self.Get_iOS)
		isMonitor = eval(read_config('appium', 'isMonitor'))
		# 获取模拟器设备列表
		if isMonitor:
			deviceName = read_config('appium', 'deviceName')
			platformVersion = read_config('appium', 'platformVersion')
			iOS_Monitor['deviceName'] = deviceName
			iOS_Monitor['platformVersion'] = platformVersion
			for dev in os.popen(self.Get_iOS):
				dev_value = dev.split()
				if dev.rfind(deviceName) == -1:
					continue
				if dev.rfind(platformVersion) == -1:
					continue
				iOS_Monitor['udid'] = dev_value[3][1:-1]
				iOS_Monitor['platformName'] = 'iOS'
			device.append(iOS_Monitor)
		else:
			pass
		# 是否运行真机
		isRealDevice = eval(read_config('appium', 'isRealDevice'))
		if isRealDevice:
			# 获取iOS真实设备列表
			for dev in os.popen(self.Get_iOS):
				dev_value = dev.split()
				if dev.rfind('Simulator') != -1:
					continue
				if dev.rfind('(') == -1:
					continue
				# iOS['platformName'] = read_config('appium', 'platformName')
				# iOS['bundleId'] = read_config('appium','bundleId')
				iOS['deviceName'] = dev_value[0]
				iOS['platformVersion'] = str(eval(dev_value[1], {}))
				# [ae679a86542a57c31e57a1d66351c87570c9bac7] 进行分片[1:-1]
				iOS['udid'] = dev_value[2][1:-1]
				iOS['platformName'] = 'iOS'
				device.append(iOS)
			# print iOS
			
			# 命令获取Android设备列表
			for dev in os.popen(self.Get_Android):
				dev_value = dev.split()
				if len(dev_value) == 0:
					continue
				if dev_value[0].startswith('List'):
					continue
				Android['udid'] = dev_value[0]
				Android['deviceName'] = dev_value[1]
				Android['platformName'] = 'Android'
				device.append(Android)
		else:
			pass
		return device


if __name__ == '__main__':
	print '*' * 40
	port = 4723
	device = {'platformVersion': '10.1', 'deviceName': 'iPhone 5s'}
	appiumserver = AppiumServer()
	# appiumserver.start_server(device,port)
	# print appiumserver.get_port(2)
	print appiumserver.get_device()
	# appiumserver.pool_run()
	print '*' * 40
