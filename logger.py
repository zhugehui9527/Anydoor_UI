# -*- coding:utf-8 -*-
from Public import *
import os
import logging

class Log():
	def __init__(self):
		project_path = os.getcwd()
		config_path = os.path.join((project_path + '/conf/'), 'monitor.cfg')
		ip = read_config(config_path, 'lo', 'ip')



def _instance():
	log_conf_path = file + '/conf/'
	global logger
	if logger is None:
		load_config(os.path.join(log_conf_path,'monitor.cfg'))
		logger = logging.getLogger("root")
	return logger

# def info(msg):
# 	return  _instance().info(msg)
#
# 	logpath = file + '/output/log/'
# 	config = logging.basicConfig(filename=os.path.join(logpath, 'AnyDoor_UI.log'),
# 	                    level=logging.INFO,
# 	                    format='%(asctime)s : %(filename)s[line:%(lineno)d] [ %(levelname)s ] %(message)s',
# 	                    datefmt='%Y-%m-%d %H:%M:%S',
# 	                    filemode='w'  # a 写入不覆盖,w 写入并覆盖
# 	                    )
