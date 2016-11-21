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
