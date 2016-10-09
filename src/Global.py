# -*- coding:utf-8 -*-
#######################################################
#filename:Global.py
#author:Jeff
#date:2016-09-21
#function:处理全局文件变量
#######################################################
from driver import *
from Public.Log import *
import time, datetime
global driver ,logger

driversignleton = DriverSignleton('/Users/zengyuanchen/Documents/Project/Anydoor_UI/conf/monitor.ini')
driver = driversignleton.get_driver()

log = LogSignleton('/Users/zengyuanchen/Documents/Project/Anydoor_UI/conf/monitor.ini')
logger = log.get_logger()

# def get_Driver():
# 	driversignleton = DriverSignleton('/Users/zengyuanchen/Documents/Project/Anydoor_UI/conf/monitor.ini')
# 	getdriver = driversignleton.get_driver()
# 	return getdriver
#
# def get_Logger():
# 	log = LogSignleton('/Users/zengyuanchen/Documents/Project/Anydoor_UI/conf/monitor.ini')
# 	getlogger = log.get_logger()
# 	return getlogger

# logger = get_Logger()
# driver = get_Driver()
#


# #将%Y-%m-%d格式时间字符串转化为时间戳（带微秒）
# def change_time(time_str):
#     timeArray = time.strptime(time_str, "%Y-%m-%d")
#     timeStamp = int(time.mktime(timeArray))
#     timeStamp = int(str(timeStamp) + '000000')
#     return timeStamp
#
# #获取当前时间戳
# def gettime_nowstamp():
#     dnow = datetime.datetime.now()
#     # print dnow
#     dnows = str(int(time.mktime(dnow.timetuple())))
#     # print dnows
#     #mics = str(dnow.microsecond)
#     mics = '000000'
#     nows = int(dnows + mics)
#     return nows

if __name__ == '__main__':
	print '打印'
	logger = get_Logger()
	logger.debug('获取logger')
	driver = get_Driver()
	logger.debug('获取driver')
