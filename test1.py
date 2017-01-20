# -*- coding:utf-8 -*-

import pytest,unittest

class A(unittest.TestCase):
	
	args = [('PA01100000000_02_PAZB','加油站'),
	        ('PA01100000000_02_WLC','值得买'),
	        ('PA00500000000_02_GSZB','热 门'),
	        ('PA01100000000_02_HDJHY','本活动的最终解释权归平安科技所有')
	        ]
	
	# @pytest.mark.parametrize("a,n",args)
	def test_timedistance_v0(self,a,n):
		'''用例名称: 检查插件,插件ID: {},插件断言:{} '''.format(a, n)
		print a,n
		

if __name__ == '__main__':
	pytest.main('-q ./test1.py')