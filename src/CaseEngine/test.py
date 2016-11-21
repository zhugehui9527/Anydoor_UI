# -*- coding:utf-8 -*-
#######################################################
#filename:Run_TestCase.py
#author:Jeff
#date:2016-09-21
#function:对运行用例进行操作处理
#######################################################
import os
from src.Public.ExcelRW import *
# from CaseEngine import *
# from ElementEngine import *

excel_path = os.path.abspath('../../TestCase/Excel/TestCase.xlsx')
print excel_path

xlseng = XlsEngine(excel_path)

xlseng.open()

sheets =  xlseng.sheets() #
elements = xlseng.readrow(u'元素表',2)
readsheet = xlseng.readsheet(u'公共案例库') # 默认打开Sheet1
# print u'sheet1 全部内容 = %s ' % readsheet
# print u'sheet1 : ' , readsheet[1][0]
print u'所有sheet: ',sheets
print u'获取sheet中行和列: ',xlseng.info(u'公共案例库') #读取sheet中行数和列数
print u'读取第一行',xlseng.readrow(u'公共案例库',1)
print u'读取第一列',xlseng.readcol(u'公共案例库',1)
print u'API行数: ' ,len(xlseng.readcol(u'公共案例库',4) )-1

def getPulicCaseNameList(sheetName,colth):
	new_list = []
	cols = xlseng.readcol(sheetName,colth)
	#去掉列表中空值操作
	for cell in cols:
		if cell != '':
			new_list.append(cell)
	return new_list
pubCaseList = getPulicCaseNameList(u'公共案例库',1)
print u'公共案例库用例列表: ',pubCaseList
print u'公共案例库用例个数: ',len(pubCaseList) - 1



# print len(aa)
#
# for rowns_list in readsheet:
# 	print rowns_list
	#
	# for cell in rowns_list:
	# 	if cell=='':
	# 		cell='null'
	# 	print cell

def run_all_testcase(excel_path,xlseng, *sheets):
    sheetsn = len(sheets)
    if 0 == sheetsn:
        testcase_file_sheets = xlseng.sheets() #读取所有sheet
    else:
        testcase_file_sheets = sheets

    # sheets页循环
    for sheetn in testcase_file_sheets:
        # logger.debug('当前sheet页是: %s ' % sheetn)
        nrow = xlseng.info(sheetn)[0] - 1    #用例总行数
        # logger.debug('当前执行的xlseng.info(sheetn)[0]页是: %s' % xlseng.info(sheetn[0]))
        # logger.debug('当前执行的xlseng.info(sheetn)[1]页是: %s' % xlseng.info(sheetn[1]))
        test_id_list = [x for x in range(nrow)]  #testid列表
        for testid in test_id_list:
            # logger.debug('开始执行用例: %s, %d' % (sheetn, testid+1))
            test_result = Runner_TestCase(datafile,sheetn,testid)
            testcase_result[(sheetn,testid+1)] = test_result  #写测试结果
            # logger.debug('执行结果[%s, %d]: %s' %  (sheetn, testid+1, str(test_result)))
    return 0





# print u'操作说明sheet = %s, 元素表sheet = %s ' % (sheets[0],sheets[1])
# print u'公共案例库sheet =%s ,sheet1 = %s' %  (sheets[2],sheets[3])
#
# print u'xlseng.info: ',xlseng.info()
#
# print u'Sheet1 第1单元格: ',xlseng.readcell('Sheet1',1,1)
#
# print u'Sheet1 第1行: ',xlseng.readrow('Sheet1',1)
#
# print u'Sheet1 第1列: ' ,xlseng.readcol('Sheet1', 2)
#
# print u'元素表 第一行: ',elements
# for element in elements:
# 	print element

# element_engine = ElementEngine()


