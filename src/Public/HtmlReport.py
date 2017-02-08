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
# from conf.Run_conf import read_config
from src.Public.Common import resultStutas
from src.Public.Global import S
from src.lib import pyh

sys.path.append("../../")
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
        self.device = S.device
        # self.device = '32E6D124-29B6-48A2-9B38-0A9D54121E10'
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
            print time.ctime(), ' [', __name__, '::', self.set_result_filename.__name__, '] :', ' 生成测试报告,\n 测试报告路径 =  ', self.filename

            # 设置测试用例执行结果
    def set_testcase_result(self, testcase_result, testcase_message=None):
        self.testcase_result = testcase_result
        self.testcase_message = testcase_message
        self.case_total = len(testcase_result)
        self.success_num = len([x for x in testcase_result if x[1] in [resultStutas.success]])
        self.fail_num = len([x for x in testcase_result if x[1] in [resultStutas.fail]])
        self.error_num = len([x for x in testcase_result if x[1] in [resultStutas.error]])
        self.rerun_num = len([x for x in testcase_result if x[1] in [resultStutas.rerun]])

    # 设置测试总耗时
    def set_run_time(self, seconds):
        self.time_took = time.strftime('%H:%M:%S', time.gmtime(seconds))
        return self.time_took
    
    def read_filter_log(self,casename):
        filter_log_path = os.path.abspath('./output/{}/html/filter/{}.log'.format(self.device['udid'],casename))
        # print filter_log_path
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
        # 如果联网则调用网上连接css与js,否则调用本地css与js
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
        
        page << pyh.h1((unicode(report_header)).encode('gbk'), align='middle') #标题居中
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
                       pyh.td(u'报错用例数'.encode('gbk'), bgcolor='#E6E6FA', align='middle') +
                       pyh.td(u'重跑用例数'.encode('gbk'), bgcolor='#E6E6FA', align='middle'))

        tab1 << pyh.tr(pyh.td(str(self.time_took), align='middle') +
                       pyh.td(str(self.case_total), align='middle') +
                       pyh.td(str(self.success_num), align='middle') +
                       pyh.td(str(self.fail_num), align='middle') +
                       pyh.td(str(self.error_num), align='middle')+
                       pyh.td(str(self.fail_num), align='middle'))
        
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
            # print 'testcase_log = %s ' % testcase_log
            testcase_log_detail =u'日志详情'
            
            start_filter = '测试用例:{} ,执行开始'.format(testcase_name)
            # print 'start_filter = %s' % start_filter
            end_filter = '测试用例:{} ,执行结束'.format(testcase_name)
            try:
                LogSignleton.get_filter_log(testcase_name,start_filter,end_filter)
                testcase_log = self.read_filter_log(testcase_name)
            except Exception as e:
                print e
            else:
                print time.ctime(), ' [', __name__, '::', HtmlReport.generate_html.__name__, '] :', '日志过滤完毕!'
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
                                                     # cl='panel panel-default' # 添加按钮边框
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
                                                     # cl='panel panel-default' # 添加按钮边框
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
                                                     # cl='panel panel-default' # 添加按钮边框
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
                                                     # cl='panel panel-default' # 添加按钮边框
                                                     ),
                                             id='accordion', cl='panel-group',style='margin-bottom: 0px;'),
                                     align='middle') +
                              pyh.td(testresult, align='middle'), bgcolor='#FF00FF')
                
        # print self.filename
        page.printOut(self.filename)

if __name__ == '__main__':
    tcHtmlReport = HtmlReport()
    path = os.path.abspath('./output/html/report.html')
    tcHtmlReport.set_result_filename(path)

    testcase_result =[['登录_1000', 'PASS','2016-11-1'], ['检查插件:PA02100000001_02_JF','FAIL','2016-11-2'], ['检查插件:PA01100000000_02_PAZB', 'ERROR','2016-11-3']]

    tcHtmlReport.set_testcase_result(testcase_result)
    tcHtmlReport.set_run_time(123)
    tcHtmlReport.generate_html('测试报告')
