# -*- coding: utf-8 -*-
__author__ = 'joko'

"""
@author:joko
@time: 16/11/9 下午6:08
"""
import os
import yaml
from src.lib.AdbUtils import ADB
from conf.Run_conf import read_config
from src.Public.Analyzelog import Anl
from src.Public.GetFilePath import all_file_path


class Gr:

    def __init__(self, all_result_path, device):
        """
        :param all_result_path: 本次测试创建的文件夹
        :param device: 设备id
        """
        self.all_result_path = all_result_path
        self.device = device
        self.adb = ADB(self.device)

    def __confirm_file(self,the_suffix_name):
        return all_file_path(self.all_result_path,the_suffix_name)

    def __yaml_file(self, all_path_result, the_suffix_name):
        """

        :return: 错误报告列表
        """
        return all_file_path(all_path_result, the_suffix_name)


    def __open_yaml(self, file_path):
        """
        获取status yaml文件内的值
        :param file_path: status yaml文件路径
        :return:
        """
        if file_path is None:
            return None
        with open(file_path) as f:
            y = yaml.load(f)
            return y['error_msg']

    def __device_info(self):
        """
        用于生成测试报告的device的信息
        :return: 设备名,磁盘状态,wifi名称
        """

        return 'device_name:' + str(self.adb.get_device_name()), 'disk:' + str(self.adb.get_disk()), \
               'wifi_name:' + str(self.adb.wifi_name()), 'system_version:' + str(self.adb.get_android_version()), \
               'resolution:' + str(self.adb.get_screen_resolution())

    def __app_info(self):
        """
        获取应用包名和版本号
        :return:
        """
        package_name = read_config('appium','appPackage')
        package_name_version = self.adb.specifies_app_version_name(
            package_name)
        return package_name, package_name_version

    def __analyze_log(self):
        """
        过滤log,只留Exception相关日志
        :return:
        """
        a = Anl(self.all_result_path)
        a.main()

    def main(self):
        """
        生成测试报告主函数
        根据status yaml的文件来生成测试报告
        :return:
        """
        import Gethtml
        self.__analyze_log()
        result = self.__yaml_file(self.all_result_path, '.yaml')
        lst = []
        for case_name, confirm_status in result.items():
            case_name = str(case_name).split('.')[0]
            case_result = self.__open_yaml(confirm_status)
            case_img = self.__confirm_file(
                str(confirm_status).replace(
                    'status', 'img').replace(
                    'yaml', 'png'))
            case_per = self.__confirm_file(
                str(confirm_status).replace(
                    'status', 'per').replace(
                    'yaml', 'png'))
            case_log = self.__confirm_file(
                str(confirm_status).replace(
                    'status', 'log').replace(
                    'yaml', 'log'))
            case_filter = self.__confirm_file(
                str(confirm_status).replace(
                    'status', 'log').replace(
                    'yaml', 'log').replace(case_name, case_name + 'filter'))

            lst.append(
                Gethtml.get_html_tr(
                    case_name,
                    case_result,
                    case_img,
                    case_per,
                    case_log,
                    case_filter))
            Gethtml.get_html(
            ''.join(lst),
            self.__app_info(),
            self.__device_info(),
            self.__test_case_execution_status(),
            self.all_result_path)


    def __test_case_execution_status(self):
        """
        获取用例执行状态
        :return: 用例数,通过数,失败数
        """
        number_of_test_cases = self.__yaml_file(
            self.all_result_path, '.yaml').values()
        passed_the_test = 0
        failed = 0
        for i in number_of_test_cases:
            if isinstance(self.__open_yaml(i), bool):
                passed_the_test += 1
            else:
                failed += 1
        return len(number_of_test_cases), passed_the_test, failed


if __name__ == '__main__':
    a = Gr(
        '/Users/joko/Documents/Auto_Analysis/result/2016-11-23_09_53_0263',
        'T7G0215A14000220')
    a.main()
