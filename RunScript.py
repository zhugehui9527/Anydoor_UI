# -*- coding:utf-8 -*-
# from conf.Run_conf import read_config
import pytest,os

def run_pytest():
	# project_path = read_config('testcase','project_path')
	case_path =  os.path.abspath('./TestCase/Scripts/Anydoor.py')
	# print 'case_path = ',case_path
	from src.Public.Global import S
	udid = S.device['udid']
	report_path = os.path.abspath('./output/{}/html/report.html'.format(udid))
	xml_path =  os.path.abspath('./output/{}/html/report.xml'.format(udid))
	# 命令拼接,注意每一个参数之间加空格
	# cmd1 = 'py.test '+ case_path +' --html='+ report_path +' --rerun 1' + ' --self-contained-html'
	cmd2 = '-q ' + case_path + ' --html=' + report_path + ' --rerun 1' + ' --self-contained-html' + ' --junitxml=' + xml_path
	# print '*' * 80
	print '* [',__name__,'::',run_pytest.__name__,'] :',' pytest执行命令 : ' ,cmd2
	print '*' * 80
	# 运行命令
	# os.system(cmd1)
	pytest.main(cmd2)
	from src.Public.Global import D
	D.driver.close_app()
	D.driver.quit()
