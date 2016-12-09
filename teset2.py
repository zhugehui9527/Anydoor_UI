# -*- coding:utf-8 -*-
# from src.ExcelOperate.ReadApi import ReadApi
import os

from conf.Run_conf import read_config
from src.Public import ExcelRW
from src.Public.Common import public

# '''
xls_file_path = read_config('testcase', 'xls_case_path')
xlsEngine = ExcelRW.XlsEngine(xls_file_path)
xlsEngine.open() # 打开excel

# readApi = ReadApi()
case_sheet1 = xlsEngine.readsheet(public.case_sheet)
print [x for x in case_sheet1]
# readApi.callCase(case_sheet1)
# '''

testcase_result = {u'test_loginByH5_1001': {'status':'PASS','timestamp':'201611'}, u'test_loginByH5_1000': {'status':'PASS','timestamp':'201612'}, u'test_CheckPlugin_1001': {'status':'PASS','timestamp':'201616'},
                   u'test_CheckPlugin_1000': {'status':'FAIL','timestamp':'201613'}, u'test_CheckPlugin_1002': {'status':'PASS','timestamp':'201614'}, u'test_getPluginList': {'status':'PASS','timestamp':'201610'}}

# case_status_list =  testcase_result.values()
# for y in  case_status_list:
#     print y
# for x in sorted(testcase_result.iteritems(),key=lambda x:x[1],reverse=False):
#     print 'x = ',x
# # pass_count = len([x for x in testcase_result.values() if x in ['PASS']])
# # print 'pass_count = ',pass_count
# test1 = sorted(testcase_result.iteritems(),key= lambda x:x[1],reverse=False)
# print 'test1= ',test1

# for testname in testcase_result:
# 	print 'testcase_name = %s' % (testname)
# 	print 'result = %s' % testcase_result[testname]
#
# print sys.platform
# print sys.version
# print '#'*40
#
# def deco(func):
#     def _deco():
#         res = func()
#         if 'ok'  in res or 'nt' in res:
#             print res
#         else:
#             print 'nothing'
#         print("  after myfunc() called.")
#         # 不需要返回func，实际上应返回原函数的返回值
#
#     return _deco
#
#
# @deco
# def myfunc():
#     print(" myfunc() called.")
#     return 'ok1','nt'
# myfunc()
#
#
# public_result = {}
# public_case ={}
# # dict1.setdefault('A','1')
# # dict1.setdefault('B','2')
# public_result['A'] = 'pass'
# public_result['B'] = 'pass'
# public_result['public_case'] =public_case
# public_case['C'] ='3'
# public_case['D'] ='4'
# # dict1['A']['time']='2016'
# # dict1['A']['result']='pass'
# # dict1['B']['time']='2015'
# # dict1['B']['result']='fail'
# print 'viewvalues = ',public_case.viewvalues()
# print 'values = ',public_case.values()
# print 'viewitems = ',public_case.viewitems()
# print 'public_result=',public_result
# if '3' in public_case.values():
#     print 'pass'
# else:
#     print  'fail'
#
# public_result_list =[]
# case_list = ['case1',['2015','pass']]
# public_result_list.append(case_list)
# print public_result_list

# case = [['case1','PASS'],['case2','FAIL']]
# print case[-1][0]


logpath = '/Users/zengyuanchen/Documents/SVN/ShareFromCloud/share/Project/Anydoor_UI/output/log/AnyDoor_UI.log'


html_path1 = '/Users/zengyuanchen/Documents/SVN/ShareFromCloud/share/Project/Anydoor_UI/output/html/report20161202095502.html'
html_path2 = '/Users/zengyuanchen/Documents/SVN/ShareFromCloud/share/Project/Anydoor_UI/output/html/report20161202095727.html'

path1 = os.path.split(html_path2)[0]
print 'html_path2 =',os.path.split(path1)[0]


time1 = 10.2730340958
print '%.3f' % time1
print round(time1,2)

'''
def get_filter_log(logpath, start_filter='', end_fileter=''):
    import os
    log_fileter_path = os.path.split(logpath)[0] + '/filter/filter.log'
    print log_fileter_path

    go_on_id = 0
    with open(log_fileter_path, 'w') as s:
        
        with open(logpath) as f:
            for line in f:
                if start_filter in line:
                    go_on_id = 1
                    s.write(line)
                elif go_on_id == 1:
                    if end_fileter not in line:
                        s.write(line)
                    else:
                        s.write(line)
                        break
    
        f.close()
    s.close()
    return log_fileter_path


start_fileter = '测试用例:H5登录001 ,执行开始'
end_fileter = '测试用例:H5登录001 ,执行结束'
log_fileter = get_filter_log(logpath,start_fileter,end_fileter)
print log_fileter
'''