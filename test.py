# -*- coding:utf-8 -*-
import os

case_path = os.path.abspath('./TestCase/Scripts/Anydoor.py')
report_path = os.path.abspath('./output/html/report.html')

# 命令拼接,注意每一个参数之间加空格
cmd1 = 'py.test ' + case_path + ' --html=' + report_path + ' --rerun 1' + ' --self-contained-html'
os.system(cmd1)