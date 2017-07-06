# -*- coding:utf-8 -*-
#######################################################
#filename:Public.py
#author:Jeff
#date:2016-12-21
#function:公共函数封装
#######################################################

import tempfile
import platform
import shutil
import os
from PIL import Image

PATH = lambda p:os.path.abspath(p)

class Img(object):
	# 获取临时截图目录的绝对路径
	temp_file = PATH(tempfile.gettempdir() + '/temp_screen.png')

	def __init__(self,driver):
		self.driver = driver

	def get_screenshot_by_element(self,element):
		'获取指定元素的截图'
		# 截取整个屏幕
		self.driver.screenshot_as_file(self.temp_file)
		location = element.location
		size = element.size
		box = (location['x'],location['y'],location['x']+size['width'],location['y']+size['height'])
		# 截取指定大小的图片
		image = Image.open(self.temp_file) #打开
		new_image = image.crop(box) # 截图
		new_image.save(self.temp_file) #保存
		return self

	def get_screen_by_size(self,percent_x,percent_y,percent_width,percent_height):
		'''
		根据指定大小进行屏幕截图
		:param start_x: 起点宽度百分比
		:param start_y: 起点高度百分比
		:param end_x: 宽度百分比
		:param end_y: 高度百分比
		:return:
		'''
		# 截图并保存到 temp_file

		self.driver.screenshot_as_file(self.temp_file)

		image = Image.open(self.temp_file)
		width = image.size[0]
		height = image.size[1]
		box = (int(percent_x * width),
		       int(percent_y * height),
		       int((percent_width + percent_x) * width) ,
		       int((percent_height + percent_y) * height))
		# print 'box = ',box
		# 裁剪
		new_image = image.crop(box)
		new_image.save(self.temp_file)
		# print '裁剪后的图片路径:',temp_file
		return self

	def copy_to_file(self,dirpath,imagename,form='png'):
		'复制截屏文件到指定目录'
		if not PATH(dirpath):
			os.makedirs(dirpath)
		imagepath = PATH(dirpath+'/'+imagename+'.'+form)
		shutil.copy(self.temp_file,imagepath)
		return imagepath

	def load_image(self,imagepath):
		'加载图片供对比'
		if os.path.isfile(imagepath):
			load = Image.open(imagepath)
			return load
		else:
			raise Exception('%s is not exist' % imagepath)

	def compare(self,loadimage,percent):
		'对比图片,percent 为图片相似度,0最相似,数值越大差别越大'
		import math
		import operator
		image1 = Image.open(self.temp_file)
		image2 = loadimage
		h1 = image1.histogram()
		h2 = image2.histogram()
		diff = math.sqrt(map(operator.add,list(map(lambda a,b:(a-b)**2,h1,h2)))/len(h1))
		if diff <= percent:
			return True
		else:
			return False

