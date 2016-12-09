# -*- coding:utf-8 -*-
#######################################################
#filename:Global.py
#author:Jeff
#date:2016-09-21
#function:处理全局文件变量
#######################################################


class D:
	from src.driver import MyDriver
	driver = MyDriver.get_driver()

class L:
	from src.Public.Log import LogSignleton
	logsignleton = LogSignleton()
	logger = logsignleton.logger
# global logger
# logger = MyLog.get_logger()
# logger = logsignleton.logger

# driversignleton = DriverSignleton(conf_path)
# # global driver
# driver = driversignleton.get_driver()
