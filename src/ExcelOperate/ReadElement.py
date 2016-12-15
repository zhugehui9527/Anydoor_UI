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
from src.Public.Global import L
from src.lib import ExcelRW

logger = L.logger
#元素和方法封装
class ReadElement(object):
    def __init__(self):
        self.platformName = read_config('appium', 'platformName')
        self.xls_file_path = read_config('testcase', 'xls_case_path')
        self.xlsEngine = ExcelRW.XlsEngine(self.xls_file_path)
        self.xlsEngine.open() # 打开excel
        # self.element_name_list = self.xlsEngine.readcol(element_by_excel.element_sheet_name,1) #读取元素表第一列
        self.element_list = self.xlsEngine.readsheet(public.element_sheet)
        
    def find_element(self,element_list=[]):
        '''
        :desc:excel 元素表中查找元素
        :param element_list:
        :return:
        '''
        logger.debug('element_list : %s' % element_list)
        if self.platformName.lower() == 'ios':
            operate_type = element_list[4] #操作类型
            operate_value = element_list[5] #操作值
            operate_index = element_list[6] #索引
            logger.debug('operate_type: %s' % operate_type)
            logger.debug('operate_value: %s' % operate_value)
            logger.debug('operate_index: %s' % operate_index)
            
        elif self.platformName.lower() == 'android':
            operate_type = element_list[1] #操作类型
            operate_value = element_list[2] #操作值
            operate_index = element_list[3] #索引
        else:
            logger.warning('暂不支持的平台')
        elementEngine = FindElementBy.FindElementBy(str(operate_type), str(operate_value), str(operate_index))
        find_element = elementEngine.get_excel_eleObject()
        return find_element
    
    # 读取元素表的每一行,判断是否包含元素,并返回改行元素所在列表
    def read_element_text(self,element_text):
        '''
        :param element_text:
        :return:row_list
        :eg: row_list=['消息中心','xpath','//android.widget.TextView[@text='消息中心']',...]
        '''
        # logger.debug('元素表: %s' % self.element_list)
        for row_list in self.element_list[1:]:
            # logger.debug('元素表中每一行的元素列表为: %s' % row_list)
            # logger.debug('元素表中第一列元素为: %s' % row_list[0])
            if element_text == row_list[0]:
                logger.debug('元素表中存在此元素: %s' % element_text)
                return row_list
           
                
    

