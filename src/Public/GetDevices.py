# -*- coding:utf-8 -*-

import os,time,re
from conf.Run_conf import read_config

class GetDevices:
	def __init__(self):
		self.Get_Android = 'adb devices'
		self.Get_iOS = 'instruments -s devices'
		self.serverport  = int(read_config('appium', 'port'))

	def get_device(self):
		'''
		连上usb线后自动获取设备列表
		:return:
		'''
		# 存储设备信息
		device = []
		isMonitor = eval(read_config('appium', 'isMonitor'))
		support_devices = str(read_config('appium','device')).split(',')
		print time.ctime(), ' [', __name__, '::', GetDevices.get_device.__name__, '] :','support devices = ',support_devices
		# 获取模拟器设备列表
		if isMonitor:
			if 'iOS_Monitor' in support_devices:
				print time.ctime(), ' [', __name__, '::', GetDevices.get_device.__name__, '] :','iOS_Monitor is allowed'
				iOS_Monitor = {}
				deviceName = read_config('appium', 'deviceName')
				platformVersion = read_config('appium', 'platformVersion')
				iOS_Monitor['deviceName'] = deviceName
				# deviceName = str(deviceName).replace(' ','')
				for dev in os.popen(self.Get_iOS).readlines():
					dev_value = str(dev).replace("\n", "").replace("\t", "").replace(" ", "")
					if dev_value.rfind(deviceName) == -1:
						continue
					if dev_value.rfind(platformVersion) == -1:
						continue
					re_deviceName = re.compile(r'(.*)\(').findall(dev_value)[0]
					re_deviceName2 = re.compile(r'(.*)\(').findall(re_deviceName)[0]
					if re_deviceName2 != deviceName:
						continue
					iOS_Monitor['udid'] = re.compile(r'\[(.*?)\]').findall(dev_value)[0]
					iOS_Monitor['platformVersion'] = platformVersion
					iOS_Monitor['platformName'] = 'iOS'
				device.append(iOS_Monitor)
			if 'Android_Monitor' in support_devices:
				print time.ctime(), ' [', __name__, '::', GetDevices.get_device.__name__, '] :','Android_Monitor is  allowed'
				# 命令获取Android设备列表
				for dev in os.popen(self.Get_Android).readlines():
					Android = {}
					dev_value = str(dev).replace("\n", "").replace("\t", "")
					if dev_value.rfind('device') != -1 and (not dev_value.startswith("List")) and dev_value != "":
						# print dev_value[:dev_value.find('device')].strip()
						Android['udid'] = dev_value[:dev_value.find('device')].strip()
						Android['platformName'] = 'Android'
						Android['deviceName'] = 'Android'
						# Android['platformVersion'] = '6.0.1'
						# Android['package'] = 'com.paic.example.simpleapp'
						# Android['activity'] = '.SettingActivity'
						# Android['app'] = '/usr/local/anydoor/app_package/PAAnydoor.apk'
						device.append(Android)

		else:
			pass
		# 是否运行真机
		isRealDevice = eval(read_config('appium', 'isRealDevice'))
		if isRealDevice:
			# 获取iOS真实设备列表
			for dev in os.popen(self.Get_iOS).readlines():
				iOS = {}
				dev_value = str(dev).replace("\n", "").replace("\t", "").replace(" ", "")
				if dev.rfind('Simulator') != -1:
					continue
				if dev.rfind('(') == -1:
					continue
				# print dev_value
				# iOS['platformName'] = read_config('appium', 'platformName')
				# iOS['bundleId'] = read_config('appium','bundleId')
				iOS['deviceName'] = re.compile(r'(.*)\(').findall(dev_value)[0]
				iOS['platformVersion'] = re.compile(r'\((.*)\)').findall(dev_value)[0]
				iOS['udid'] = re.compile(r'\[(.*?)\]').findall(dev_value)[0]
				iOS['platformName'] = 'iOS'

				device.append(iOS)
			# print iOS

			# 命令获取Android设备列表
			for dev in os.popen(self.Get_Android).readlines():
				Android = {}
				dev_value = str(dev).replace("\n", "").replace("\t", "")
				if dev_value.rfind('device') != -1 and (not dev_value.startswith("List")) and dev_value != "":
					# print dev_value[:dev_value.find('device')].strip()
					Android['udid'] = dev_value[:dev_value.find('device')].strip()
					Android['platformName'] = 'Android'
					Android['deviceName'] = 'Android'
					# Android['platformVersion'] = '6.0.1'
					# Android['package'] = 'com.paic.example.simpleapp'
					# Android['activity'] = '.SettingActivity'
					# Android['app'] = '/usr/local/anydoor/app_package/PAAnydoor.apk'
					device.append(Android)
		else:
			pass
		print '*'*80
		print time.ctime(), ' [', __name__, '::', GetDevices.get_device.__name__, '] :', ' \n device =  ', device
		return device

	def __is_using(self):
		'''
		detect whether port is using
		:param port:
		:return:
		'''
		cmd = "netstat -an | grep %s" % str(self.serverport)
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
			if not self.__is_using() and (self.serverport not in port_list):
				port_list.append(self.serverport)
			else:
				self.serverport += 1

		# while True:
		# 	if len(port_list) == count:
		# 		break
		#
		# 	else:
		# 		port_list.append(self.serverport)
		# 		self.serverport += 1
		#

		return port_list


if __name__ == '__main__':
	G = GetDevices()
	G.get_device()
