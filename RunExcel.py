# -*- coding:utf-8 -*-
#######################################################
# filename:RunExcel.py
# author:Jeff
# date:2016-11-21
# function:驱动Excel测试用例
#######################################################
import time,unittest,os
from conf.Run_conf import read_config
from src.ExcelOperate.ReadApi import ReadApi
from src.Public.Common import operate_api,public,resultClass,resultStutas
from src.Public.Global import L,D,S
from src.Public.Retry import Retry
from src.lib import ExcelRW
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

retry_num = int(read_config('retry', 'retry_num'))
retry_isTrue = bool(read_config('retry', 'retry_isTrue'))
# project_path = read_config('testcase', 'project_path')
result = resultClass.result

class RunExcelCase(unittest.TestCase):
	
	def __init__(self,caselist,mouldeName):
		super(RunExcelCase,self).__init__(mouldeName)
		self.driver = D.driver
		self.readApi = ReadApi(self.driver)
		self.xls_file_path = os.path.abspath('./TestCase/Excel/TestCase.xlsx')
		self.platformName = S.device['platformName']
		self.xlsEngine = ExcelRW.XlsEngine(self.xls_file_path)
		self.xlsEngine.open()  # 打开excel
		self.publicCaseList = self.xlsEngine.readsheet(public.public_case_sheet)
		self.sheetCaseList = self.xlsEngine.readsheet(public.case_sheet)
		self.caselist = caselist
	
	def callPublicCase(self, casename):
		'''
		:description:判断casename是否在公共案例库中,如有则执行公共案例库
		:param casename:
		:return:   还缺少对ios或者Android独有的判断
		'''
		public_case_type = 1 #公共案例库名称不为空
		result_public = [] #存放公共案例库执行结果
		L.logger.debug('callPublicCase 执行中')
		# 遍历公共案例库
		for publicCase in self.publicCaseList[1:] :
			# 执行公共案例库,案例名称为空的部分
			if public_case_type == 0:
				if (publicCase[0] == '') and (publicCase[1] !=''):
					# 判断是否是ios或者Android独有操作
					# print time.ctime(), ' [', __name__, '::', RunExcelCase.callPublicCase.__name__, '] :', ' platformName =  ', self.platformName
					if((self.platformName).lower() != str(publicCase[4]).lower()) and (len(publicCase[4]) != 0):
							# L.logger.debug('1 continue 跳出循环 : %d' % public_case_type)
							L.logger.debug('%s 独有操作' % str(publicCase[4]).lower())
					else:
						if self.readApi.readApiList(publicCase):
							# 公共案例每步执行结果记录
							result_public.append(resultStutas.success)
						else:
							# 公共案例每步执行结果记录
							result_public.append(resultStutas.fail)
				else:
					# 跳出循环
					break
			else:
				# 先定位到指定案例
				if casename == publicCase[0]:
					result_public.append(publicCase[0]) #添加公共案例-用例名
					# publicCaseID = publicCase[1]
					L.logger.debug('公共案例库中存在此方法: %s' % casename)
					# L.logger.debug('连接设备的平台类型: [ %s ]' % self.platformName.lower())
					# L.logger.debug('Excel表格中的平台类型: [ %s ]' % str(publicCase[4]).lower())
					if ((self.platformName).lower() != str(publicCase[4]).lower()) and (len(publicCase[4]) != 0):
						# L.logger.debug('0 continue 跳出循环 : %d' % public_case_type)
						L.logger.debug('%s 独有操作' % str(publicCase[4]).lower())
						#跳出本次循环
						# continue
					else:
						# L.logger.debug('0 执行api并记录结果: %d' % public_case_type)
						if self.readApi.readApiList(publicCase):
							# 公共案例每步执行结果记录
							result_public.append(resultStutas.success)
						else:
							# 公共案例每步执行结果记录
							result_public.append(resultStutas.fail)
						
					public_case_type = 0
				
		return result_public
	
	
	#function:运行一条测试用例,Retry 失败重跑,1重跑次数,isRetry重跑开关
	@Retry(retry_count=retry_num,isRetry=retry_isTrue)
	def function(self):
		L.logger.warning('测试用例:%s ,执行开始' % self.caselist[0])
		case_start_time = time.time()
		case_list = []
		case_list.append(self.caselist[0])
		# 判断是否为公共库api
		if operate_api.publicCase == self.caselist[3]:
			# 执行公共案例库
			result_public = self.callPublicCase(self.caselist[7])
			L.logger.debug('公共案例库执行记录: %s' % result_public)
			if resultStutas.fail in result_public:
				# result[self.caselist[0]] = resultStutas.fail
				case_list.append(resultStutas.fail)
			else:
				# result[self.caselist[0]] = resultStutas.success
				case_list.append(resultStutas.success)
			if case_list:
				L.logger.debug('===' * 40)
				L.logger.debug('当前用例:%s ,执行结果: %s' % (case_list[0],case_list[1]))
				L.logger.debug('===' * 40)
			else:
				L.logger.warning('case_list 为空')
		
		else:
			# 执行测试用例库
			if self.readApi.readApiList(self.caselist):
				case_list.append(resultStutas.success)
			else:
				case_list.append(resultStutas.fail)
			if case_list:
				L.logger.debug('===' * 40)
				# L.logger.debug('执行结果记录: %s' % case_list)
				L.logger.warning('当前用例:%s ,执行结果: %s' % (case_list[0],case_list[1]))
				L.logger.debug('===' * 40)
			else:
				L.logger.warning('case_list 为空')
				
		case_cost_time = time.time() - case_start_time
		case_cost_time =round(case_cost_time,3)
		retry_flag = 'FALSE'
		case_list.append(case_cost_time)
		case_list.append(retry_flag)
		# 判断result列表最后一个元素是否是当前的测试用例,如果是当前用例则更新原用例的结果,如果不是,则添加新结果
		if result:
			if result[-1][0] == case_list[0]:
				result[-1][1]= case_list[1] # 更新结果
				result[-1][2] = case_list[2] # 更新时间
				if resultStutas.success not in case_list:
					retry_flag = 'TRUE'
					result[-1][3] = retry_flag
			else:
				result.append(case_list)
		else:
			result.append(case_list)
		
		L.logger.warning('测试用例:%s ,执行结束' % self.caselist[0])
		L.logger.warning('用例执行总结果: %s' % result)
		return case_list

def get_html_report():
	from src.Public.Global import S
	device = S.device
	udid = device['udid']
	html_result_path = os.path.abspath('./output/{}/html/report.html'.format(udid))
	# 测试结束时间
	end_time = time.time()
	from src.Public.HtmlReport import HtmlReport
	AHtmlReport = HtmlReport()
	print '*' * 80
	print time.ctime(), ' [', __name__, '::', get_html_report.__name__, '] :', ' 生成测试报告'
	# 生成测试报告
	AHtmlReport.set_result_filename(html_result_path)
	AHtmlReport.set_testcase_result(result)
	AHtmlReport.set_run_time(end_time - time.time())
	AHtmlReport.generate_html('测试报告')
	

if __name__ == '__main__':
	
	# current_path = os.getcwd()
	# timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
	# report_path = current_path + '/output/html/'+ timestr + '_report.html'
	# ReportObject = open(report_path, "wb")
	# testRunner = HTMLTestRunner.HTMLTestRunner(stream=ReportObject, title='Report', description='IOS')
	#
	# # runner = unittest.TextTestRunner()
	# Run_Case(testRunner)
	# ReportObject.close()
	#
	
	runner = unittest.TextTestRunner(verbosity=2)
	# Run_Case(runner)
	