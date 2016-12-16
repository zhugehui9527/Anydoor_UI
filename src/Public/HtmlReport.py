#coding=UTF-8
#######################################################
#filename:HtmlReport.py
#author:Jeff
#date:2016-11
#function:
#######################################################

import os
import platform
import sys
import time
import requests
from src.lib.Log import LogSignleton
from conf.Run_conf import read_config
from src.Public.Common import resultStutas
from src.lib import pyh

reload(sys)
sys.setdefaultencoding('utf8')
# HTML测试报告
class HtmlReport(object):
    def __init__(self):
        self.current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.title = 'Test Report Page'       #网页标签名称
        self.filename = ''                    #结果文件名
        self.time_took = '00:00:00'           #测试耗时
        self.success_num = 0                  #测试通过的用例数
        self.fail_num = 0                     #测试失败的用例数
        self.error_num = 0                    #运行出错的用例数
        self.case_total = 0                   #运行测试用例总数
        self.logfile = ''                     #每个用例运行日志
        self.logerr = ''                      #每个用例运行错误日志
        # self.logpath = read_config('logger','log_file')
        
    #设置结果文件名
    def set_result_filename(self, filename='Test_Report_Filename.html'):
        self.filename = filename
        #判断是否为目录
        if os.path.isdir(self.filename):
            raise IOError("%s must point to a file" % filename)
        elif '' == self.filename:
            raise IOError('filename can not be empty')
        else:
            parent_path, ext = os.path.splitext(filename)
            tm = time.strftime('%Y%m%d%H%M%S', time.localtime())
            self.filename = parent_path + tm + ext   #报告名中添加当前时间

    # 设置测试用例执行结果
    def set_testcase_result(self, testcase_result, testcase_message=None):
        self.testcase_result = testcase_result
        self.testcase_message = testcase_message
        self.case_total = len(testcase_result)
        self.success_num = len([x for x in testcase_result if x[1] in [resultStutas.success]])
        self.fail_num = len([x for x in testcase_result if x[1] in [resultStutas.fail]])
        self.error_num = len([x for x in testcase_result if x[1] in [resultStutas.error]])

    # 设置测试总耗时
    def set_run_time(self, seconds):
        self.time_took = time.strftime('%H:%M:%S', time.gmtime(seconds))
        return self.time_took
    
    def read_filter_log(self,casename):
        filter_log_path = read_config('testcase','project_path')+'/output/html/filter/{}.log'.format(casename).encode('utf-8')
        print filter_log_path
        try:
            with open(filter_log_path) as f:
                text =  f.read()
                return text
        except Exception as e:
            print e
        
    def get_url_res(self,url):
        res = requests.get(url).status_code
        return res
    
    #生成HTML报告
    def generate_html(self, report_header):
        def get_tab():
            tab = page << pyh.table()
            #设置表格属性
            tab.attributes['border'] = '1'   # 表格边框
            tab.attributes['cellpa dding'] = '1'   # 单元格边沿与其内容之间的空白
            tab.attributes['cellspacing'] = '0'   # 单元格之间间隔
            tab.attributes['cl'] = 'table'
            tab.attributes['borderColor'] = '#504F4F'
            tab.attributes['width'] = '90%'
            return tab
        page = pyh.PyH(self.title)
        css_url = 'https://cdn.static.runoob.com/libs/bootstrap/3.3.7/css/bootstrap.min.css'
        js1_url = 'https://cdn.static.runoob.com/libs/jquery/2.1.1/jquery.min.js'
        js2_url = 'https://cdn.static.runoob.com/libs/bootstrap/3.3.7/js/bootstrap.min.js'
        if self.get_url_res(css_url)== 200:
            page.addCSS(css_url)
        else:
            css_local = './css/bootstrap.min.css'
            page.addCSS(css_local)
        if self.get_url_res(js1_url) == 200:
            page.addJS(js1_url)
        else:
            js1_local = './js/jquery.min.js'
            page.addJS(js1_local)
        if self.get_url_res(js2_url) == 200:
            page.addJS(js2_url)
        else:
            js2_local = './js/bootstrap.min.js'
            page.addJS(js2_local)
        
        page << pyh.h1(report_header, align='middle') #标题居中
        # page << pyh.p(u'报告生成时间：'.encode('gbk') + str(self.current_time))
        page << pyh.h3('Environment', align='left')  # 标题居左
        tab2 = get_tab()
        
        # 表格头
        tab2 << pyh.tr(pyh.td(u'报告生成时间'.encode('gbk'), bgcolor='#E6E6FA', align='middle') +
                       pyh.td(u'Platform'.encode('gbk'), bgcolor='#E6E6FA', align='middle') +
                       pyh.td(u'Python'.encode('gbk'), bgcolor='#E6E6FA', align='middle') +
                       pyh.td(u'Appium'.encode('gbk'), bgcolor='#E6E6FA', align='middle')
                       ,bt='0')

        tab2 << pyh.tr(pyh.td(str(self.current_time), align='middle') +
                       pyh.td(str(platform.platform()), align='middle') +
                       pyh.td(str(platform.python_version()), align='middle') +
                       pyh.td(str(os.popen('appium -v').read()), align='middle')
                       )

        page << pyh.h3('Summary', align='left')  # 标题居左
        tab1 = get_tab()

        # 表格头
        tab1 << pyh.tr(pyh.td(u'测试总耗时'.encode('gbk'), bgcolor='#E6E6FA', align='middle') +
                       pyh.td(u'测试用例总数'.encode('gbk'), bgcolor='#E6E6FA', align='middle') +
                       pyh.td(u'成功用例数'.encode('gbk'), bgcolor='#E6E6FA', align='middle') +
                       pyh.td(u'失败用例数'.encode('gbk'), bgcolor='#E6E6FA', align='middle') +
                       pyh.td(u'报错用例数'.encode('gbk'), bgcolor='#E6E6FA', align='middle'))

        tab1 << pyh.tr(pyh.td(str(self.time_took), align='middle') +
                       pyh.td(str(self.case_total), align='middle') +
                       pyh.td(str(self.success_num), align='middle') +
                       pyh.td(str(self.fail_num), align='middle') +
                       pyh.td(str(self.error_num), align='middle'))
        
        page << pyh.h3('Results', align='left')  # 标题居左
        
        tab = get_tab()

        # 表格头
        tab << pyh.tr(pyh.td(u'用例名称'.encode('gbk'), bgcolor='#E6E6FA', align='middle') +
                      pyh.td(u'运行时间(s)'.encode('gbk'), bgcolor='#E6E6FA', align='middle') +
                      pyh.td(u'运行日志'.encode('gbk'), bgcolor='#E6E6FA', align='middle') +
                      pyh.td(u'测试结果'.encode('gbk'), bgcolor='#E6E6FA', align='middle'))
        
        # print resultlist
        for testcase_list in self.testcase_result:
            testcase_id = str(self.testcase_result.index(testcase_list))
            # print 'testcase_id = ',testcase_id
            testresult = testcase_list[1]
            testcase_name = testcase_list[0]
            testcase_duration = str(testcase_list[2])
            testcase_log = self.read_filter_log(testcase_name)
            # print 'testcase_log = %s ' % testcase_log
            testcase_log_detail =u'日志详情'
            
            start_filter = '测试用例:{} ,执行开始'.format(testcase_name)
            # print 'start_filter = %s' % start_filter
            end_filter = '测试用例:{} ,执行结束'.format(testcase_name)
        
            LogSignleton.get_filter_log(testcase_name,start_filter,end_filter)

            if 'PASS' == testresult:
                tab << pyh.tr(pyh.td(testcase_name.encode('gbk', 'ignore'), align='middle') +
                              pyh.td(testcase_duration.encode('gbk', 'ignore'), align='middle') +
                              pyh.td(pyh.div(pyh.div(pyh.a(testcase_log_detail.encode('gbk','ignore'),
                                                           dt='collapse',
                                                           href='#{}'.format(testcase_id),
                                                           dp='#accordion',
                                                           cl='collapsed',
                                                           ae='false',
                                                           align='middle')+
                                                     pyh.div(testcase_log.encode('gbk', 'ignore'),
                                                                     id=testcase_id,
                                                                     cl='panel-collapse collapse',
                                                                     ae='false',
                                                                     style='height: 0px;',
                                                                    align='left'),
                                                           
                                                     style='background-color: #70DBDB;',
                                                     # cl='panel panel-default' #边框
                                                     ),
                                             id='accordion',cl='panel-group',style='margin-bottom: 0px;'),
                                     align='middle') +
                              pyh.td(testresult, align='middle'), bgcolor='#70DBDB')
                
            elif 'FAIL' == testresult:
                tab << pyh.tr(pyh.td(testcase_name.encode('gbk', 'ignore'), align='middle') +
                              pyh.td(testcase_duration.encode('gbk', 'ignore'), align='middle') +
                              pyh.td(pyh.div(pyh.div(pyh.a(testcase_log_detail.encode('gbk', 'ignore'),
                                                           dt='collapse',
                                                           href='#{}'.format(testcase_id),
                                                           dp='#accordion',
                                                           cl='collapsed',
                                                           ae='false',
                                                           align='middle') +
                                                     pyh.div(testcase_log.encode('gbk', 'ignore'),
                                                                     id=testcase_id,
                                                                     cl='panel-collapse collapse',
                                                                     ae='false',
                                                                     style='height: 0px;',
                                                                    align='left'),
                                                            
                                                     style='background-color: #FF6EC7;',
                                                     # cl='panel panel-default'
                                                     ),
                                             id='accordion', cl='panel-group',style='margin-bottom: 0px;'),
                                     align='middle') +
                              pyh.td(testresult, align='middle'), bgcolor='#FF6EC7')

            elif 'ERROR' == testresult:
                tab << pyh.tr(pyh.td(testcase_name.encode('gbk', 'ignore'), align='middle') +
                              pyh.td(testcase_duration.encode('gbk', 'ignore'), align='middle') +
                              pyh.td(pyh.div(pyh.div(pyh.a(testcase_log_detail.encode('gbk', 'ignore'),
                                                           dt='collapse',
                                                           href='#{}'.format(testcase_id),
                                                           dp='#accordion',
                                                           cl='collapsed',
                                                           ae='false',
                                                           align='middle') +
                                                    pyh.div(testcase_log.encode('gbk', 'ignore'),
                                                                     id=testcase_id,
                                                                     cl='panel-collapse collapse',
                                                                     ae='false',
                                                                     style='height: 0px;',
                                                                    align='left'),
                                                             
                                                     style='background-color: #DB7093;',
                                                     # cl='panel panel-default'
                                                     ),
                                             id='accordion', cl='panel-group',style='margin-bottom: 0px;'),
                                     align='middle') +
                              pyh.td(testresult, align='middle'), bgcolor='#DB7093')
            else:
                tab << pyh.tr(pyh.td(testcase_name.encode('gbk', 'ignore'), align='middle') +
                              pyh.td(testcase_duration.encode('gbk', 'ignore'), align='middle') +
                              pyh.td(pyh.div(pyh.div(pyh.a(testcase_log_detail.encode('gbk', 'ignore'),
                                                           dt='collapse',
                                                           href='#{}'.format(testcase_id),
                                                           dp='#accordion',
                                                           cl='collapsed',
                                                           ae='false',
                                                           align='middle') +
                                                     pyh.div(testcase_log.encode('gbk', 'ignore'),
                                                                     id=testcase_id,
                                                                     cl='panel-collapse collapse',
                                                                     ae='false',
                                                                     style='height: 0px;',
                                                                    align='left'),
                                                           
                                                     style='background-color: #FF00FF;',
                                                     # cl='panel panel-default'
                                                     ),
                                             id='accordion', cl='panel-group',style='margin-bottom: 0px;'),
                                     align='middle') +
                              pyh.td(testresult, align='middle'), bgcolor='#FF00FF')
                
        # print self.filename
        page.printOut(self.filename)
