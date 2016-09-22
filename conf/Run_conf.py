#coding=utf8
#######################################################
#filename:Run_conf.py
#author:Jeff
#date:2016-09
#function:运行加载配置数据
#######################################################
from src import Run_TestCase
from src.Public import logger
import os

data_file = '..\\TestCase\\TestCase.xlsx'
conf_file = '.\\monitor.ini'
report_file = '..\\output\\html\\Test_Report_Filename.html'
log_file ='..\\output\\log\\AnyDoor_UI.log'

print 'TestCase Running...'
logger.GenerateLog(log_file)
print os.path.basename(conf_file)
# Run_TestCase.run_testcase(data_file, conf_file, report_file)
print 'TestCase Run End'