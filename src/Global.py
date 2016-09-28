# -*- coding:utf-8 -*-
#######################################################
#filename:Global.py
#author:Jeff
#date:2016-09-21
#function:处理全局文件变量
#######################################################
import logging
from driver import appdriver
from src.Public.logger import *
import time, datetime

global logger,driver
logger = logging.getLogger()
driver = appdriver.get_driver()

# logtest = Log()
# logtest.GenerateLog()
# loggers = logtest.get_my_logger()


#将%Y-%m-%d格式时间字符串转化为时间戳（带微秒）
def change_time(time_str):
    timeArray = time.strptime(time_str, "%Y-%m-%d")
    timeStamp = int(time.mktime(timeArray))
    timeStamp = int(str(timeStamp) + '000000')
    return timeStamp

#获取当前时间戳
def gettime_nowstamp():
    dnow = datetime.datetime.now()
    # print dnow
    dnows = str(int(time.mktime(dnow.timetuple())))
    # print dnows
    #mics = str(dnow.microsecond)
    mics = '000000'
    nows = int(dnows + mics)
    return nows

if __name__ == '__main__':
   print ''

