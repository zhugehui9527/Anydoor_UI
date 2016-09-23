#coding=utf8
#######################################################
#filename:Interface_Test.py
#author:defias
#date:2015-7
#function:
#######################################################
from Public.Public import *
from public import ExcelRW
from Assert import *
import unittest
import time
import os
import sys



# 驱动执行一条测试用例
def caseEngine(xlseng, case_conf, sheetn, testid):
    try:
        #用例所在行
        testcase_rown = testid + 1

        if __name__ == '__main__':
            testcase_col = case_conf
        #列定义
        interface_type_coln = testcase_col['interface_type']  #接口类型列
        url_path_coln = testcase_col['url_path']  #URL路径
        params_coln = testcase_col['params']  #参数列
        test_interface_id_coln = testcase_col['test_interface_id']    #Test_interface_id列
        expectation_coln =  testcase_col['expectation']  #期望结果列

        #列值
        interface_type = xlseng.readcell(sheetn, testcase_rown, interface_type_coln)   #接口类型
        url_path = xlseng.readcell(sheetn, testcase_rown, url_path_coln)   # url路径
        params = xlseng.readcell(sheetn, testcase_rown, params_coln)  # 参数
        test_interface_id = str(xlseng.readcell(sheetn, testcase_rown, test_interface_id_coln))  # 参数
        expectation = xlseng.readcell(sheetn, testcase_rown,expectation_coln)  #期望结果
    except Exception as e:
        logging.exception(e)
        raise




#测试
if __name__ == '__main__':
    datafile = '..\\TestCase.xlsx'
    conf_file = '..\\Conf.ini'
    sheetn = 'Sheet1'
    testid = 1

    xlseng = ExcelRW.XlsEngine(datafile)
    xlseng.open()
    # case_conf = Configfile_Parser.Configfile_Parser(conf_file)
    #
    # result_list = Test_Interface_Tiancheng(xlseng,  case_conf, sheetn, testid)
    # print result_list