'''
import datetime
import StringIO
import sys
import time
import unittest
TestResult = unittest.TestResult

class OutputRedirector(object):
    """ Wrapper to redirect stdout or stderr """
    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(s)

    def writelines(self, lines):
        self.fp.writelines(lines)

    def flush(self):
        self.fp.flush()

stdout_redirector = OutputRedirector(sys.stdout)
stderr_redirector = OutputRedirector(sys.stderr)

class _TestResult(TestResult):
    # note: _TestResult is a pure representation of results.
    # It lacks the output and reporting ability compares to unittest._TextTestResult.

    def __init__(self, verbosity=1):
        TestResult.__init__(self)
        self.stdout0 = None
        self.stderr0 = None
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.verbosity = verbosity

        # result is a list of result in 4 tuple
        # (
        #   result code (0: success; 1: fail; 2: error),
        #   TestCase object,
        #   Test output (byte string),
        #   stack trace,
        # )
        self.result = []


    def startTest(self, test):
        TestResult.startTest(self, test)
        # just one buffer for both stdout and stderr
        self.outputBuffer = StringIO.StringIO()
        stdout_redirector.fp = self.outputBuffer
        stderr_redirector.fp = self.outputBuffer
        self.stdout0 = sys.stdout
        self.stderr0 = sys.stderr
        sys.stdout = stdout_redirector
        sys.stderr = stderr_redirector


    def complete_output(self):
        """
        Disconnect output redirection and return buffer.
        Safe to call multiple times.
        """
        if self.stdout0:
            sys.stdout = self.stdout0
            sys.stderr = self.stderr0
            self.stdout0 = None
            self.stderr0 = None
        return self.outputBuffer.getvalue()


    def stopTest(self, test):
        # Usually one of addSuccess, addError or addFailure would have been called.
        # But there are some path in unittest that would bypass this.
        # We must disconnect stdout in stopTest(), which is guaranteed to be called.
        self.complete_output()


    def addSuccess(self, test):
        self.success_count += 1
        TestResult.addSuccess(self, test)
        output = self.complete_output()
        self.result.append((0, test, output, ''))
        if self.verbosity > 1:
            sys.stderr.write('ok ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('.')

    def addError(self, test, err):
        self.error_count += 1
        TestResult.addError(self, test, err)
        _, _exc_str = self.errors[-1]
        output = self.complete_output()
        self.result.append((2, test, output, _exc_str))
        if self.verbosity > 1:
            sys.stderr.write('E  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('E')

    def addFailure(self, test, err):
        self.failure_count += 1
        TestResult.addFailure(self, test, err)
        _, _exc_str = self.failures[-1]
        output = self.complete_output()
        self.result.append((1, test, output, _exc_str))
        if self.verbosity > 1:
            sys.stderr.write('F  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('F')
'''
if __name__ == '__main__':
    tcHtmlReport = HtmlReport()
    path = '/Users/zengyuanchen/Documents/SVN/ShareFromCloud/share/Project/Anydoor_UI/output/html/report.html'
    tcHtmlReport.set_result_filename(path)

    testcase_result =[['登录_1000', 'PASS','2016-11-1'], ['获取插件列表','FAIL','2016-11-2'], ['检查插件:PA01100000000_02_PAZB', 'ERROR','2016-11-3']]

    tcHtmlReport.set_testcase_result(testcase_result)
    tcHtmlReport.set_run_time(123)
    tcHtmlReport.generate_html('测试报告'.encode('gbk'))
