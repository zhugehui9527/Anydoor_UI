# -*- coding:utf-8 -*-
#######################################################
#filename:driver.py
#author:Jeff
#date:2016-09-21
#function:对日志进行操作处理
#######################################################
import unittest,pytest
from HTMLTestRunner import HTMLTestRunner
# from AppiumServer import AppiumServer
from appOperate import AppOperate
from Element import *
from Global import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Anydoor_UI(unittest.TestCase):
    def setup_class(cls):
        '''
        setup class
        :return:
        '''
        cls.driver = Element()
        cls.appOperate = AppOperate()
        cls.username = read_config('login','login_username')
        cls.password = read_config('login', 'login_password')
        logger.debug('测试用例即将执行,初始化工作')

    def teardown_class(cls):
        '''
        teardown class
        :return:
        '''
        cls.driver.quit()
        logger.debug('测试用例执行完成,退出服务')

    def test_A1(self):
        '''用例名称:宿主一账通H5登录'''
        logger.debug('向右滑动,进入个人中心')
        self.driver.swipe_right()
        logger.debug('H5页面进行账密登录')
        self.appOperate.loginByH5(self.username, self.password)
        loginResult = self.appOperate.wait_for_text(30,'我的资产')
        if loginResult:
            self.assertTrue(loginResult,'登陆成功')
        else:
            self.assertFalse(loginResult,'登陆失败')
        self.appOperate.closeH5()
        self.driver.swipe_left()

    def test_A2(self):
        '''用例名称:获取插件列表'''
        self.appOperate.getPluginList()


    def test_A3(self):
        '''用例名称: 检查插件,插件名称: 平安地图,插件ID: PA01100000000_02_PAZB ,插件断言: mapSelected '''
        pluginId = 'PA01100000000_02_PAZB'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, 'mapSelected'),'插件: %s 断言失败' % pluginId)

    # """
    def test_A4(self):
        '''用例名称: 检查插件,插件名称: 模拟炒股,插件ID: PA01100000000_02_WLC ,插件断言: 值得买 '''
        pluginId = 'PA01100000000_02_WLC'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '值得买'),'插件: %s 断言失败' % pluginId)

    # @pytest.mark.xfail(run=False) #不运行此用例
    @pytest.mark.skipif(True,reason='PA00300000000_02_MCX is offline!')
    def test_A5(self):
        '''用例名称: 检查插件,插件名称: 买车险,插件ID: PA00300000000_02_MCX,插件断言: 买车险' '''
        pluginId = 'PA00300000000_02_MCX'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '买车险'), '插件: %s 断言失败' % pluginId)

    def test_A6(self):
        '''用例名称: 检查插件,插件名称: 看直播,插件ID: PA00500000000_02_GSZB,插件断言: 热 门 '''
        pluginId = 'PA00500000000_02_GSZB'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '热门推荐'), '插件: %s 断言失败' % pluginId)

    # 进入第二个页面
    def test_A7(self):
        '''用例名称: 检查插件,插件名称: 积分福利,插件ID: PA02100000001_02_JF,插件断言: 可用积分 '''
        pluginId = 'PA02100000001_02_JF'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '可用积分'), '插件: %s 断言失败' % pluginId)

    def test_A8(self):
        '''用例名称: 检查插件,插件名称: 活动集合,插件ID: PA01100000000_02_HDJHY,插件断言: 本活动的最终解释权归平安科技所有 '''
        pluginId = 'PA01100000000_02_HDJHY'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '本活动的最终解释权归平安科技所有'), '插件: %s 断言失败' % pluginId)

    def test_A9(self):
        '''用例名称: 检查插件,插件名称: 找网点,插件ID: PA01100000001_02_WDCX,插件断言: ATM '''
        pluginId = 'PA01100000001_02_WDCX'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, 'ATM'), '插件: %s 断言失败' % pluginId)

    def test_B0(self):
        '''用例名称: 检查插件,插件名称: 卡面由你,插件ID: PA01100000001_02_XYK,插件断言: 我的信用卡 '''
        pluginId = 'PA01100000001_02_XYK'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '我的信用卡'), '插件: %s 断言失败' % pluginId)

    def test_B1(self):
        '''用例名称: 检查插件,插件名称: 买航意险,插件ID: PA01100000000_02_YYG,插件断言: 立即投保 '''
        pluginId = 'PA01100000000_02_YYG'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '立即投保'), '插件: %s 断言失败' % pluginId)

    def test_B2(self):
        '''用例名称: 检查插件,插件名称: 在线投资,插件ID: PA02500000000_02_TZLC,插件断言: Containers '''
        pluginId = 'PA02500000000_02_TZLC'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, 'Containers'), '插件: %s 断言失败' % pluginId)

    def test_B3(self):
        '''用例名称: 检查插件,插件名称: 房按揭,插件ID: PA03300000000_02_AJDK,插件断言: 试算一下 '''
        pluginId = 'PA03300000000_02_AJDK'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '试算一下'), '插件: %s 断言失败' % pluginId)

    def test_B4(self):
        '''用例名称: 检查插件,插件名称: 平安好贷,插件ID: PA01200000000_02_XYD,插件断言: 马上贷款 '''
        pluginId = 'PA01200000000_02_XYD'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '马上贷款'), '插件: %s 断言失败' % pluginId)
    #第三个页面
    def test_B5(self):
        '''用例名称: 检查插件,插件名称: 应急钱包,插件ID: PA02100000000_02_YJQB,插件断言: 获取动态码 '''
        pluginId = 'PA02100000000_02_YJQB'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '获取动态码'), '插件: %s 断言失败' % pluginId)

    def test_B6(self):
        '''用例名称: 检查插件,插件名称: 查号码,插件ID: PA00800000000_02_PACX,插件断言: 使馆信息 '''
        pluginId = 'PA00800000000_02_PACX'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '使馆信息'), '插件: %s 断言失败' % pluginId)

    #@pytest.mark.xfail(run=False) #不运行此用例
    @pytest.mark.skipif(True,reason='PA01100000000_02_ZCCX is remaining!')
    def test_B7(self):
        '''用例名称: 检查插件,插件名称: 资产查询,插件ID: PA01100000000_02_ZCCX,插件断言: 资产提醒 '''
        pluginId = 'PA01100000000_02_ZCCX'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '资产提醒'), '插件: %s 断言失败' % pluginId)

    def test_B8(self):
        '''用例名称: 检查插件,插件名称: 融e贷,插件ID: PA00500000000_02_RED,插件断言: 申请条件 '''
        pluginId = 'PA00500000000_02_RED'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '申请条件'), '插件: %s 断言失败' % pluginId)

    def test_B9(self):
        '''用例名称: 检查插件,插件名称: 活期盈,插件ID: PA02100000000_02_HQY,插件断言: 获取验证码 '''
        pluginId = 'PA02100000000_02_HQY'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '获取验证码'), '插件: %s 断言失败' % pluginId)

    def test_C0(self):
        '''用例名称: 检查插件,插件名称: 精品特卖,插件ID: PA01100000000_02_RYG,插件断言: 安少爷の物:搜罗全网品质好物 '''
        pluginId = 'PA01100000000_02_RYG'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '安少爷の物:搜罗全网品质好物'), '插件: %s 断言失败' % pluginId)

    def test_C1(self):
        '''用例名称: 检查插件,插件名称: 我要吐槽,插件ID: PA01100000000_02_YHFK,插件断言: 建议反馈 '''
        pluginId = 'PA01100000000_02_YHFK'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '建议反馈'), '插件: %s 断言失败' % pluginId)

    def test_C2(self):
        '''用例名称: 检查插件,插件名称: 明星理财,插件ID: PA02100000000_02_KY,插件断言: AnyDoorSDKBundle.bundle '''
        pluginId = 'PA02100000000_02_KY'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, 'AnyDoorSDKBundle.bundle'), '插件: %s 断言失败' % pluginId)

    def test_C3(self):
        '''用例名称: 检查插件,插件名称: 财富礼包,插件ID: PA02100000000_02_JNHPS,插件断言: 点击查看活动规则 '''
        pluginId = 'PA02100000000_02_JNHPS'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '点击查看活动规则'), '插件: %s 断言失败' % pluginId)

    def test_C4(self):
        '''用例名称: 检查插件,插件名称: 财富宝,插件ID: PA00400000000_02_CFBXZZC,插件断言: 温馨提示 '''
        pluginId = 'PA00400000000_02_CFBXZZC'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '温馨提示'), '插件: %s 断言失败' % pluginId)

    def test_C5(self):
        '''用例名称: 检查插件,插件名称: 找网点,插件ID: PA01100000001_02_WDCX,插件断言: ATM '''
        pluginId = 'PA01100000001_02_WDCX'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, 'ATM'), '插件: %s 断言失败' % pluginId)
    # 下一页
    def test_C6(self):
        '''用例名称: 检查插件,插件名称: 资产生活,插件ID: PA02100000000_02_QDCS,插件断言: 您已累计获得 '''
        pluginId = 'PA02100000000_02_QDCS'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '距离抢购结束'), '插件: %s 断言失败' % pluginId)

    def test_C7(self):
        '''用例名称: 检查插件,插件名称: 买保尊宝 ,插件ID: PA02500000000_02_BZB,插件断言: 热销基金 '''
        pluginId = 'PA02500000000_02_BZB'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '热销基金'), '插件: %s 断言失败' % pluginId)

    def test_C8(self):
        '''用例名称: 检查插件,插件名称: 平安易贷,插件ID: PA02100000000_02_PAYD,插件断言: 小额消费贷款 '''
        pluginId = 'PA02100000000_02_PAYD'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '小额消费贷款'), '插件: %s 断言失败' % pluginId)

    def test_C9(self):
        '''用例名称: 检查插件,插件名称: 车估值,插件ID: PA02100000000_02_CGZ,插件断言: 添加车 '''
        pluginId = 'PA02100000000_02_CGZ'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '添加车'), '插件: %s 断言失败' % pluginId)

    def test_D0(self):
        '''用例名称: 检查插件,插件名称: 房估值,插件ID: PA02100000000_02_FGZ,插件断言: 我的房产 '''
        pluginId = 'PA02100000000_02_FGZ'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '我的房产'), '插件: %s 断言失败' % pluginId)

    def test_D1(self):
        '''用例名称: 检查插件,插件名称: 薪易通,插件ID: SZDBK00000000_02_XYT,插件断言: 贷款描述 '''
        pluginId = 'SZDBK00000000_02_XYT'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '贷款描述'), '插件: %s 断言失败' % pluginId)

    def test_D2(self):
        '''用例名称: 检查插件,插件名称: 二手房,插件ID: PA02800000000_02_ESF,插件断言: 售价 '''
        pluginId = 'PA02800000000_02_ESF'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '售价'), '插件: %s 断言失败' % pluginId)

    def test_D3(self):
        '''用例名称: 检查插件,插件名称: 新房,插件ID: PA02800000000_02_XF,插件断言: 楼盘列表 '''
        pluginId = 'PA02800000000_02_XF'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '楼盘列表'), '插件: %s 断言失败' % pluginId)
    #下一页
    def test_D4(self):
        '''用例名称: 检查插件,插件名称: 平安易贷,插件ID: PA02100000000_02_XEDK,插件断言: 小额消费贷款 '''
        pluginId = 'PA02100000000_02_XEDK'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '小额消费贷款'), '插件: %s 断言失败' % pluginId)

    def test_D5(self):
        '''用例名称: 检查插件,插件名称: 亲子礼包,插件ID: PA02100000000_02_JNHRS,插件断言: 点击查看活动规则 '''
        pluginId = 'PA02100000000_02_JNHRS'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '点击查看活动规则'), '插件: %s 断言失败' % pluginId)

    def test_D6(self):
        '''用例名称: 检查插件,插件名称: 领话费,插件ID: PA02100000000_02_JNHJK,插件断言: 点击查看活动规则 '''
        pluginId = 'PA02100000000_02_JNHJK'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '点击查看活动规则'), '插件: %s 断言失败' % pluginId)

    def test_D7(self):
        '''用例名称: 检查插件,插件名称: 保险超市,插件ID: PA01100000000_02_BXCS,插件断言: 旅行意外险 '''
        pluginId = 'PA01100000000_02_BXCS'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '旅行意外险'), '插件: %s 断言失败' % pluginId)

    def test_D8(self):
        '''用例名称: 检查插件,插件名称: 现金理财,插件ID: PA01100000000_02_LHBLC,插件断言: 超强现金理财 '''
        pluginId = 'PA01100000000_02_LHBLC'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '超强现金理财'), '插件: %s 断言失败' % pluginId)

    def test_D9(self):
        '''用例名称: 检查插件,插件名称: 股票组合,插件ID: PA00500000000_02_GPZH,插件断言: 专家观点 '''
        pluginId = 'PA00500000000_02_GPZH'
        logger.debug('遍历插件,插件ID: %s' % pluginId)
        self.assertTrue(self.appOperate.check_plugin(pluginId, '专家观点'), '插件: %s 断言失败' % pluginId)
    # """
    # def test_E0(self):
    #     '''用例名称: 检查插件,插件名称: 平安地图,插件ID: PA01100000000_02_PAZB ,插件断言: mapSelected '''
    #     pluginId = 'PA01100000000_02_PAZB'
    #     logger.debug('遍历插件,插件ID: %s' % pluginId)
    #     self.assertTrue(self.appOperate.check_plugin(pluginId, 'mapSelected'),'插件: %s 断言失败' % pluginId)
    #
    # def test_E1(self):
    #     '''用例名称: 不存在的插件ID,测试用例失败专用 '''
    #     pluginId = 'PA00500000000_02_1GPZH'
    #     logger.debug('遍历插件,插件ID: %s' % pluginId)
    #     self.assertTrue(self.appOperate.check_plugin(pluginId, '专家观点'), '插件: %s 断言失败' % pluginId)
    #
    # def test_E2(self):
    #     '''用例名称: 存在的插件ID,不存在的断言,测试用例失败专用 '''
    #     pluginId = 'PA00500000000_02_GPZH'
    #     logger.debug('遍历插件,插件ID: %s' % pluginId)
    #     self.assertTrue(self.appOperate.check_plugin(pluginId, '专家2观点'), '插件: %s 断言失败' % pluginId)

if __name__=='__main__':
    try:
        print '*' * 40, " 开始测试 ", '*' * 40
        suite = unittest.TestSuite()
        # 跑指定某一个用例
        # suite.addTest(Anydoor_UI("test_A1"))
        # suite.addTest(Anydoor_UI("test_A3"))
        # suite.addTest(Anydoor_UI("test_D3"))
        # suite.addTest(Anydoor_UI("test_E0"))
        #加载一个测试类下的所有测试用例
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromTestCase(Anydoor_UI)

        timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        report_path = '/Users/zengyuanchen/Documents/Project/Anydoor_UI/output/html/' + timestr + '_report.html'
        ReportObject = open(report_path, "wb")
        testRunner = HTMLTestRunner(stream=ReportObject,title='测试报告',description='IOS UI 自动化')
        testRunner.run(suite)
        ReportObject.close()
        print '*' * 40, " 结束测试 ", '*' * 40
    except Exception as e:
        logger.error(e)
    # finally:
    #     appiumserver.stop_server()
    # finally:
    #     driver.quit()
