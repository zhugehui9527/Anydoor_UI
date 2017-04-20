# -*- coding:utf-8 -*-
import pytest,os

def run_pytest():
	'''
	运行pytest单元测试框架并生成html测试报告
	:return:
	'''
	project_path = os.path.dirname(os.path.abspath(__file__))
	case_path = os.path.abspath(os.path.join(project_path, 'TestCase', 'Scripts', 'Anydoor.py'))
	# print 'case_path = ',case_path
	from src.Public.Global import S
	udid = S.device['udid']
	report_path = os.path.abspath('./output/{}/html/pytest_report.html'.format(udid))
	xml_path =  os.path.abspath('./output/{}/html/pytest_report.xml'.format(udid))
	# 命令拼接,注意每一个参数之间加空格
	# cmd 加参数 -s 输出日志但是html报告不显示日志,加 --capture=no 不输出日志,html报告显示日志,--rerun 1 失败重跑次数1,
	# --self-contained-html 自包含html报告,样式文件包含在html中 ;--junitxml= 生成xml格式报告
	# -q 静默模式
	cmd = '-s ' + case_path + ' --html=' + report_path + ' --rerun 1' + ' --self-contained-html' + ' --junitxml=' + xml_path
	# print '*' * 80
	print '* [',__name__,'::',run_pytest.__name__,'] :',' pytest执行命令 : ' ,cmd
	print '*' * 80
	# 运行命令
	# os.system(cmd1)
	pytest.main(cmd)
	from src.Public.Global import D
	D.driver.close_app()
	D.driver.quit()

