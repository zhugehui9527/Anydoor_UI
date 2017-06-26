# -*- coding:utf-8 -*-
#######################################################
#filename:Run_conf.py
#author:Jeff
#date:2016-09
#function:运行加载配置数据
#######################################################
import os,sys
if '3.6' in sys.version:
	import configparser as cfg
else:
	import ConfigParser as cfg

# sys.path.append("..")
# prjDir = os.path.split(os.path.realpath(__file__))[0]
# conf_path = os.path.join(prjDir, "monitor.ini")
# logger.debug('conf path is %s ' % conf_path)
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
conf_path = PATH('monitor.ini')
# print('conf_path = ',conf_path)
#加载配置文件
def load_config(file_path):
	config = cfg.ConfigParser()
	try:
		if os.path.isfile(file_path):
			if '3.6' in sys.version:
				config.read(file_path,'utf-8')
			else:
				config.read(file_path)
			return config
	except:
		print ("配置文件 monitor.ini is not exits" )

#读取cfg文件中的seciton区域中的某一个option值并返回该值
def read_config(section_name,option):
	monitor_cfg = load_config(conf_path)
	for section in monitor_cfg.sections():
		if section == section_name:
			value = monitor_cfg.get(section,option)
			return value

def get_host():
	'''指定配置段获取主机'''
	return eval(str(read_config('appium', 'ip')))


def get_port():
	'''指定配置段获取端口号'''
	return eval(str(read_config('appium', 'port')))

def get_runmode(mode):
	'''指定配置段获取运行模式'''
	return eval(str(read_config('runmode', mode)))


def get_index():
	'''指定配置段获取待执行的列表'''
	return eval(str(read_config('runmode', 'index')))


def get_unindex(self, *section):
	'''指定配置段获取不执行的列表'''
	return eval(str(read_config('runmode', 'unindex')))


if __name__ == '__main__':
	import os

	ini_path = os.path.abspath('./conf/monitor.ini')
	deviceName = read_config('appium','deviceName')
	print ('deviceName : %s' % deviceName)
