# -*- coding:utf-8 -*-
#######################################################
#filename:driver.py
#author:Jeff
#date:2016-09-21
#function:对日志进行操作处理
#######################################################
import unittest,time
from HTMLTestRunner import HTMLTestRunner
from Element import *
from appOperate import *
from Public.Public import *
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')


class Anydoor_UI(unittest.TestCase):
    __usage__ = '''
    %prog      # Searches CWD
    %prog DIR
    '''
    def setUp(self):
        self.driver = Element()

    def tearDown(self):
        self.driver.quit()

    def checkPlugin(self,plugname,result):
        self.driver.implicitly_wait(3)
        self.driver.by_id(plugname).click()

    def test_1(self):
        "开始宿主一账通登录。。。"
        self.driver.implicitly_wait(3)
        self.driver.by_id("一账通").click()
        self.driver.implicitly_wait(3)
        self.driver.by_id("宿主登陆").click()
        self.driver.implicitly_wait(3)
        self.driver.by_id("选择登陆用户").click()
        self.driver.implicitly_wait(3)
        self.driver.by_id("确认").click()
        self.driver.implicitly_wait(3)
        self.driver.by_id("登陆").click()
        self.driver.implicitly_wait(8)



    def test_2(self):
        '测试场景1'
        print self.driver.device_time()

    def test_3(self):
        '测试场景2'
        print self.driver

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
        print unittest.TestLoader().loadTestsFromModule(mod)

    # suit = unittest.TestSuite()
    # suit.addTest(Anydoor_UI("testLogin"))
    # suit.addTests(Anydoor_UI)
    # suit = unittest.TestLoader.loadTestsFromTestCase(Anydoor_UI)
    print "starting...."
    timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    report_path = '/Users/zengyuanchen/Documents/Project/Anydoor_UI/src/' + timestr + 'report.html'
    ReportObject = open(report_path, "wb")
    testRunner = HTMLTestRunner(stream=ReportObject,title=u'测试报告',description=u'IOS UI 自动化')
    testRunner.run(suite)
    ReportObject.close()