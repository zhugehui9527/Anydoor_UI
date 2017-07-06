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
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
def get_now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

class Utils:
    def __init__(self):
        pass

    @staticmethod
    def cmd_subprocess(cmd):
        '''执行shell命令'''
        # shell设为true，程序将通过shell来执行
	    # stdin, stdout, stderr分别表示程序的标准输入、输出、错误句柄。
	    # 他们可以是PIPE，文件描述符或文件对象，也可以设置为None，表示从父进程继承。
	    # subprocess.PIPE实际上为文本流提供一个缓存区

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
		self.test_db_path = PATH('../../data/test.db')
		self.conn = sqlite3.connect(self.test_db_path)
		self.cursor = self.conn.cursor()
		self.__is_table()

	def execute(self, *args, **kwargs):
		"""

        :param args:
        :param kwargs:
        :return: 提交数据
        """
		self.cursor.execute(*args, **kwargs)

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
	        case_id INTEGER PRIMARY KEY,
	        case_name TEXT,
	        device_name TEXT,
	        cpu_list TEXT,
	        mem_list TEXT,
	        execution_status TEXT,
	        created_time DATETIME DEFAULT (datetime('now', 'localtime'))
	    );""")

	def insert_per(self, case_name, device_name, cpu_list, mem_list, execution_status, ):
		key = "(case_name,device_name,cpu_list,mem_list,execution_status,created_time)"
		values = "('{}','{}','{}','{}','{}','{}')" \
			.format(case_name, device_name, cpu_list, mem_list, execution_status, get_now_time())
		self.execute("INSERT INTO test_results {} VALUES {}".format(key, values))

	def select_per(self, case_name, device_name):
		statement = "select * from test_results where " \
					"case_name = '{}' " \
					"and " \
					"device_name = '{}' " \
					"and " \
					"execution_status = 1 " \
					"order by created_time desc".format(case_name, device_name)
		self.cursor.execute(statement)
		row = self.cursor.fetchone()
		if row is not None:
			cpu = re.findall(r"\d+\.?\d*", row[3])
			mem = re.findall(r"\d+\.?\d*", row[4])
			return [int(i) for i in cpu], [int(i) for i in mem]
		else:
			return None


if __name__ == '__main__':
	s = SQL()
