# -*- coding:utf-8 -*-
import traceback
import time
import sys
import yaml
from src.Public.Global import L,S
from src.lib.Element import Element
from src.Public.Performance import data_marker
from src.Public.GetLog import Al
from src.Public.GenReport import Gr
from src.lib.Utils import SQL
from src.Public.GetFilePath import all_file_path
from src.lib.AdbUtils import ADB
reload(sys)
sys.setdefaultencoding("utf-8")

def e():
    """
    捕获用例执行函数异常安装
    :return: True|AssertionError|AttributeError
    """

    def E(func):
        def wrapper(*args, **kwargs):
            error_msg = True
            try:
                return func(*args, **kwargs)
            except AssertionError as e:
                L.logger.warn(traceback.format_exc())
                L.logger.error(e)
                error_msg = 'Assertion error'
            except AttributeError as e:
                L.logger.warn(traceback.format_exc())
                L.logger.error(e)
                error_msg = 'Attribute Error'
            except Exception as e:
                error_msg = traceback.format_exc()
                L.logger.error(e)
            finally:
                return error_msg

        return wrapper

    return E


class BB(Element):
    """
    继承测试信息
    """
    pass
class start_case():
    def __init__(self, driver, yaml_name, yaml_path, all_result_path, device,index):
        self.path_yaml = yaml_path
        self.filename = str(yaml_name).split('.')[0]
        self.dash_page = BB(driver)
        self.device = device
        self.all_result_path = all_result_path
        self.index = int(index)
        self.adb = ADB(device)

    def __save_screen_file(self):
        """
        截图:
        1:首先调用appium自带方法,如果失败会调用minicap,
        2:minicap失败会调用adb 截图
        :return: 存储的图片地址
        """
        screen_file = self.all_result_path + '/img/{}.png'.format(self.filename)
        L.logger.debug('截图路径: %s' % screen_file)
        try:
            self.dash_page.screenshot_as_file(screen_file)
        except Exception as e:
            L.logger.warn('截图保存失败,错误信息: %s' % e)

        return screen_file

    def __save_cpu_mem(self, cpu, mem, h_cpu, h_mem):
        """

        :param cpu: cpu值列表
        :param mem: 内存值列表
        :return: 返回性能生成图片
        """
        per_img_file = self.all_result_path + \
                       '/per/{}.png'.format(self.filename)

        data_marker(cpu, mem, h_cpu, h_mem, per_img_file)
        return per_img_file

    def __save_error_status(self):
        """
        测试用例的的状态
        :return: 错误日志路径
        """
        error_file = self.all_result_path + \
                     '/status/{}.yaml'.format(self.filename)
        return error_file

    def __save_android_log(self):
        """

        :return:清理当前设备缓存log,并且记录当前设备log
        """
        android_log = Al(self.device)
        log_file = self.all_result_path + '/log/{}.log'.format(self.filename)


        android_log.main(log_file)
        return log_file

    def __save_android_result(self):
        """
        生成测试报告
        :return: 测试报告路径
        """
        r = Gr(self.all_result_path, self.device)
        r.main()
        return self.all_result_path

    def __select_per(self, case_name, device_name, ):
        sql = SQL()
        return sql.select_per(case_name, device_name, )

    def __save_sql(self, case_name, device_name, cpu_list, mem_list, execution_status):
        sql = SQL()

        sql.insert_per(case_name, device_name, cpu_list, mem_list, execution_status)
        sql.close()

    def get_all_case(self, path_yaml):
        """

        :param path_yaml: 用例地址
        :return: 返回yaml内字典,且遍历继承的信息,支持多重继承
        """

        def get_case(path_yaml):
            case_list = []

            inherit_case_file = all_file_path(self.all_result_path,'.yaml')
            with open(path_yaml) as f:
                for dic in yaml.load(f):
                    if isinstance(dic, dict):
                        if 'test_inherit' in dic:
                            inherit_case_name = dic['test_inherit']
                            inherit_case = inherit_case_name + '.yaml'
                            if inherit_case in inherit_case_file.keys():
                                case_list += case_list + get_case(inherit_case_file[inherit_case])

                        else:
                            case_list.append(dic)
                    else:
                        L.logger.warn('get_case:not dic')
            return case_list

        return get_case(path_yaml)

    # @e()
    def __analysis_yaml(self, path_yaml):
        """
        测试用例解释器
        :param path_yaml: 测试用例地址
        1:每执行一条用例会记录下当前的性能
        :return:
        """
        from conf.Run_conf import read_config
        package_name = read_config('appium','appPackage')
        looptimes = int(read_config('yaml','looptimes'))
        turn_on = bool(read_config('performance','turn_on'))
        cpu_list = []
        mem_list = []
        for x in range(looptimes):
            for dic in self.get_all_case(path_yaml):
                L.logger.debug(str(dic))
                if isinstance(dic, dict):
                    if 'test_name' in dic:
                        test_name = str(dic['test_name']).decode('utf-8')
                        L.logger.info(
                            'Start the test_case: {}'.format(
                                test_name))

                    range_num = 1
                    if 'test_range' in dic:
                        # 循环控制
                        # todo:打印循环相关的日志
                        range_num = dic['test_range']

                    for i in xrange(0, range_num):
                        if dic['test_action'] == 'click':
                            # 点击
                            test_control = dic['test_control']
                            test_control_type = dic['test_control_type']

                            L.logger.debug('click {}'.format(test_control))
                            click_ele = self.dash_page.find_element((test_control_type, test_control))
                            self.dash_page.click(click_ele)

                        elif dic['test_action'] == 'send_keys':
                            # 发送文本
                            test_control_type = dic['test_control_type']
                            test_control = dic['test_control']
                            # test_text = dic['test_text']
                            send_keys_ele = self.dash_page.find_element((test_control_type, test_control))
                            if dic.has_key('test_text'):
                                test_text = dic['test_text']
                                L.logger.debug('send {} to {}'.format(test_text, test_control))
                                self.dash_page.send_keys(send_keys_ele, str(test_text))

                            elif dic.has_key('test_texts'):
                                test_texts = dic['test_texts']
                                L.logger.debug('send {} to {}'.format(test_texts[self.index], test_control))
                                # L.logger.debug('test_texts : %s,type: %s' % (test_texts,type(test_texts)))
                                self.dash_page.send_keys(send_keys_ele, test_texts[int(self.index)])

                        elif 'swipe' in dic['test_action']:
                            # 滑动
                            test_action = dic['test_action']
                            L.logger.debug('{}'.format(test_action))
                            self.dash_page.swipe_all(test_action)

                        elif 'entity' in dic['test_action']:
                            # 实体按键
                            test_action = dic['test_action']
                            L.logger.debug('{}'.format(test_action))
                            self.dash_page.send_key_event(test_action)

                        elif dic['test_action'] == 'element_text':
                            test_wait = 15
                            test_control = dic['test_control']
                            test_control_type = dic['test_control_type']
                            el = self.dash_page.find_element((test_control_type, test_control), wait=test_wait)
                            L.logger.info('find text: {}'.format(el.text))

                        elif dic['test_action'] == 'assert':
                            # 断言
                            test_wait = 15
                            test_control = dic['test_control']
                            test_control_type = dic['test_control_type']
                            test_text = dic['test_text']
                            if dic.has_key('test_wait'):
                                test_wait = int(dic['test_wait'])

                            L.logger.debug('assert {}'.format(test_control))

                            el = self.dash_page.find_element((test_control_type, test_control), wait=test_wait)
                            assert el.text == test_text

                        if 'test_sleep' in dic:
                            # 等待
                            sleep = dic['test_sleep']
                            L.logger.debug('Wait {} seconds'.format(sleep))
                            time.sleep(int(sleep))

                        if turn_on:
                            # 增加性能的开关判断
                            L.logger.debug('Obtaining app performance data')
                            cpu = self.adb.get_cpu(package_name)
                            mem = self.adb.get_mem(package_name)
                            L.logger.debug('cpu:{}'.format(cpu))
                            L.logger.debug('mem:{}'.format(mem))
                            cpu_list.append(cpu)
                            mem_list.append(mem)

                else:
                    L.logger.error(
                        'Yaml file format error, the current {}, you need dict'.format(
                            type(dic)))

        L.logger.debug("sql 存储")
        historical_per = self.__select_per(self.filename, self.device, )
        self.__save_sql(self.filename, self.device, cpu_list, mem_list, 1)
        if historical_per is not None:
            h_cpu = historical_per[0]
            h_mem = historical_per[1]
            self.__save_cpu_mem(cpu_list, mem_list, h_cpu, h_mem)
        else:
            self.__save_cpu_mem(cpu_list, mem_list, None, None)

        L.logger.debug('cpu_list:{}'.format(cpu_list))
        L.logger.debug('mem_list:{}'.format(mem_list))
        return True

    def __load_analysis(self):
        """
        执行测试
        执行步骤:
            1:开启记录log
            2:执行测试
            3:记录执行结果
            4:存储执行结果
            5:截图
        :return: 截图路径
        """
        L.logger.debug('read the yaml file')
        self.__save_android_log()
        error_msg = self.__analysis_yaml(self.path_yaml)
        with open(self.__save_error_status(), 'wb') as f:
            yaml.dump({'error_msg': error_msg}, f)
            L.logger.debug(str('results of the:%s' % error_msg))
            f.close()

        return self.__save_screen_file()

    def main(self):
        """
        执行步骤:
            1:开启测试
            2:生成测试报告
        :return:
        """
        time.sleep(5)
        self.__load_analysis()
        time.sleep(1)

        self.__save_android_result()

