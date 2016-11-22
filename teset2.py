# -*- coding:utf-8 -*-
from src.ExcelOperate.ReadApi import ReadApi
from conf.Run_conf import read_config
from src.Public import ExcelRW
from src.Common import public

# '''
xls_file_path = read_config('testcase', 'xls_case_path')
xlsEngine = ExcelRW.XlsEngine(xls_file_path)
xlsEngine.open() # 打开excel


readApi = ReadApi()
# readApi.callPublicCase('SwipeToClickPersonalCenter')
# readApi.callPublicCase('loginyztByH5')



case_sheet1 = xlsEngine.readsheet(public.case_sheet)
readApi.callCase(case_sheet1)
# '''
