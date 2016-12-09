# -*- coding:utf-8 -*-
#######################################################
#filename:Element.py
#author:Jeff
#date:2016-09-21
#function:封装操作驱动元素
#######################################################
class operate_api(object):
	click = 'click'
	sendkeys = 'sendkeys'
	swipe2left = 'swipe2left'
	swipe2right = 'swipe2right'
	assertTrue = 'assertTrue'
	assertTrueCheckPlugin = 'assertTrueCheckPlugin'
	assertFalse = 'assertFalse'
	waitFortext = 'waitFortext'
	hidekeyboard = 'hidekeyboard'
	sleep = 'sleep'
	publicCase = u'公共库'
	checkPlugin = 'checkPlugin'
	closeH5='closeH5'
	closeH5ByPluginId='closeH5ByPluginId'
	getPluginList='getPluginList'
	getScreenShot='getScreenShot'
	
class resultStutas(object):
	success = 'PASS'
	fail = 'FAIL'
	error = 'ERROR'
	successCode = 1
	failCode = 0
	errorCode = -1
	timestamp ='timestamp'
	status = 'status'
	
class resultClass:
	result=[]
	img_base64={}
	trace={}
	log={}
	
class element_by(object):
	by_id = 'id'
	by_xpath = 'xpath'
	by_name = 'name'
	by_classname = 'classname'

class public(object):
	time2wait = 20
	element_sheet = u'元素表'
	public_case_sheet =u'公共案例库'
	case_sheet = u'Sheet1'
	

class element_by_excel(object):
	element_sheet_name =u'元素表'
	msgCenter = u'消息中心'
	personalCenter = u'个人中心'
	loginUsername_H5 =u'H5一账通登陆页面账号'
	loginPassword_H5 =u'H5一账通登陆页面密码'
	loginButton_H5 = u'H5一账通登陆页面登陆按钮'
	YZT = u'一账通'
	YZT_not = u'非一账通'
	login_SZ = u'宿主登陆'
	loginUsername_SZ_Default = u'宿主默认登录账号'
	loginUsername_SZ = u'宿主登录账号'
	loginUsername_SZ_Sure =u'确认宿主登录账号'
	loginUsername_SZ_Button =u'宿主登录按钮'
	loginPassword_SZ_Button = u'密码登录按钮'
	loginUsername_low = u'低门槛账密登陆页面账号'
	loginPassword_low = u'低门槛账密登陆页面密码'
	login_low_button =u'低门槛账密登陆页面登录按钮'


