# -*- coding:utf-8 -*-
#######################################################
#filename:Run_Unittest.py
#author:Jeff
#date:2016-09-21
#function:对日志进行操作处理
#######################################################
import unittest
from HTMLTestRunner import HTMLTestRunner
from Global import *
from Public.logger import *
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

logtest = Log()
logtest.GenerateLog()
logger = logtest.get_my_logger()
logger.info('测试')
logger.debug('测试')
logger.error('测试')
logger.warning('测试')
logger.critical('测试')
