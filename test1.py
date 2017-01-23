# -*- coding:utf-8 -*-
from selenium import webdriver
import time

B = webdriver.Chrome('/Users/zengyuanchen/Documents/Project/UIAutoTest/UIAutoTest/tools/driverServer/chromedriver')
B.get('https://www.baidu.com/')
# B.find_element_by_id('kw').send_keys('test')
# time.sleep(3)
# B.find_element_by_class_name('bg s_btn_wr').click()
# time.sleep(3)
T = B.find_elements_by_name('tj_login')

try:
	T[0].click()
	print 'T0'
except:
	T[1].click()
	print 'T1'
