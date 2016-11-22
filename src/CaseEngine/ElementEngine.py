#coding=utf8
#######################################################
#filename:Interface_Test.py
#author:defias
#date:2015-7
#function:
#######################################################
from src.Element import Element
from src.Global import logger
from src.Common import element_by

#读取元素表,拼接并返回element对象
class ElementEngine(object):
    def __init__(self,operate_type,operate_value,operate_index):
        self.wd = Element()
        self.operate_type = operate_type
        self.operate_value = operate_value
        self.operate_index = operate_index

    def get_excel_eleObject(self):
        if self.operate_index == '':
            return self.find_element(self.operate_type,self.operate_value)
        else:
            return self.find_elements(self.operate_type,self.operate_value,self.operate_index)


    def find_element(self,by_type,by_value):
        logger.debug('调用查找元素方法: find_element')
        element_by_dic = {element_by.by_id: lambda :self.wd.by_id(by_value),
                         element_by.by_classname: lambda :self.wd.by_classname(by_value),
                         element_by.by_name: lambda :self.wd.by_name(by_value),
                         element_by.by_xpath: lambda :self.wd.by_xpath(by_value)
                         }
        if by_type:
            if element_by_dic.has_key(str(by_type).lower()):
                return element_by_dic[str(by_type).lower()]()
            else:
                logger.warning('暂不支持的类型: %s' % by_type)
        else:
            logger.warning('by_type为空')

    def find_elements(self,by_type,by_value,by_index):
        logger.debug('调用查找元素方法: find_elements')
        elements_by_dic = {element_by.by_id:  self.wd.by_ids(by_value)[int(by_index)],
                          element_by.by_classname: self.wd.by_classnames(by_value)[int(by_index)],
                          element_by.by_name:  self.wd.by_names(by_value)[int(by_index)],
                          element_by.by_xpath:  self.wd.by_xpaths(by_value)[int(by_index)]
                          }
        if by_type:
            if elements_by_dic.has_key(str(by_type).lower()):
                # logger.debug('字典key值: %s ,字典value: %s' % (self.operate_type,elements_by_dic[self.operate_type]))
                return elements_by_dic[str(by_type).lower()]()
            else:
                logger.warning('暂不支持的类型: %s' % by_type)
        else:
            logger.warning('by_type为空')


if __name__ == 'main':
    caseengine = ElementEngine('test_0001','by_id','一账通登陆')
