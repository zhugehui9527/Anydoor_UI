#coding=utf8
#######################################################
#filename:Interface_Test.py
#author:defias
#date:2015-7
#function:
#######################################################

# # from src.Element import Element
# from src.Global import logger
# from src.appOperate import AppOperatef
# from src.CaseEngine import ElementEngine
from conf.Run_conf import read_config
from src.Public import ExcelRW
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
xls_file_path = read_config('testcase', 'xls_case_path')
print xls_file_path
xlsEngine = ExcelRW.XlsEngine(xls_file_path)
xlsEngine.open()
element_sheet_row_list = xlsEngine.readrow(u'元素表',1)
element_sheet_col_list = xlsEngine.readcol(u'元素表',1)
read_sheet_element = xlsEngine.readsheet(u'元素表')
read_sheet_pulcase_list = xlsEngine.readsheet(u'公共案例库')
print element_sheet_row_list[0]
print element_sheet_col_list[1:]
print '*'*40
for pulcase in read_sheet_pulcase_list:
	# print pulcase
	# print (pulcase[6]), pulcase[7]
	
	if 'SwipeToClickPersonalCenter' in pulcase[0]:
		print pulcase
		print 'pass'
	else:
		pass


# element_dict ={}
# for row_list in read_sheet[1:]:
# 	element_name = row_list[0]
# 	#ios
# 	operate_type = row_list[4]
# 	operate_value = row_list[5]
# 	operate_index = row_list[6]
#
# 	elementEngine = ElementEngine.ElementEngine(operate_type,operate_value,operate_index)
# 	find_element = elementEngine.get_excel_eleObject()
# 	element_dict[element_name]= find_element

# print element_dict
	
		
