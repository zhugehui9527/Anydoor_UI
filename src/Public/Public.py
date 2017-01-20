# -*- coding:utf-8 -*-
#######################################################
#filename:Public.py
#author:Jeff
#date:2016-12-21
#function:公共函数封装
#######################################################
from appOperate import AppOperate
from src.Public.Common import platform as pf
from src.Public.Global import D,S

def platform_pluginIn_isTrue(pluginId):
	'''
	判断平台如果不是iOS平台 或者 插件不在插件列表 则返回True
	:param pluginId: 插件id
	:return: True
	
	'''
	appOperate = AppOperate(D.driver)
	if S.device['platformName'].lower() != pf.ios or (pluginId not in appOperate.getPluginList()):
		return True
	else:
		return False