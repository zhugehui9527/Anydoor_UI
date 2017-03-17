# -*- coding:utf-8 -*-
#######################################################
#filename:Utils.py
#author:Jeff
#date:2016-12-12
#function:常用模块封装
import subprocess
import threading
import os,sys
import sqlite3
import time
import re


sys.path.append('../../')

def get_now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

class Utils:
    def __init__(self):
        pass
	
    @staticmethod
    def cmd_subprocess(cmd):
        '''执行shell命令'''
        return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
    @staticmethod
    def cmd_output(cmd):
        return subprocess.check_output(cmd)

			
class cmd_tt(threading.Thread):
	'''
	run cmd on mac
	'''
	def __init__(self, cmd):
		threading.Thread.__init__(self)
		self.cmd = cmd

	def run(self):
		os.system(self.cmd)
		
	# def cmd_Popen(self):
	# 	os.popen(self.cmd)
	
class SQL:
	def __init__(self):
		self.test_db_path = os.path.abspath('../../output/test.db')
		self.conn = sqlite3.connect(self.test_db_path)
		self.cursor = self.conn.cursor()
		self.__is_table()
		
	def execute(self,*args,**kwargs):
		'''
		执行sql
		:param args: sql语句
		:param kwargs: 关键词参数
		:return: 执行结果
		'''
		self.cursor.execute(*args,**kwargs)
	
	def close(self):
		self.cursor.close()
		self.conn.commit()
		self.conn.close()
	
	def __is_table(self):
		"""
		判断表是否存在
		:return:
		"""
		self.cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='test_results'")
		row = self.cursor.fetchone()
		if row[0] != 1:
			self.__built_table()
	
	def __built_table(self):
		"""
		建表
		:return:
		"""
		self.execute("""
	    CREATE TABLE test_results
	    (
	        case_id INTEGER PRIMARY KEY  NOT NULL,
	        case_name TEXT,
	        device_name TEXT NOT NULL,
	        filter_log TEXT,
	        screen_shot_base64 TEXT,
	        cpu_list TEXT,
	        mem_list TEXT,
	        cost_time CHAR(50),
	        result TEXT,
	        created_time DATETIME DEFAULT (datetime('now', 'localtime'))
	    );""")
	
	def insert_per(self, case_name, device_name, filter_log, cost_time,result,screen_shot_base64=None,cpu_list=None, mem_list=None):
		'''插入每个用例的执行结果'''
		key = "(case_name,device_name,filter_log,screen_shot_base64,cpu_list,mem_list,cost_time,result,created_time)"
		values = "('{}','{}','{}','{}','{}','{}','{}','{}','{}')"\
			.format(case_name, device_name, filter_log,screen_shot_base64,cpu_list, mem_list, cost_time, result,get_now_time())
		self.execute("INSERT INTO test_results {} VALUES {}".format(key, values))
		
	def update_per(self,case_name, device_name, filter_log, cost_time,result,screen_shot_base64=None,cpu_list=None, mem_list=None):
		'''SQL更新结果'''
		update_sql ="UPDATE test_results set " \
		            "filter_log='{}'," \
		            "screen_shot_base64='{}'," \
		            "cpu_list='{}'," \
		            "mem_list='{}'," \
		            "cost_time='{}'," \
		            "result='{}'," \
		            "created_time='{}' " \
		            "where case_name='{}'" \
		            "and device_name='{}'" \
		            "order by created_time desc limit 1"
		statement = update_sql.format(filter_log,screen_shot_base64,cpu_list, mem_list, cost_time, result,get_now_time(),case_name, device_name)
		# print statement
		self.cursor.execute(statement)
		self.conn.commit()
		
	def select_per(self, case_name, device_name):
		statement = "select * from test_results where " \
		            "case_name = '{}' " \
		            "and " \
		            "device_name = '{}' " \
		            " order by created_time desc".format(case_name, device_name)
		self.cursor.execute(statement)
		#抓取一行数据
		row = self.cursor.fetchone()
		return row
	
		# if row is not None:
		# 	cpu = re.findall(r"\d+\.?\d*", row[3])
		# 	mem = re.findall(r"\d+\.?\d*", row[4])
		# 	return [int(i) for i in cpu], [int(i) for i in mem]
		# else:
		# 	return None


if __name__ == '__main__':
	s = SQL()
	
	# s.insert_per('login','u123','过滤日志','30','pass','base64','cpu_lists','mem_lists')
	print s.select_per('login', 'u123')
	s.update_per('login','u123','','33','fail','base64','cpu_lists','mem_lists')
	# # s.insert_per('login1', 'u123', '过滤日志', 'base64', 'cpu_lists', 'mem_lists', '30', 'pass')
	print s.select_per('login','u123')
	s.close()