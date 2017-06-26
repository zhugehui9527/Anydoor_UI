# -*- coding:utf-8 -*-
#######################################################
#filename:common.py
#author:Jeff
#date:2016-09-21
#function:常用的common关键字封装
#######################################################
class operate_api(object):
	click = 'click'
	sendkeys = 'sendkeys'
	swipe2left = 'swipe2left'
	swipe2right = 'swipe2right'
	swipe2up = 'swipe2up'
	swipe2down = 'swipe2down'
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
	rerun = 'RERUN'
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

class platform:
	ios = 'ios'
	android = 'android'

class element_by(object):
	by_id = 'id'
	by_xpath = 'xpath'
	by_name = 'name'
	by_classname = 'classname'


class public(object):
	time2wait = 15
	element_sheet = u'元素表'
	public_case_sheet =u'公共案例库'
	case_sheet = u'Sheet1'
	macaca = 'macaca'
	appium ='appium'
	runmode = 'runmode'
	driver = 'driver'


class desired_caps:
	appium = 'appium'
	hostname = 'hostname'
	ip = 'ip'
	port = 'port'
	deviceName = 'deviceName'
	bundleId = 'bundleId'
	platformName = 'platformName'
	platformVersion = 'platformVersion'
	appPackage = 'appPackage'
	appActivity= 'appActivity'
	autoAcceptAlerts = 'autoAcceptAlerts'
	noReset = 'noReset'
	automationName = 'automationName'
	unicodeKeyboard = 'unicodeKeyboard'
	resetKeyboard = 'resetKeyboard'
	autoWebview = 'autoWebview'
	app = 'app'
	WaitForAppScript = 'WaitForAppScript'
	newCommandTimeout = 'newCommandTimeout'
	clearSystemFiles = 'clearSystemFiles'
	udid = 'udid'
	reuse = 'reuse'
