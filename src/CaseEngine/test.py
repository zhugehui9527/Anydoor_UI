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

sheets =  xlseng.sheets()
elements = xlseng.readrow(u'元素表',2)
readsheet = xlseng.readsheet()
print u'sheet1 全部内容 = %s ' % readsheet
print u'sheet1 : ' , readsheet[1][0]
for x in readsheet:
	print x
	for y in x:
		print y

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
for element in elements:
	print element

# element_engine = ElementEngine()


