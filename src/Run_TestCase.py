# -*- coding:utf-8 -*-
#######################################################
#filename:Run_TestCase.py
#author:Jeff
#date:2016-09-21
#function:对运行用例进行操作处理
#######################################################
"""
from Global import driver
from Global import logger
from Public.readConfig import *
from Public import ExcelRW
import HtmlReport
import os,time
from CaseEngine.RunCaseEngine import RunCaseEngine
from CaseEngine.CommonFunction import *
from conf.Run_conf import *

# 保存测试结果
testcase_result = {}

# 执行所有页或指定页中的所有测试用例
def run_all_testcase(datafile,xlseng, *sheets):
    sheetsn = len(sheets)
    if 0 == sheetsn:
        testcase_file_sheets = xlseng.sheets()
    else:
        testcase_file_sheets = sheets

    # sheets页循环
    for sheetn in testcase_file_sheets:
        logger.debug('当前sheet页是: %s ' % sheetn)
        nrow = xlseng.info(sheetn)[0] - 1    #用例总行数
        logger.debug('当前执行的xlseng.info(sheetn)[0]页是: %s' % xlseng.info(sheetn[0]))
        logger.debug('当前执行的xlseng.info(sheetn)[1]页是: %s' % xlseng.info(sheetn[1]))
        test_id_list = [x for x in range(nrow)]  #testid列表
        for testid in test_id_list:
            logger.debug('开始执行用例: %s, %d' % (sheetn, testid+1))
            test_result = Runner_TestCase(datafile,sheetn,testid)
            testcase_result[(sheetn,testid+1)] = test_result  #写测试结果
            logger.debug('执行结果[%s, %d]: %s' %  (sheetn, testid+1, str(test_result)))
    return 0

# 执行测试用例
def run_testcase(data_file, conf_file, report_file=None):
    #读配置文件
    logger.debug('配置文件: %s' % os.path.abspath(conf_file))
    # case_conf = load_config(conf_file)
    runmode =read_config('runmode','mode')

    #初始化数据文件对象
    logger.debug('数据文件: %s' % os.path.abspath(data_file))
    xlseng = ExcelRW.XlsEngine(data_file)
    xlseng.open()

    #初始化测试结果报告对象
    # logger.debug('报告文件: %s' % os.path.abspath(report_file))
    # tcHtmlReport = HtmlReport()
    # tcHtmlReport.set_result_filename(report_file)

    #记录测试开始时间
    start_time = time.time()

    try:
        #运行模式：全部执行
        if "0" == runmode:
            logger.debug('运行模式：全部执行')
            run_all_testcase(data_file,xlseng)

        #运行模式：部分执行
        elif "1" == runmode:
            logger.debug('运行模式：部分执行')
            testcase_dict = get_index()
            logger.debug('待执行用例： ' + str(testcase_dict))
            if {} == testcase_dict:
                logger.debug('所有都执行')
                run_all_testcase(data_file,xlseng)
            else:
                testcase_sheets = testcase_dict.keys()
                # sheets页循环
                for sheetn in testcase_sheets:
                    test_id_list = testcase_dict[sheetn]
                    if [] == test_id_list:
                        run_all_testcase(data_file,xlseng, sheetn)
                    else:
                        for testid in test_id_list:
                            logger.debug('开始执行用例: %s, %s ' % (sheetn, testid))
                            test_result = Runner_TestCase(data_file,sheetn,testid)
                            testcase_result[(sheetn,testid)] = test_result  #写测试结果
                            logger.debug('执行结果[%s, %s]: [%s %s %s %s]' %  (sheetn, testid, str(test_result[1]),str(test_result[2]),str(test_result[4]),str(test_result[6])))

        #运行模式：部分不执行
        elif "2" == runmode:
            logger.debug('运行模式：部分不执行')
            untestcase_dict = get_unindex()
            logger.debug('不执行用例： ' + str(untestcase_dict))
            if {} == untestcase_dict:
                logger.debug('所有都不执行')
                pass
            else:
                untestcase_sheets = untestcase_dict.keys()
                testcase_file_sheets = xlseng.sheets()
                testcase_sheets = [x for x in testcase_file_sheets if x not in untestcase_sheets]
                # sheets页循环
                for sheetn in testcase_sheets:
                    untest_id_list = untestcase_dict[sheetn]
                    if [] == untest_id_list:
                        pass
                    else:
                        nrow = xlseng.info(sheetn)[0] - 1
                        testid_all_list = [x for x in range(nrow)]  #所有testid列表
                        test_id_list = [x for x in testid_all_list if x not in untest_id_list]
                        for testid in test_id_list:
                            logger.debug('开始执行用例: %s, %s ' % (sheetn, testid))
                            test_result = Runner_TestCase(data_file,sheetn,testid)
                            testcase_result[(sheetn,testid)] = test_result  #写测试结果
                            logger.debug('执行结果[%s, %s]: %s' % (sheetn, testid, str(test_result)))  #日志编码问题？

        else:
            print "运行模式配置错误！"
            logger.error('运行模式配置错误')

    except Exception as e:
        logging.exception(e)

    finally:
        #测试结束时间
        end_time = time.time()

        #生成测试报告
        # logger.debug('testcase_result: %s' % str(testcase_result))
        # tcHtmlReport.set_testcase_result(testcase_result)
        # tcHtmlReport.set_run_time(end_time - start_time)
        # tcHtmlReport.generate_html(u'UI自动化测试结果'.encode('gbk'), xlseng, case_conf)


if __name__ == '__main__':
    # '''
    data_file = os.path.abspath('../TestCase/Excel/TestCase.xlsx')
    conf_file = os.path.abspath('../conf/monitor.ini')
    report_file = '../result/Test_Report_Filename.html'
    print 'data_file = '+data_file
    print 'conf_file = ' + conf_file
    run_testcase(data_file, conf_file)
    # '''
    # pass
"""