#coding=utf8
#######################################################
#filename:Interface_Test.py
#author:defias
#date:2015-7
#function:
#######################################################
from src.Element import Element
from src.Global import *
from src.appOperate import AppOperate
from src.Common import *

#元素和方法封装
class CaseEngine(object):
    def __init__(self,testid,operate_type,operate_value,data=None,index=None):
        '''
        :param testid:
        :param operate_type:
        :param operate_value:
        :param data:
        :param index:
        '''
        self.wd = Element()
        self.operate_type = operate_type
        self.operate_value = operate_value
        self.data = data
        self.index = index
        self.testid = testid
        # self.operate_method = operate_method
        self.time2wait = public.time2wait
        self.appoperate = AppOperate()

    def find_element(self):
        logger.debug('调用查找元素方法: find_element')
        element_by_dic = {element_by.by_id:lambda: self.wd.by_id(self.operate_value),
                         element_by.by_classname:lambda: self.wd.by_classname(self.operate_value),
                         element_by.by_name:lambda: self.wd.by_name(self.operate_value),
                         element_by.by_xpath:lambda: self.wd.by_xpath(self.operate_value)
                         }
        if self.testid:
            if element_by_dic.has_key(str(self.operate_type).lower()):
                logger.debug('如果testid不为空,返回对应的操作: %s' % element_by_dic[str(self.operate_type).lower()])
                return element_by_dic[str(self.operate_type).lower()]
            else:
                logger.warning('暂不支持的类型: %s' % self.operate_type)
                return False  # 暂不支持的类型

        # if self.operate_type == 'by_id':
        #     return self.wd.by_id(self.opetate_value)
        # elif self.operate_type == 'by_xpath':
        #     return self.wd.by_xpath(self.opetate_value)
        # elif self.operate_type == 'by_name':
        #     return self.wd.by_name(self.opetate_value)
        # elif self.operate_type == 'by_classname':
        #     return self.wd.by_classname(self.opetate_value)
        # else:
        #     logger.warning('暂不支持的类型: %s' % self.operate_type)
        #     return 0  # 0 暂不支持的类型

    def find_elements(self):
        elements_by_dic = {element_by.by_id: lambda: self.wd.by_ids(self.operate_value)[int(self.index)],
                          element_by.by_classname:lambda: self.wd.by_classnames(self.operate_value)[int(self.index)],
                          element_by.by_name: lambda: self.wd.by_names(self.operate_value)[int(self.index)],
                          element_by.by_xpath: lambda: self.wd.by_xpaths(self.operate_value)[int(self.index)]
                          }
        if self.testid:
            if elements_by_dic.has_key(str(self.operate_type).lower()):
                logger.debug('字典key值: %s ,字典value: %s' % (self.operate_type,elements_by_dic[self.operate_type]))
                return elements_by_dic[str(self.operate_type).lower()]
            else:
                logger.warning('暂不支持的类型: %s' % self.operate_type)
                return False  # 暂不支持的类型

        # if self.operate_type == 'by_ids':
        #     return self.wd.by_ids(self.opetate_value)[self.index]
        # elif self.operate_type == 'by_xpaths':
        #     return self.wd.by_xpaths(self.opetate_value)[self.index]
        # elif self.operate_type == 'by_names':
        #     return self.wd.by_names(self.opetate_value)[self.index]
        # else:
        #     logger.warning('暂不支持的类型: %s' % self.operate_type)
        #     return 0  # 0 暂不支持的类型

    # 点击操作
    def click(self):
        if self.index is None:
            logger.debug('索引为 空')
            try:
                logger.debug('find_element 点击操作')
                el = self.find_element()
                el.click()

            except AttributeError as A:
                logger.error(A)
                raise
        else:
            logger.debug('索引为: %d' % int(self.index))
            try:
                els =self.find_elements()
                els.click()
                logger.debug('find_elements 点击操作')
            except AttributeError as A:
                logger.error(A)
                raise

    #输入框发送事件
    def sendkeys(self):
        if self.data is not None:
            if self.index is None:
                try:
                    el = self.find_element()
                    el.clear()
                    logger.debug('清除输入框内容')
                    el.send_keys(self.data)
                    logger.debug('输入框输入: %s' % self.data)
                except Exception as e :
                    logger.error(e)
                    raise e
            else:
                try:
                    el = self.find_elements()
                    el.clear()
                    logger.debug('清除输入框内容')
                    el.send_keys(self.data)
                    logger.debug('输入框输入: %s' % self.data)
                except Exception as e:
                    logger.error(e)
                    raise e
        else:
            logger.warning('没有从excel中获取到data')

    def swipe_left(self):
        self.wd.swipe_left()

    def swipe_right(self):
        self.wd.swipe_right()

    def assertTrue(self,expr,msg=None):
        '''
        :param condition:
        :param msg:
        :return:
        '''
        assert expr,msg

    def assertNotTrue(self,expr,msg=None):
        '''
        :param condition:
        :param msg:
        :return:
        '''
        assert not expr,msg

    def waitFortext(self,text,time2wait):
        '''
        :param text:
        :param time2wait:
        :return:
        '''
        return self.appoperate.wait_for_text(time2wait,text)


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


if __name__ == 'main':
    caseengine = CaseEngine('test_0001','by_id','一账通登陆')
    caseengine.click()