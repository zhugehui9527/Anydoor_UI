# -*- coding:utf-8 -*-
#######################################################
# filename:Anydoor.py
# author:Jeff
# date:2016-09-21
# function:对测试用例进行操作处理
#######################################################
import sys,time
import pytest,unittest
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
		# driver.swipe_right()  # 右滑动
		# time.sleep(3)
		# driver.by_id("个人中心").click()
		# time.sleep(3)
		appOperate.loginByH5(username, password)
		loginResult = appOperate.wait_for_text(30, '我的订单')
		assert loginResult
	finally:
		appOperate.closeH5()
		time.sleep(3)
		wd.swipe_left()
		time.sleep(3)


def test_pluginlist():
	'''用例名称: 获取插件列表'''
	global getPluginList
	getPluginList = appOperate.getPluginList()
	assert getPluginList
	
def skip():
	'''判断运行该用例的是否是IOS平台,是返回True,否则返回False;
	用于判断是否需要跳过当前插件检查用例(因为iOS和Android插件列表有差异性)。
	'''
	PlatformName_lower = S.device['platformName'].lower()
	if PlatformName_lower != pf.ios :
		L.logger.debug('当前系统为Android ')
		return True
	else:
		L.logger.debug('当前系统为iOS')
		return False

skip_Anr = pytest.mark.skipif('skip()')
# 插件ID 和 断言,注意跳过skip_Anr后面有两个括号
checkPluginInfo = [
					skip_Anr(('PA01100000000_02_PAZB', u'加油站')),
                   ('PA01100000000_02_WLC', u'值得买'),
                   # skip_Anr(('PA00500000000_02_GSZB', u'热 门')),
                   # ('PA01100000000_02_HDJHY', u'本活动的最终解释权归平安科技所有'),
					# ('PA00800000000_02_PACX', u'使馆信息'),
					# # ('PA00800000000_02_PAC1X', u'使馆信息'), #不存在的插件
					# # ('PA00800000000_02_PACX', u'使s馆信息'), #断言错误
                   ('PA01100000001_02_WDCX','ATM'),
                   ('PA01100000001_02_XYK',u'我的信用卡'),
                   ('PA01100000000_02_YYG',u'1元GO'),
                   ('PA03300000000_02_AJDK',u'试算一下'),
                   # ('PA02500000000_02_TZLC',u'任意门'), # 需要截图断言
                   ('PA02100000001_02_JF', u'可用积分'),
                   ('PA01200000000_02_XYD', u'马上贷款'),
                   ('PA02100000000_02_YJQB', u'获取动态码'),
                   ('PA02100000000_02_KY', u'立即冲刺'),
                   ('PA02100000000_02_HQY', u'获取验证码'),
                   ('PA00800000000_02_PACX', u'使馆信息'),
                   ('PA00400000000_02_CFBXZZC', u'温馨提示'),
                   # ('PA01100000000_02_RYG', u'个人中心'),
                   ('PA00500000000_02_RED', u'申请条件'),
                   ('PA01100000000_02_ZCCX', u'资产提醒'),
                   ('PA01100000000_02_YHFK', u'建议反馈'),
                   # ('PA01100000003_02_WDCX', u'ATM'),
					('PA02100000000_02_DYP', u'电影'),
                   ('SZDBK00000000_02_XYT', u'个人信息'),
                   # ('PA02100000000_02_WDZC', u'资产提醒'), # 下线
                   ('PA02100000000_02_PAYD', u'小额消费贷款'),
                   ('PA02700000000_02_PAYX', u'欢乐游戏'),
                   ('PA02100000000_02_CGZ', u'添加车'),
                   ('PA02100000000_02_CJKX', u'财经快讯'),
                   ('PA02500000000_02_BZB', u'热销基金'),
					('PA01100000000_02_BXCS', u'旅游险'),
                   ('PA02100000000_02_XEDK', u'小额消费贷款'),
                   ('PA01100000000_02_LHBLC', u'投资须谨慎，以上产品不保证收益'),
                   skip_Anr(('PA00500000000_02_GPZH', u'股市有风险，投资需谨慎'))
                   ]


# 插件和检查插件方法分离,便于维护
@pytest.mark.parametrize(("pluginID,pluginAssert"),checkPluginInfo)
def test_checkplugin(pluginID,pluginAssert):
	'''
	对插件进行检查
	:param pluginID:插件ID
	:param pluginAssert:插件断言
	:return:
	'''

	# PluginList = appOperate.getPluginList()
	if pluginID not in getPluginList:
		L.logger.warning('插件: %s 不在插件列表' % pluginID)
		pytest.xfail('offline')
	else:
		L.logger.debug('遍历检查插件,插件ID: %s' % pluginID)
		assert appOperate.check_plugin(pluginID,pluginAssert)


checkPluginInfo1 = [('PA02500000000_02_TZLC',0, 0.1, 0.9, 0.2),# 对比屏幕上面的截图
                    ('PA01100000003_02_WDCX',0, 0.85,0.9, 0.15), # 对比屏幕下面的截图
                    # ('PA01100000000_02_RYG')
                    ]
@pytest.mark.parametrize("pluginID,start_x,start_y,weight,height",checkPluginInfo1)
def test_checkplugin_by_image(pluginID,start_x,start_y,weight,height):
	'''
	某些插件界面全是图片不好断言,故采用图片对比进行断言
	:param pluginID: 插件
	:param start_x: 起点横坐标百分比
	:param start_y: 起点纵坐标百分比
	:param weight: 截图的宽度百分比
	:param height: 截图的高度百分比
	:return:
	'''
	if pluginID not in getPluginList:
		L.logger.warning('插件: %s 不在插件列表' % pluginID)
		pytest.xfail('offline')
	else:
		L.logger.debug('遍历检查插件,插件ID: %s' % pluginID)
		assert appOperate.check_plugin_byImage(pluginID, start_x, start_y, weight, height)

