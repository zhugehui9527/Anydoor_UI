# -*- coding:utf-8 -*-

import os
import sys
from src.Public.Global import L,S,D

sys.path.append("../../")
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class RunApp(object):
    def __init__(self, device_l,index=0):
        """
        self.time:用于建立存放文件的目录
        """
        # self.time = time.strftime(
        #     "%Y-%m-%d_%H_%M_%S",
        #     time.localtime(
        #         time.time()))
        self.index = index
        self.device_l = device_l
        self.device = self.device_l['udid']
        L.logger.info('start test device:%s' % self.device)
        self.all_result_path = self.mkdir_file()
        self.driver = D.driver

    def mkdir_file(self):
        """
        :return:创建日志存放文件夹
        """

        result_file = S.device_dir

        # result_file_every = result_file + '/' + \
        #                     time.strftime("%Y-%m-%d_%H_%M_%S{}".format(random.randint(10, 99)),
        #                                   time.localtime(time.time()))
        file_list = [
            result_file,
            result_file + '/log',
            result_file + '/per',
            result_file + '/img',
            result_file + '/status']

        if not os.path.exists(result_file):
            os.mkdir(result_file)

        for file_path in file_list:
            if not os.path.exists(os.path.abspath(file_path)):
                os.mkdir(file_path)
        return result_file


    def analysis(self, yaml_name, yaml_path):
        """
        继承driver开始测试
        :param path_yaml: 测试用例地址
        :return:
        """
        import RunYaml
        s = RunYaml.start_case(
            D.driver,
            yaml_name,
            yaml_path,
            self.all_result_path,
            self.device,
            self.index
        )
        return s.main()

    def case_start(self):
        """
        控制diver开启 and 关闭,且清理进程
        执行步骤:
            1:安装应用
            2:开启driver,并且执行测试
            3:关闭driver
            4:清理logcat appium 进程
        :return:
        """
        from src.Public.GetFilePath import all_file_path
        yaml_paths = PATH('../../TestCase/Yaml')
        test_case_yaml = all_file_path(yaml_paths,'.yaml').items()
        L.logger.debug('test_case_yaml : %s' % test_case_yaml)
        if not test_case_yaml:
            L.logger.error('not yaml found ')
        else:
            for yaml_name, yaml_path in test_case_yaml:
                L.logger.debug('yaml path:{}'.format(yaml_path))
                self.analysis(yaml_name, yaml_path)
                # try:
                #     self.driver.quit()
                #     L.logger.debug('driver quit')
                # except Exception as e:
                #     L.logger.warn('driver quit Error %s' % e)
