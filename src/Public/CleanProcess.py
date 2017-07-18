# -*- coding: utf-8 -*-
__author__ = 'Jeff'

"""
@author:Jeff
@time: 16/11/8 下午2:52
"""
import platform
import subprocess
import time
from conf.Run_conf import read_config
from src.Public.Common import public as pc



class Cp(object):

    def __init__(self):
        self.runmode = read_config(pc.runmode, pc.driver)

    def cmd(self,cmd):
        return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def __darwin(self, port, device):
        for line in self.cmd(
            "lsof -i tcp:%s | grep node|awk '{print $2}'" %
                str(port)).stdout.readlines():
            self.cmd('kill -9 %s' % line.strip())
            # logger.debug('CleanProcess:Darwin:kill appium')
        for line in self.cmd(
                "ps -A | grep logcat | grep %s" % device).stdout.readlines():
            self.cmd('kill -9 %s' % line.strip())
            # logger.debug('CleanProcess:Darwin:kill logcat')

    def __linux(self, port, device):
        # linux必须最高权限才可获取到端口
        for line in self.cmd(
            "lsof -i:%s |awk '{print $2}'" %
                str(port)).stdout.readlines():
            self.cmd('kill -9 %s' % line.strip())
            # logger.debug('CleanProcess:linux:kill appium')
        for line in self.cmd(
            "ps -ef | grep logcat | grep %s|awk '{print $2}'" %
                device).stdout.readlines():
            self.cmd('kill -9 %s' % line.strip())
            # logger.debug('CleanProcess:linux:kill logcat')

    def clean_adb(self):
        cmd = "lsof -i :5037 |awk '{print $2}'"
        lines = self.cmd(cmd).stdout.readlines()
        lines_list = []
        lines_list.append(lines)
        if len(lines_list) != 0:
            # print (self.runmode + " 相关进程列表 = %s " % lines_list)
            # logger.debug('appium 相关进程列表 = %s ' % lines_list)
            for line in lines_list:
                for x in line:
                    cmd2 = 'kill -9 %s' % x
                    self.cmd(cmd2)

    def __darwin_all(self, ):
        # for line in self.cmd(
        #         "ps -A | grep logcat|awk '{print $1}'").stdout.readlines():
        #     self.cmd('kill -9 %s' % line.strip())
        #     logger.debug('CleanProcess:Darwin:kill logcat')
        lines_list = []
        cmd = "ps -A | grep "+self.runmode+"|awk '{print $1}'"
        lines = self.cmd(cmd).stdout.readlines()
        # print ('lines = ',lines)
        lines_list.append(lines)
        # print (lines_list)

        if len(lines_list) !=0:
            # print (self.runmode + " 相关进程列表 = %s " % lines_list)
            # logger.debug('appium 相关进程列表 = %s ' % lines_list)
            for line in lines_list:
                for x in line:
                    cmd2 = 'kill -9 %s' % x
                    self.cmd(cmd2)
                    # print ('CleanProcess:Darwin: %s'%  cmd2)
            # print ('CleanProcess:Darwin:kill %s '% self.runmode)
                # self.cmd('killall node')
                # logger.debug('CleanProcess:Darwin:kill appium')

    def __linux_all(self):
        for line in self.cmd(
                "ps -ef | grep logcat|grep -v grep|awk '{print $2}'").stdout.readlines():
            self.cmd('kill -9 %s' % line.strip())
            # logger.debug('CleanProcess:linux:kill logcat')

        for line in self.cmd(
                "ps -ef |grep "+self.runmode+" |grep -v grep|awk '{print $2}'").stdout.readlines():
            self.cmd('kill -9 %s' % line.strip())
            # logger.debug('CleanProcess:linux:kill appium')

    def __windows(self):
        # todo windows未完成
        for line in self.cmd(
                "netstat -aon|findstr 4700").stdout.readlines():
            pid = line.strip().split(' ')[-1]
            process_name = self.cmd(
                'tasklist|findstr {}'.format(pid)).stdout.read().split(' ')[0]
            self.cmd('taskkill /f /t /im {}'.format(process_name))

    def clean_process(self, port, device):
        """
        清理logcat与appium指定进程
        :return:
        """
        if platform.system() == 'Darwin':
            self.__darwin(port, device)
            self.clean_adb()
        elif platform.system() == 'Linux':
            self.__linux(port, device)
        else:
            print ('CleanProcess:Not identifying your operating system')
            # logger.debug(
            #     'CleanProcess:Not identifying your operating system')

    def clean_process_all(self, ):
        """
        清理logcat与appium所有进程
        :return:
        """
        if platform.system() == 'Darwin':
            self.__darwin_all()
            self.clean_adb()
        elif platform.system() == 'Linux':
            self.__linux_all()
        else:
            'CleanProcess:Not identifying your operating system'
            # logger.debug(
            #     'CleanProcess:Not identifying your operating system')


if __name__ == '__main__':
    c = Cp()
    # c.clean_process(4723, 'T7G0215A14000220')
    # c.clean_process_all()
    # c.darwin_all()
