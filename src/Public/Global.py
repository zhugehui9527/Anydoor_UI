# -*- coding:utf-8 -*-
#######################################################
#filename:Global.py
#author:Jeff
#date:2016-09-21
#function:处理全局文件变量
#######################################################

class D:
	from src.lib.driver import MyDriver
	driver = MyDriver.get_driver()

class L:
	from src.lib.Log import LogSignleton
	logsignleton = LogSignleton()
	logger = logsignleton.logger
	
		
	

