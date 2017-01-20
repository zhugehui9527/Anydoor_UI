# -*- coding:utf-8 -*-
#######################################################
# filename:Anydoor.py
# author:Jeff
# date:2016-09-21
# function:对测试用例进行操作处理
#######################################################
import sys,time
import pytest
from conf.Run_conf import read_config
from src.Public.Global import L,D,S
from src.Public.appOperate import AppOperate
from src.lib.Element import Element
from src.Public.Common import platform as pf
# from src.Public import Public

reload(sys)
sys.setdefaultencoding('utf-8')

driver = D.driver
appOperate = AppOperate(driver)
wd = Element(driver)
username = read_config('login', 'login_username')
password = read_config('login', 'login_password')

def test_login():
	'''用例名称: 测试H5登录'''
	try:
		appOperate.loginByH5(username, password)
		time.sleep(3)
		loginResult = appOperate.wait_for_text(30, '我的订单')
		assert loginResult
	finally:
		appOperate.closeH5()
		time.sleep(3)
		wd.swipe_left()
		time.sleep(3)

def test_pluginlist():
	'''用例名称: 获取插件列表'''
	getPluginList = appOperate.getPluginList()
	assert getPluginList
	
	
# 插件ID 和 断言
checkPluginInfo = [('PA01100000000_02_PAZB', u'加油站'),
                   ('PA01100000000_02_WLC', u'值得买'),
                   ('PA00500000000_02_GSZB', u'热 门'),
                   ('PA01100000000_02_HDJHY', u'本活动的最终解释权归平安科技所有'),
                   ('PA01100000001_02_WDCX','ATM'),
                   ('PA01100000001_02_XYK',u'我的信用卡'),
                   ('PA01100000000_02_YYG',u'1元GO'),
                   ('PA03300000000_02_AJDK',u'试算一下'),
                   ('PA02500000000_02_TZLC',u'任意门'),
                   ('PA02100000001_02_JF', u'可用积分'),
                   ('PA01200000000_02_XYD', u'马上贷款'),
                   ('PA02100000000_02_YJQB', u'获取动态码'),
                   ('PA02100000000_02_KY', '5-6%'),
                   ('PA02100000000_02_HQY', u'获取验证码'),
                   ('PA00800000000_02_PACX', u'使馆信息'),
                   ('PA00400000000_02_CFBXZZC', u'温馨提示'),
                   ('PA01100000000_02_RYG', u'个人中心'),
                   ('PA00500000000_02_RED', u'申请条件'),
                   ('PA01100000000_02_ZCCX', u'资产提醒'),
                   ('PA01100000000_02_YHFK', u'建议反馈'),
                   ('PA01100000003_02_WDCX', u'ATM'),
                   ('SZDBK00000000_02_XYT', u'个人信息'),
                   ('PA02100000000_02_WDZC', u'资产提醒'),
                   ('PA02100000000_02_PAYD', u'小额消费贷款'),
                   ('PA02700000000_02_PAYX', u'欢乐游戏'),
                   ('PA02100000000_02_CGZ', u'添加车'),
                   ('PA02100000000_02_CJKX', u'财经快讯'),
                   ('PA02500000000_02_BZB', u'热销基金'),
                   ('PA02100000000_02_XEDK', u'小额消费贷款'),
                   ('PA01100000000_02_LHBLC', u'投资须谨慎，以上产品不保证收益'),
                   ('PA00500000000_02_GPZH', u'股市有风险，投资需谨慎')
                   ]

# @pytest.mark.skipif(S.device['platformName'].lower() != pf.ios)
@pytest.mark.parametrize("pluginID,pluginAssert",checkPluginInfo)
def test_checkplugin(pluginID,pluginAssert):
	'''用例名称: 检查插件:{},断言:{}'''.format(pluginID,pluginAssert)
	L.logger.debug('遍历检查插件,插件ID: %s' % pluginID)
	assert appOperate.check_plugin(pluginID,pluginAssert)
	
