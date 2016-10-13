# -*- coding:utf-8 -*-
#######################################################
#filename:Global.py
#author:Jeff
#date:2016-09-21
#function:处理全局文件变量
#######################################################
from driver import MyDriver
from Public.Log import LogSignleton
# from conf.Run_conf import get_conf_path
# conf_path = get_conf_path()
# global logger,driver
driver = MyDriver.get_driver()
logsignleton = LogSignleton()
logger = logsignleton.logger

# global logger
# logger = MyLog.get_logger()
# logger = logsignleton.logger

# driversignleton = DriverSignleton(conf_path)
# # global driver
# driver = driversignleton.get_driver()

# log = LogSignleton(conf_path)
# logger = log.get_logger()

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

# if __name__ == '__main__':
# 	# print '打印'
# 	# logger = log.get_Logger()
# 	# logger.debug('获取logger')
# 	# driver = log.get_Driver()
# 	# logger.debug('获取driver')
# 	pass

