# -*- coding:utf-8 -*-
#######################################################
#filename:driver.py
#author:Jeff
#date:2016-09-21
#function:对日志进行操作处理
#######################################################
import unittest,time
from HTMLTestRunner import HTMLTestRunner
from appOperate import *
from Element import *
from Public.logger import *
from Global import *
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')


class Anydoor_UI(unittest.TestCase):
    __usage__ = '''
    %prog      # Searches CWD
    %prog DIR
    '''
    def setUp(self):
        global driver
        self.driver = driver
        # self.driver = Element()
        self.appOperate = appOperate(self.driver)
        # 实例化调用Log
        logtest = Log()
        logtest.GenerateLog()


    def tearDown(self):
        self.driver.quit()


    def test_1(self):
        "开始宿主一账通登录。。。"
        logger.debug('向右滑动')
        self.driver.swipe_right()
        logger.debug('H5页面进行账密登录')
        self.appOperate.loginByH5('18589091413', 'Solution123')
        loginResult = self.appOperate.wait_for_text(15,'我的资产')
        if loginResult:
            self.assertTrue(loginResult,'登陆成功')
        else:
            self.assertFalse(loginResult,'登陆失败')
        self.appOperate.closeH5()
        self.driver.swipe_left()


    def test_2(self):
        '遍历插件'
        plugId = 'PA01100000000_02_PAZB'
        logger.debug('遍历插件,插件ID: %s' % plugId)
        if self.appOperate.check_plugin(plugId,'mapSelected'):
            self.assertTrue('插件校验成功!')
        else:
            self.assertFalse('插件校验失败!')


    def test_3(self):
        '遍历插件'
        plugId = 'PA01100000000_02_PAZB'
        logger.debug('遍历插件,插件ID: %s' % plugId)
        if self.appOperate.check_plugin(plugId,'mapSelected'):
            self.assertTrue('插件校验成功!')
        else:
            self.assertFalse('插件校验失败!')



if __name__=='__main__':
    if len(sys.argv) > 1:
        unit_dir = sys.argv[1]
        # print unit_dir
    else:
        unit_dir = '.'
    test_modules = [filename.replace('.py', '') for filename in os.listdir(unit_dir)
                    if filename.endswith('.py') and filename.startswith('Anydoor')]
    # print test_modules
    map(__import__, test_modules)

    suite = unittest.TestSuite()
    for mod in [sys.modules[modname] for modname in test_modules]:
        suite.addTest(unittest.TestLoader().loadTestsFromModule(mod))
        # print unittest.TestLoader().loadTestsFromModule(mod)

    # suit = unittest.TestSuite()
    # suit.addTest(Anydoor_UI("testLogin"))
    # suit.addTests(Anydoor_UI)
    # suit = unittest.TestLoader.loadTestsFromTestCase(Anydoor_UI)
    print '*'*40," 开始测试 ",'*'*40
    timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    report_path = '/Users/zengyuanchen/Documents/Project/Anydoor_UI/output/html/' + timestr + '_report.html'
    ReportObject = open(report_path, "wb")
    testRunner = HTMLTestRunner(stream=ReportObject,title=u'测试报告',description=u'IOS UI 自动化')
    testRunner.run(suite)
    ReportObject.close()