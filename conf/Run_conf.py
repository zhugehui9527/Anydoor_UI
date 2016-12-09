# -*- coding:utf-8 -*-
#######################################################
#filename:Run_conf.py
#author:Jeff
#date:2016-09
#function:运行加载配置数据
#######################################################
import os
import ConfigParser

prjDir = os.path.split(os.path.realpath(__file__))[0]
conf_path = os.path.join(prjDir, "monitor.ini")
# logger.debug('conf path is %s ' % conf_path)

#加载配置文件
def load_config(file_path):
	config = ConfigParser.ConfigParser()
	try:
		if os.path.exists(file_path):
			config.read(file_path)
			return config
	except:
		# logger.error("%s is not exits" % file_path)
		print "%s is not exits",file_path

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
	ini_path = '/Users/zengyuanchen/Documents/SVN/ShareFromCloud/share/Project/Anydoor_UI/conf/monitor.ini'
	deviceName = read_config('appium','deviceName')
	print 'deviceName : %s' % deviceName