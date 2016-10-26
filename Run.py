# -*- coding:utf-8 -*-
import os,sys,pytest_instafail

# from AppiumServer import RunServerOnMac
# from AppiumServer import AppiumServer
# appiumserver = AppiumServer()
# def driver_on():
# 	return appiumserver.start_server()
case_path = os.path.abspath('./src/Anydoor.py')
report_path = os.path.abspath('./output/html/report.html')

def run_on_mac(cmd):
	os.system(cmd)

cmd1 = 'py.test '+case_path+' --html='+ report_path +' --rerun 2'
# cmd2 = 'py.test --lf'
run_on_mac(cmd1)
# run_on_mac(cmd2)
