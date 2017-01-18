#coding=utf8
#######################################################
#filename:FindElementBy.py
#author:Jeff
#date:2016-9
#function: 查找元素相关功能与封装
#######################################################

from src.Public.Common import element_by

from src.lib.Element import Element
from src.Public.Global import L
# logger =L.logger
#读取元素表,拼接并返回element对象
class FindElementBy(object):
    def __init__(self,driver,operate_type,operate_value,operate_index):
        self.wd = Element(driver)
        self.operate_type = operate_type
        self.operate_value = operate_value
        self.operate_index = operate_index

    def get_excel_eleObject(self):
        if len(self.operate_index) == 0:
            return self.find_element(self.operate_type,self.operate_value)
        else:
            return self.find_elements(self.operate_type,self.operate_value,int(self.operate_index))


    def find_element(self,by_type,by_value):
        L.logger.debug('调用查找元素方法: find_element,查找方式: %s ,查找元素值: %s ' % (by_type, by_value))
        element_by_dic = {element_by.by_id: lambda :self.wd.by_id(by_value),
                         element_by.by_classname: lambda :self.wd.by_classname(by_value),
                         element_by.by_name: lambda :self.wd.by_name(by_value),
                         element_by.by_xpath: lambda :self.wd.by_xpath(by_value)
                         }
        if by_type:
            if element_by_dic.has_key(str(by_type).lower()):
                return element_by_dic[str(by_type).lower()]()
            else:
                L.logger.warning('暂不支持的类型: %s' % by_type)
        else:
            L.logger.warning('by_type为空')

    def find_elements(self,by_type,by_value,by_index):
        L.logger.debug('调用查找元素方法: find_elements,查找方式: %s ,查找元素值: %s ,元素索引: %s' % (by_type,by_value,by_index))
        
        elements_by_dic = {element_by.by_classname: lambda : self.wd.by_classnames(by_value)[by_index],
                           element_by.by_id: lambda : self.wd.by_ids(by_value)[by_index],
                           element_by.by_name: lambda : self.wd.by_names(by_value)[by_index],
                           element_by.by_xpath: lambda : self.wd.by_xpaths(by_value)[by_index]
                          }
        if by_type:
            if elements_by_dic.has_key(by_type.lower()):
                # L.logger.debug('字典key值: %s ,字典value: %s' % (by_type,elements_by_dic[by_type]))
                return elements_by_dic[by_type.lower()]()
            else:
                L.logger.warning('暂不支持的类型: %s' % by_type)
        else:
            L.logger.warning('by_type为空')


if __name__ == 'main':
    caseengine = FindElementBy('test_0001','by_id','一账通登陆')
