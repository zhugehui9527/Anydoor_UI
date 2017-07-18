# -*- coding:utf-8 -*-

import os,time,re
from conf.Run_conf import read_config
BOOL = lambda p: True if p == 'True' or p == 'true' else False
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
		isMonitor = BOOL(read_config('appium', 'isMonitor'))
		support_devices = str(read_config('appium','device')).split(',')
		print (time.ctime(), ' [', __name__, '::', GetDevices.get_device.__name__, '] :','support devices = ',support_devices)
		# 获取模拟器设备列表
		if isMonitor:
			if 'iOS_Monitor' in support_devices:
				print (time.ctime(), ' [', __name__, '::', GetDevices.get_device.__name__, '] :','iOS_Monitor is allowed')
				iOS_Monitor = {}
				deviceName = read_config('appium', 'deviceName')
				platformVersion = read_config('appium', 'platformVersion')
				iOS_Monitor['deviceName'] = deviceName
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
				print (time.ctime(), ' [', __name__, '::', GetDevices.get_device.__name__, '] :','Android_Monitor is  allowed')
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
		isRealDevice = BOOL(read_config('appium', 'isRealDevice'))
		if isRealDevice:
			if 'iOS_Real_Device' in support_devices:
				# 获取iOS真实设备列表
				for dev in os.popen(self.Get_iOS).readlines():
					iOS = {}
					dev_value = str(dev).replace("\n", "").replace("\t", "").replace(" ", "")
					if dev.rfind('Simulator') != -1:
						continue
					if dev.rfind('(') == -1:
						continue
					print dev_value
					# iOS['platformName'] = read_config('appium', 'platformName')
					# iOS['bundleId'] = read_config('appium','bundleId')
					iOS['deviceName'] = re.compile(r'(.*)\(').findall(dev_value)[0]
					iOS['platformVersion'] = re.compile(r'\((.*)\)').findall(dev_value)[0]
					iOS['udid'] = re.compile(r'\[(.*?)\]').findall(dev_value)[0]
					iOS['platformName'] = 'iOS'
					device.append(iOS)

			if 'Android_Real_Device' in support_devices:
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
		# print ('*'*80)
		print (time.ctime(), ' [', __name__, '::', GetDevices.get_device.__name__, '] :', ' \n device =  ', device)
		if device:
			return device
		else:
			raise ValueError, '设备未连接或者设备配置错误,请检查设备以及相关配置'


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
				self.serverport += 10

		# while True:
		# 	if len(port_list) == count:
		# 		break
		#
		# 	else:
		# 		port_list.append(self.serverport)
		# 		self.serverport += 1
		#

		return port_list

	def set_device_yaml(self):
		"""
        获取当前设备的Android version并且保存到yaml里
        :return:
        """
		device_lst = []
		from src.lib.AdbUtils import ADB
		from src.Public.Global import L
		for device in self.get_device:
			adb = ADB(device)

			L.logger.debug(
				'get device:{},Android version:{}'.format(
					device, adb.get_android_version()))
			device_lst.append({'platformVersion': adb.get_android_version(
			), 'deviceName': device, 'platformName': 'Android'})

		import yaml
		import os
		PATH = lambda p: os.path.abspath(
			os.path.join(os.path.dirname(__file__), p)
		)
		device_info_path = PATH('../../conf/deviceinfo.yaml')
		with open(device_info_path, 'w') as f:
			yaml.dump(device_lst, f)
			f.close()

if __name__ == '__main__':
	G = GetDevices()
	G.get_device()
