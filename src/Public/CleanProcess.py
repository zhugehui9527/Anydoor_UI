# -*- coding: utf-8 -*-
__author__ = 'Jeff'

"""
@author:Jeff
@time: 16/11/8 下午2:52
"""
import platform
import subprocess

from src.Public.Global import L
logger = L.logger


class Cp(object):
	
    def cmd(self,cmd):
        return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
    def __darwin(self, port, device):
        for line in self.cmd(
            "lsof -i tcp:%s | grep node|awk '{print $2}'" %
                str(port)).stdout.readlines():
            self.cmd('kill -9 %s' % line.strip())
            logger.debug('CleanProcess:Darwin:kill appium')
        for line in self.cmd(
                "ps -A | grep logcat | grep %s" % device).stdout.readlines():
            self.cmd('kill -9 %s' % line.strip())
            logger.debug('CleanProcess:Darwin:kill logcat')

    def __linux(self, port, device):
        # linux必须最高权限才可获取到端口
        for line in self.cmd(
            "lsof -i:%s |awk '{print $2}'" %
                str(port)).stdout.readlines():
            self.cmd('kill -9 %s' % line.strip())
            logger.debug('CleanProcess:linux:kill appium')
        for line in self.cmd(
            "ps -ef | grep logcat | grep %s|awk '{print $2}'" %
                device).stdout.readlines():
            self.cmd('kill -9 %s' % line.strip())
            logger.debug('CleanProcess:linux:kill logcat')

    def __darwin_all(self, ):
        # for line in self.cmd(
        #         "ps -A | grep logcat|awk '{print $1}'").stdout.readlines():
        #     self.cmd('kill -9 %s' % line.strip())
        #     logger.debug('CleanProcess:Darwin:kill logcat')
        lines_list = []
        lines = self.cmd("ps -A | grep appium|awk '{print $1}'").stdout.readline()
        lines_list.append(lines)
        if len(lines_list) !=0:
            logger.debug('appium 相关进程列表 = %s ' % lines_list)
            for line in lines_list:
                self.cmd('kill -9 %s' % line)
                logger.debug('CleanProcess:Darwin:kill appium')

    def __linux_all(self):
        for line in self.cmd(
                "ps -ef | grep logcat|grep -v grep|awk '{print $2}'").stdout.readlines():
            self.cmd('kill -9 %s' % line.strip())
            logger.debug('CleanProcess:linux:kill logcat')

        for line in self.cmd(
                "ps -ef |grep appium |grep -v grep|awk '{print $2}'").stdout.readlines():
            self.cmd('kill -9 %s' % line.strip())
            logger.debug('CleanProcess:linux:kill appium')

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
        elif platform.system() == 'Linux':
            self.__linux(port, device)
        else:
            logger.debug(
                'CleanProcess:Not identifying your operating system')

    def clean_process_all(self, ):
        """
        清理logcat与appium所有进程
        :return:
        """
        if platform.system() == 'Darwin':
            self.__darwin_all()
        elif platform.system() == 'Linux':
            self.__linux_all()
        else:
            logger.debug(
                'CleanProcess:Not identifying your operating system')


if __name__ == '__main__':
    c = Cp()
    # c.clean_process(4723, 'T7G0215A14000220')
    c.clean_process_all()