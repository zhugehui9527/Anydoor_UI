# -*- coding:utf-8 -*-
import pytest, os

PATH = lambda p: os.path.abspath(
	os.path.join(os.path.dirname(__file__), p)
)

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
	from src.Public.Global import L
	report_path = PATH('./output/{}/html/pytest_report.html'.format(udid))
	xml_path = PATH('./output/{}/html/pytest_report.xml'.format(udid))
	allure_xml_path = PATH('./output/{}/xml'.format(udid))
	allure_html_path = PATH('./output/{}/html'.format(udid))
	# 命令拼接,注意每一个参数之间加空格
	# cmd 加参数 -s 输出日志但是html报告不显示日志,加 --capture=no 不输出日志,html报告显示日志,--rerun 1 失败重跑次数1,
	# --self-contained-html 自包含html报告,样式文件包含在html中 ;--junitxml= 生成xml格式报告
	# -q 静默模式
	cmd = ' -s ' + case_path + ' --html=' + report_path + ' --rerun 1 ' + ' --self-contained-html' + ' --junitxml=' + xml_path
	cmd1 = ' -s ' + case_path + ' --alluredir ' + allure_xml_path
	cmd2 = 'allure generate ' + allure_xml_path + ' -o ' + allure_html_path
	# print '*' * 80

	# print ('*' * 80)
	# 运行命令
	from conf.Run_conf import read_config
	report_mode = read_config('runmode','report')

	try:
		if report_mode == '0':
			L.logger.debug(' pytest执行命令 :%s ' % cmd)
			pytest.main(cmd)
		else:
			L.logger.debug(' pytest执行命令 :%s ' % cmd1)
			pytest.main(cmd1)
			from src.lib.Utils import Utils
			L.logger.debug(' pytest执行生成html报告命令 :%s ' % cmd2)
			Utils.cmd_subprocess(cmd2)
	except Exception as e:
		L.logger.error(e)
		raise

	from src.Public.Global import D
	D.driver.close_app()
	D.driver.quit()
