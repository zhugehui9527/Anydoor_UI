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

#实例化调用Log
logtest = Log()
logtest.GenerateLog()

#遍历unittest中所有模块
if len(sys.argv) > 1:
	unit_dir = sys.argv[1]
	print unit_dir
else:
	unit_dir = '.'
test_modules = [filename.replace('.py', '') for filename in os.listdir(unit_dir)
                if filename.endswith('.py') and filename.startswith('Anydoor')]
logger.debug('遍历unittest中所有模块,模块内容: %s' % test_modules)
map(__import__, test_modules)

suite = unittest.TestSuite()
for mod in [sys.modules[modname] for modname in test_modules]:
	suite.addTest(unittest.TestLoader().loadTestsFromModule(mod))

print "starting...."
timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
report_path = '/Users/zengyuanchen/Documents/Project/Anydoor_UI/output/html/' + timestr + '_report.html'
ReportObject = open(report_path, "wb")
testRunner = HTMLTestRunner(stream=ReportObject, title=u'测试报告', description=u'IOS UI 自动化')
testRunner.run(suite)
ReportObject.close()