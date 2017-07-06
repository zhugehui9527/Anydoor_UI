# -*- coding:utf-8 -*-
#######################################################
# filename:Anydoor.py
# author:Jeff
# date:2016-09-21
# function:对测试用例进行操作处理
#######################################################
import sys,time
import pytest, allure
import unittest
from conf.Run_conf import read_config
from src.Public.Global import L,D,S
from src.Public.appOperate import AppOperate
from src.lib.Element import Element
from src.Public.Common import platform as pf

reload(sys)
sys.setdefaultencoding('utf-8')

driver = D.driver
appOperate = AppOperate(driver)
wd = Element(driver)



@pytest.allure.severity(allure.MASTER_HELPER.severity_level.NORMAL)
def test_login():
	'''用例名称: 登录'''

	appOperate.paphone_login()
	# assert wd.by_id('注册成功')
	time.sleep(3)


def test_audio():
	'''音频'''
	appOperate.pahpone_audio()
	# assert wd.by_id('正在通话')
	# wd.by_id('voip hangup icons').click()
	# wd.by_id('确定').click()
