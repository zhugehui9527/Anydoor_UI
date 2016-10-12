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
# from Public.Log import *
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
        self.driver = Element()
        self.appOperate = AppOperate()



    def tearDown(self):
        pass
        # self.driver.quit()


    def test_1(self):
        '''用例名称:宿主一账通H5登录'''
        logger.debug('向右滑动')
        self.driver.swipe_right()
        logger.debug('H5页面进行账密登录')
        self.appOperate.loginByH5('18589091413', 'Solution123')
        loginResult = self.appOperate.wait_for_text(30,'我的资产')
        if loginResult:
            self.assertTrue(loginResult,'登陆成功')
        else:
            self.assertFalse(loginResult,'登陆失败')
        self.appOperate.closeH5()
        self.driver.swipe_left()

    def test_2(self):
        '''用例名称:获取插件列表'''
        self.appOperate.getPluginList()


    def test_3(self):
        '''用例名称: 检查插件,插件名称: 平安地图,插件ID: PA01100000000_02_PAZB'''
        plugId = 'PA01100000000_02_PAZB'
        logger.debug('遍历插件,插件ID: %s' % plugId)
        self.assertTrue(self.appOperate.check_plugin(plugId, 'mapSelected'), '插件断言失败')

    def test_4(self):
        '''用例名称: 检查插件,插件名称: 模拟炒股,插件ID: PA01100000000_02_WLC'''
        plugId = 'PA01100000000_02_WLC'
        logger.debug('遍历插件,插件ID: %s' % plugId)
        self.assertTrue(self.appOperate.check_plugin(plugId, '值得买'),'插件断言失败')


    def test_5(self):
        '''用例名称: 检查插件,插件名称: 买车险,插件ID: PA00300000000_02_MCX'''
        plugId = 'PA00300000000_02_MCX'
        logger.debug('遍历插件,插件ID: %s' % plugId)
        self.assertTrue(self.appOperate.check_plugin(plugId, '买车险'), '插件断言失败')

    def test_6(self):
        '''用例名称: 检查插件,插件名称: 看直播,插件ID: PA00500000000_02_GSZB'''
        plugId = 'PA00500000000_02_GSZB'
        logger.debug('遍历插件,插件ID: %s' % plugId)
        self.assertTrue(self.appOperate.check_plugin(plugId, '热 门'), '插件断言失败')

    # 进入第二个页面
    def test_7(self):
        '''用例名称: 检查插件,插件名称: 积分福利,插件ID: PA02100000001_02_JF'''
        plugId = 'PA02100000001_02_JF'
        logger.debug('遍历插件,插件ID: %s' % plugId)
        self.assertTrue(self.appOperate.check_plugin(plugId, '可用积分'), '插件断言失败')

    def test_8(self):
        '''用例名称: 检查插件,插件名称: 活动集合,插件ID: PA01100000000_02_HDJHY'''
        plugId = 'PA01100000000_02_HDJHY'
        logger.debug('遍历插件,插件ID: %s' % plugId)
        self.assertTrue(self.appOperate.check_plugin(plugId, '本活动的最终解释权归平安科技所有'), '插件断言失败')

    def test_9(self):
        '''用例名称: 检查插件,插件名称: 股票组合,插件ID: PA00500000000_02_GPZH'''
        plugId = 'PA00500000000_02_GPZH'
        logger.debug('遍历插件,插件ID: %s' % plugId)
        self.assertTrue(self.appOperate.check_plugin(plugId, '专家观点'), '插件断言失败')



if __name__=='__main__':
    # if len(sys.argv) > 1:
    #     unit_dir = sys.argv[1]
    #     # print unit_dir
    # else:
    #     unit_dir = '.'
    # test_modules = [filename.replace('.py', '') for filename in os.listdir(unit_dir)
    #                 if filename.endswith('.py') and filename.startswith('Anydoor')]
    # # print test_modules
    # map(__import__, test_modules)
    #
    # suite = unittest.TestSuite()
    # for mod in [sys.modules[modname] for modname in test_modules]:
    #     suite.addTest(unittest.TestLoader().loadTestsFromModule(mod))

    try:
        suite = unittest.TestSuite()
        # suite.addTest(Anydoor_UI("test_1"))
        # suite.addTest(Anydoor_UI("test_2"))
        # suite.addTest(Anydoor_UI("test_3"))
        # suite.addTest(Anydoor_UI("test_4"))
        # suite.addTest(Anydoor_UI("test_5"))
        # suite.addTests(Anydoor_UI)

        #加载一个测试类下的所有测试用例
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromTestCase(Anydoor_UI)
        print '*'*40," 开始测试 ",'*'*40
        timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        report_path = '/Users/zengyuanchen/Documents/Project/Anydoor_UI/output/html/' + timestr + '_report.html'
        ReportObject = open(report_path, "wb")
        testRunner = HTMLTestRunner(stream=ReportObject,title='测试报告',description='IOS UI 自动化')
        testRunner.run(suite)
        ReportObject.close()

        print '*' * 40, " 结束测试 ", '*' * 40
    except Exception:
        raise
    finally:
        driver.quit()
