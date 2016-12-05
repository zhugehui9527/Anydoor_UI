# -*- coding:utf-8 -*-
#######################################################
#filename:readConfig.py
#author:Jeff
#date:2016-09-21
#function:对配置文件进行操作处理
from src.Common import resultStutas
from src.Global import logger
# isRetrys=True
def Retry(retry_count = 3,isRetry=True):
	'''
	:description:失败重跑
	:param retry_count: 重跑次数
	:return:
	'''
	def info(func):
		if isRetry:
			def wrapper(*args, **kwargs):
				result_func = func(*args, **kwargs)
				logger.debug('调用函数: %s' % func.__name__)
				casename = result_func[0]  # 返回用例名
				caseresult = result_func[1]  # 返回结果
				if result_func:
					for x in range(retry_count):
						logger.debug('当前用例名称: %s ,当前执行结果: %s' % (casename, caseresult))
						if caseresult in (resultStutas.fail,resultStutas.error):
							logger.debug('失败重跑第 【 %s 】 次执行中' % str(x+1))
							t = func(*args, **kwargs)
							retry_name = t[0]
							retry_result = t[1]
							logger.debug('失败重跑执行用例: %s ,执行结果:%s' %(retry_name,retry_result))
						else:
							break
					# return t
				else:
					logger.warning('函数: %s 返回结果为空' % func.__name__)
	
			return wrapper
	
	return info
