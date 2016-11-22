# -*- coding:utf-8 -*-
import os
# from src.Global import logger

case_path = os.path.abspath('./TestCase/Scripts/Anydoor.py')
report_path = os.path.abspath('./output/html/report.html')
cmd1 = 'py.test '+case_path+' --html='+ report_path +' --rerun 0' + ' --self-contained-html'

def run_on_mac(cmd):
	'''
	run command on mac
	:param cmd:
	:return:
	'''
	os.system(cmd)
	print '命令: ',cmd


# 运行命令
run_on_mac(cmd1)
