#coding=gbk
#######################################################
#filename:Comm_Function.py
#author:defias
#date:2015-8
#function:公共函数、全局变量
#######################################################
from src.Public import ExcelRW
from RunCaseEngine import RunCaseEngine
from RunCaseEngine import RunElementEngine
from src.Global import *
from conf.Run_conf import read_config

# 用例文件列字段定义
testcase_col = {u'CaseSuite(案例)':1, u'CaseID(步骤id)':2, u'Description(步骤描述)':3, u'Action_Keyword(操作)':4,
                u'ios or android(ios或android独有操作)':5, u'Element(元素封装)':6, u'PageObject(页面元素)':7,u'Parameter(传入参数)':8}

element_col = {u'元素封装':1,u'定位方式(android)':2,u'元素实体(android)':3,
               u'索引(android)':4,u'定位方式(ios)':5,u'元素实体(ios)':6,u'索引(ios)':7}

platformName = read_config('appium','platformName')

def Get_Element_Excel(datafile, sheetn, element_row):
    element_rown = element_row +1
    # 列定义
    element_coln = element_col[u'元素封装']
    operate_type_andr_coln = element_col[u'定位方式(android)']
    operate_type_ios_coln = element_col[u'定位方式(ios)']
    operate_value_andr_coln = element_col[u'元素实体(android)']
    operate_value_ios_coln = element_col[u'元素实体(ios)']
    operate_index_andr_coln = element_col[u'索引(android)']
    operate_index_ios_coln = element_col[u'索引(ios)']

    # 初始化测试用例文件对象
    xlseng = ExcelRW.XlsEngine(datafile)
    xlseng.open()

    # 存储读取的数据
    element_name = xlseng.readcell(sheetn, element_rown, element_coln)
    operate_type_andr = xlseng.readcell(sheetn, element_rown, operate_type_andr_coln)
    operate_type_ios = xlseng.readcell(sheetn, element_rown, operate_type_ios_coln)
    operate_value_andr = xlseng.readcell(sheetn, element_rown, operate_value_andr_coln)
    operate_value_ios = xlseng.readcell(sheetn, element_rown, operate_value_ios_coln)
    operate_index_andr = xlseng.readcell(sheetn, element_rown, operate_index_andr_coln)
    operate_index_ios = xlseng.readcell(sheetn, element_rown, operate_index_ios_coln)

    element_result_list ={}
    if platformName.lower() == 'ios':
        run_element_engine_ios = RunElementEngine(element_name,operate_type_ios,operate_value_ios,operate_index_ios)
        return run_element_engine_ios
    elif platformName.lower() == 'android':
        run_element_engine_andr = RunElementEngine(element_name,operate_type_andr,operate_value_andr,operate_index_andr)
        return run_element_engine_andr
    else:
        logger.warning('暂不支持的平台类型')
        return 0

# 初始化获取一条测试用例信息
def Runner_TestCase(datafile, sheetn, testid):
    #用例所在行
    testcase_rown = testid + 1

    #列定义
    case_id_coln = testcase_col[u'CaseID(步骤id)']
    case_suit_coln = testcase_col[u'CaseSuite(案例)']
    case_description_coln = testcase_col[u'Description(步骤描述)']
    case_api_coln = testcase_col[u'Action_Keyword(操作)']
    andr_or_ios_coln = testcase_col[u'ios or android(ios或android独有操作)']
    case_element_coln = testcase_col[u'Element(元素封装)']
    case_pageobject_coln = testcase_col[u'PageObject(页面元素)']
    case_param_coln = testcase_col[u'Parameter(传入参数)']

    #初始化测试用例文件对象
    xlseng = ExcelRW.XlsEngine(datafile)
    xlseng.open()

    # 存储读取的数据
    case_id = xlseng.readcell(sheetn, testcase_rown, case_id_coln)
    case_suit = xlseng.readcell(sheetn, testcase_rown, case_suit_coln)
    # case_description = xlseng.readcell(sheetn, testcase_rown, case_description_coln)
    case_api = xlseng.readcell(sheetn, testcase_rown, case_api_coln)
    andr_or_ios = xlseng.readcell(sheetn, testcase_rown, andr_or_ios_coln)
    case_element = xlseng.readcell(sheetn, testcase_rown, case_element_coln)
    case_pageobject = xlseng.readcell(sheetn, testcase_rown, case_pageobject_coln)
    case_param = xlseng.readcell(sheetn, testcase_rown, case_param_coln)

    result_list = [] # 存放函数返回结果
    runcaseengine = RunCaseEngine(case_id,case_api,andr_or_ios,case_element,case_pageobject,case_param)
    runcase_operate = runcaseengine.operate()
    result_list.append(runcase_operate)
    #tresponse=result_list.append(response)
    #print "tresponse",tresponse
    result_list.append(case_suit)
    result_list.append(case_api)
    result_list.append(andr_or_ios)
    result_list.append(case_element)

    #print "result_list=",result_list
    return result_list

# 获取用例文件中的用例名称和接口名称
def Get_Testcase_Name(datafile, sheetn, testid):
    #用例所在行
    testcase_rown = testid + 1
    #列定义
    casename_coln = testcase_col[u'用例名称']
    operate_type_coln = testcase_col[u'定位方式']
    operate_value_coln = testcase_col[u'定位元素']

    #初始化测试用例文件对象
    xlseng = ExcelRW.XlsEngine(datafile)
    xlseng.open()

    casename = xlseng.readcell(sheetn, testcase_rown, casename_coln)
    operate_type = xlseng.readcell(sheetn, testcase_rown, operate_type_coln)
    operate_value = xlseng.readcell(sheetn, testcase_rown, operate_value_coln)
    # 根据报告输出调整返回值的顺序
    return casename,operate_type,operate_value

if __name__ == '__main__':
    datafile = '..\\..\\TestCase\\Excel\\TestCase.xlsx'
    result_list = Runner_TestCase(datafile, 'Sheet1', 1)
    print result_list
    # response = result_list[0]
    # # print response.status_code
    # print response.headers
    # print response.content

    #print Get_Testcase_Name(datafile,'Sheet1', 1)[2]
