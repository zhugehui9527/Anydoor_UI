#coding=utf8
#######################################################
#filename:HtmlReport.py
#author:defias
#date:2015-7
#function:
#######################################################
import sys
# from src.Public.Public import pyh
import time
import os

# HTML测试报告
class HtmlReport(object):
    def __init__(self):
        self.title = 'Test Report Page'       #网页标签名称
        self.filename = ''                    #结果文件名
        self.time_took = '00:00:00'           #测试耗时
        self.success_num = 0                  #测试通过的用例数
        self.fail_num = 0                     #测试失败的用例数
        self.error_num = 0                    #运行出错的用例数
        self.case_total = 0                   #运行测试用例总数

    #设置结果文件名
    def set_result_filename(self, filename='Test_Report_Filename.html'):
        self.filename = filename
        #判断是否为目录
        if os.path.isdir(self.filename):
            raise IOError("%s must point to a file" % self.filename)
        elif '' == self.filename:
            raise IOError('filename can not be empty')
        else:
            parent_path, ext = os.path.splitext(filename)
            tm = time.strftime('%Y%m%d%H%M%S', time.localtime())
            self.filename = parent_path + tm + ext   #报告名中添加当前时间

    # 设置测试用例执行结果
    def set_testcase_result(self, testcase_result):
        self.testcase_result = testcase_result
        if {} != self.testcase_result:
            self.case_total = len(testcase_result)
            self.success_num = len([x for x in testcase_result.values() if x[0] in ['PASS']])
            self.fail_num = len([x for x in testcase_result.values() if x[0] in ['FAIL']])
            self.error_num = len([x for x in testcase_result.values() if x[0] in ['ERROR']])
        else:
            self.case_total = 0
            self.success_num = 0
            self.fail_num = 0
            self.error_num = 0

    # 设置测试总耗时
    def set_run_time(self, seconds):
        self.time_took = time.strftime('%H:%M:%S', time.gmtime(seconds))
        return self.time_took

    #生成HTML报告
    def generate_html(self, report_title, xlseng, tiancheng_case_conf):
        page = pyh.PyH(self.title)
        page << pyh.h1(report_title, align='middle') #标题居中
        page << pyh.p(u'测试总耗时：'.encode('gbk') + str(self.time_took))
        page << pyh.p(u'测试用例总数：'.encode('gbk') + str(self.case_total))
        page << pyh.p(u'成功用例数：'.encode('gbk') + str(self.success_num))
        page << pyh.p(u'失败用例数：'.encode('gbk') + str(self.fail_num))
        page << pyh.p(u'出错用例数：'.encode('gbk') + str(self.error_num))

        tab = page << pyh.table()
        #设置表格属性
        tab.attributes['border'] = '1'   #表格边框
        tab.attributes['cellpadding'] = '1'   #单元格边沿与其内容之间的空白
        tab.attributes['cellspacing'] = '0'   #单元格之间间隔
        tab.attributes['cl'] = 'table'
        tab.attributes['borderColor'] = '#504F4F'
        tab.attributes['width'] = '90%'

        #表格头
        tab << pyh.tr(pyh.th(u'用例ID'.encode('gbk'), bgcolor='#E6E6FA', align='left') + pyh.th(u'用例名称'.encode('gbk'), bgcolor='#E6E6FA', align='left') +
            pyh.th(u'测试项'.encode('gbk'), bgcolor='#E6E6FA', align='left') + pyh.th(u'测试项类型'.encode('gbk'), bgcolor='#E6E6FA', align='left') +
            pyh.th(u'测试结果'.encode('gbk'), bgcolor='#E6E6FA', align='left') + pyh.th(u'提示信息'.encode('gbk'), bgcolor='#E6E6FA', align='left'))

        if {} == self.testcase_result:
            page.printOut(self.filename)
            print self.filename
            return -1

        for sheetn,testcase_id in sorted(self.testcase_result.keys(), key=lambda x: x[1]):
            test_report_id = sheetn + '_' + str(testcase_id)
            #print test_report_id#

            #从用例文件中读取用例相关名称
            #testcase_name,interface_type,interface_name = Comm_Function.Get_Testcase_Name(datafile,sheetn,testcase_id)

            #用例所在行
            testcase_rown = testcase_id + 1

            testcase_col = tiancheng_case_conf.get_testfile_coln()
            #列号
            testcase_name_coln = testcase_col['test_name']  #用例名称列
            interface_type_coln = testcase_col['interface_type']  #接口类型列
            interface_name_coln = testcase_col['interface_name']  #接口名称列

            testcase_name = xlseng.readcell(sheetn, testcase_rown, testcase_name_coln)
            interface_type = xlseng.readcell(sheetn, testcase_rown, interface_type_coln)
            interface_name = xlseng.readcell(sheetn, testcase_rown, interface_name_coln)

            testresult = self.testcase_result[(sheetn, testcase_id)][0]
            if 'PASS' == testresult:
                testinfo = ''
            else:
                testinfo = self.testcase_result[(sheetn, testcase_id)][1]

            if 'PASS' == testresult:
                tab << pyh.tr(pyh.td(test_report_id, align='left') + pyh.td(testcase_name.encode('gbk'), align='left') +
                    pyh.td(interface_name.encode('gbk'), align='left') + pyh.td(interface_type.encode('gbk'), align='left') +
                    pyh.th(testresult, bgcolor='#00ff00', align='left') + pyh.th(testinfo.decode('utf-8').encode('gbk'), align='left'))
            elif 'FAIL' == testresult:
                tab << pyh.tr(pyh.td(test_report_id, align='left') + pyh.td(testcase_name.encode('gbk'), align='left') +
                    pyh.td(interface_name.encode('gbk'), align='left') + pyh.td(interface_type.encode('gbk'), align='left') +
                    pyh.th(testresult, bgcolor='#F9032C', align='left') + pyh.th(testinfo.decode('utf-8').encode('gbk'), align='left'))
            else:
                tab << pyh.tr(pyh.td(test_report_id, align='left') + pyh.td(testcase_name.encode('gbk'), align='left') +
                    pyh.td(interface_name.encode('gbk'), align='left') + pyh.td(interface_type.encode('gbk'), align='left') +
                    pyh.th(testresult, bgcolor='#DA03C5', align='left') + pyh.th(testinfo.decode('utf-8').encode('gbk'), align='left'))

        page.printOut(self.filename)
        print self.filename
        return 0

if __name__ == '__main__':
    tcHtmlReport = HtmlReport()
    tcHtmlReport.set_result_filename()

    testcase_result = {('Sheet1',1):'PASS', ('Sheet1',2):'ERROR'}
    tcHtmlReport.set_testcase_result(testcase_result)
    tcHtmlReport.set_run_time(123)
    tcHtmlReport.generate_html(u'测试结果'.encode('gbk'),'.\data\TestCase.xlsx')
