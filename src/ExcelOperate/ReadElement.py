#coding=utf8
#######################################################
#filename:ReadElement.py
#author:Jeff
#date:2016-11
#function: 读取元素表并进行处理
#######################################################
from conf.Run_conf import read_config
from src.ExcelOperate import FindElementBy
from src.Public.Common import public
from src.Public.Global import L,S
from src.lib import ExcelRW

#ReadElement->FindElementBy->Element-
#元素和方法封装
class ReadElement(object):
    def __init__(self,driver):
        self.platformName = S.device['platformName']
        self.xls_file_path = read_config('testcase', 'xls_case_path')
        self.xlsEngine = ExcelRW.XlsEngine(self.xls_file_path)
        self.xlsEngine.open() # 打开excel
        self.element_list = self.xlsEngine.readsheet(public.element_sheet)
        self.driver = driver
        
    def find_element(self,element_list=[]):
        '''
        :desc:excel 元素表中查找元素
        :param element_list:
        :return:
        '''
        L.logger.debug('element_list : %s' % element_list)
        if self.platformName.lower() == 'ios':
            operate_type = element_list[4] #操作类型
            operate_value = element_list[5] #操作值
            operate_index = element_list[6] #索引
            L.logger.debug('operate_type: %s' % operate_type)
            L.logger.debug('operate_value: %s' % operate_value)
            L.logger.debug('operate_index: %s' % operate_index)
            
        elif self.platformName.lower() == 'android':
            operate_type = element_list[1] #操作类型
            operate_value = element_list[2] #操作值
            operate_index = element_list[3] #索引
        else:
            L.logger.warning('暂不支持的平台')
        elementEngine = FindElementBy.FindElementBy(self.driver,str(operate_type), str(operate_value), str(operate_index))
        find_element = elementEngine.get_excel_eleObject()
        return find_element
    
    # 读取元素表的每一行,判断是否包含元素,并返回改行元素所在列表
    def read_element_text(self,element_text):
        '''
        :param element_text:
        :return:row_list
        :eg: row_list=['消息中心','xpath','//android.widget.TextView[@text='消息中心']',...]
        '''
        # L.logger.debug('元素表: %s' % self.element_list)
        for row_list in self.element_list[1:]:
            if element_text == row_list[0]:
                L.logger.debug('元素表中存在此元素: %s' % element_text)
                return row_list
           
                
    

