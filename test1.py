# -*- coding:utf-8 -*-

import pytest,unittest

list_1 = [('PA01100000000_02_PAZB', '加油站'),
		('PA01100000000_02_WLC', '值得买'),
        ('PA00500000000_02_GSZB', '热 门'),
        ('PA01100000000_02_HDJHY', '本活动的最终解释权归平安科技所有')
          ]

def A(a):
	for x in list_1:
		if a in x:
			print 'True'
	
args = [pytest.mark.skipif("A('PA01100000000_02_PAZB')")(('PA01100000000_02_PAZB', '加油站')),
        ('PA01100000000_02_WLC', '值得买'),
        ('PA00500000000_02_GSZB', '热 门'),
        ('PA01100000000_02_HDJHY', '本活动的最终解释权归平安科技所有')
        ]


@pytest.mark.parametrize("a,n", args)
def test_timedistance_v0( a, n):
	print a, n

if __name__ == '__main__':
	pytest.main('-q ./test1.py')
