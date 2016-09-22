# -*- coding:utf-8 -*-
#######################################################
#filename:driver.py
#author:Jeff
#date:2016-09-21
#function:对日志进行操作处理
#######################################################

from driver import driver

class appOperate():
	def __init__(self):
		at = driver()
		self.driver = at.get_driver()

	def wait_for_text(self,time2wait,text):
		print 'ss'
