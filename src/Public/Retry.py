# -*- coding:utf-8 -*-
#######################################################
#filename:Retry.py
#author:Jeff
#date:2016-09-21
#function:失败重跑函数封装
#######################################################

from src.Public.Common import resultStutas
from src.Public.Global import L

def Retry(retry_count = 3,isRetry=True):
	'''
	:description:失败重跑
	:param retry_count: 重跑次数
	:return:
	'''
	def info(func):
		def wrapper(*args, **kwargs):
			result_func = func(*args, **kwargs)
			L.logger.info('重跑次数: %s' % str(retry_count))
			L.logger.info('重跑开关: %s' % str(isRetry))
			if isRetry:
				L.logger.info('调用函数: %s' % func.__name__)
				casename = result_func[0]  # 返回用例名
				caseresult = result_func[1]  # 返回结果
				
				if result_func:
					for x in range(retry_count):
						L.logger.info('当前用例名称: %s ,当前执行结果: %s' % (casename, caseresult))
						if caseresult in (resultStutas.fail,resultStutas.error):
							L.logger.info('失败重跑第 【 %s 】 次执行中' % str(x+1))
							t = func(*args, **kwargs)
							retry_name = t[0]
							retry_result = t[1]
							L.logger.info('失败重跑执行用例: %s ,执行结果:%s' %(retry_name,retry_result))
						else:
							break
					# return t
				else:
					L.logger.warning('函数: %s 返回结果为空' % func.__name__)
			else:
				return result_func
	
		return wrapper
	
	return info
