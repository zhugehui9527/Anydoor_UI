#coding=utf8
#######################################################
#filename:Interface_Test.py
#author:defias
#date:2015-7
#function:
#######################################################
from src.Element import Element
from src.Global import logger
from src.appOperate import AppOperate
from src.Common import *
from conf.Run_conf import read_config
from src.CaseEngine import ElementEngine


#元素和方法封装
class CaseEngine(object):
    def __init__(self,operate_row,operate_type,operate_value,operate_index):
        self.wd = Element()
        self.operate_type = operate_type
        self.operate_value = operate_value
        self.operate_index = operate_index
        self.operate_row = operate_row
        self.elementEngine = ElementEngine.ElementEngine()
        self.platformName = read_config('appium', 'platformName')
        self.time2wait = public.time2wait
        self.appoperate = AppOperate()

    # 点击操作
    def click(self):
        try:
            el = self.elementEngine.get_excel_eleObject()
            el.click()
        except AttributeError as A:
            logger.error(A)
            raise

    #输入框发送事件
    def sendkeys(self):
        pass

        # if self.data == '':
        #     if self.index == '':
        #         try:
        #             el = self.find_element()
        #             el.clear()
        #             # logger.debug('清除输入框内容')
        #             el.send_keys(self.data)
        #             logger.debug('输入框输入: %s' % self.data)
        #         except Exception as e :
        #             logger.error(e)
        #             raise e
        #     else:
        #         try:
        #             el = self.find_elements()
        #             el.clear()
        #             logger.debug('清除输入框内容')
        #             el.send_keys(self.data)
        #             logger.debug('输入框输入: %s' % self.data)
        #         except Exception as e:
        #             logger.error(e)
        #             raise e
        # else:
        #     logger.warning('没有从excel中获取到data')

    def swipe_left(self):
        self.wd.swipe_left()

    def swipe_right(self):
        self.wd.swipe_right()

    def assertTrue(self):
        assert self.appoperate.wait_for_text(int(self.data),self.operate_value)

    def assertNotTrue(self):
        assert not self.appoperate.wait_for_text(int(self.data),self.operate_value)

    def waitFortext(self):
        '''
        :param text:
        :param time2wait:
        :return:
        '''
        return self.appoperate.wait_for_text(int(self.data),self.operate_value)


    def closeH5(self):
        '''
        :return:
        '''
        return self.appoperate.closeH5()

    def closeH5_ByPluginid(self,pluginid):
        '''
        :param pluginid:
        :return:
        '''
        return self.appoperate.closeH5_byPluginId(pluginid)

    def hidekeyboard(self):
        return self.wd.hide_keyboard()

if __name__ == 'main':
    caseengine = CaseEngine('test_0001','by_id','一账通登陆')
    caseengine.click()