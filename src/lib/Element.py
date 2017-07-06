# -*- coding:utf-8 -*-
#######################################################
#filename:Element.py
#author:Jeff
#date:2016-09-21
#function:封装操作驱动元素
#######################################################
import os
import sys
import time
from conf.Run_conf import read_config
from appium.webdriver.mobilecommand import MobileCommand
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from appium.webdriver.webelement import WebElement

from src.Public.Common import element_by as eBy
from src.Public.Common import desired_caps as Dc
from src.Public.Common import public as pc
from src.Public.Global import L,S

# reload(sys)
# sys.setdefaultencoding('utf-8')

class Element(object):
    def __init__(self,driver):
        self.driver = driver
        self.runmode = read_config(pc.runmode,pc.driver)

    # 重新封装find_element
    def find_element(self,loc,wait=pc.time2wait):
        '''
        重新封装find_element,查找元素设置了等待时间
        :param loc: 查找元素变量
        :param wait: 等待时间
        :return: 找到元素返回元素对象,否则返回空
        :eg : find_element((By.ID,id_value),10)
        '''
        try:
            if self.runmode == pc.appium:
                WebDriverWait(self.driver, wait).until(lambda driver: driver.find_element(*loc).is_displayed())
                return self.driver.find_element(*loc)
            else:
                WebDriverWait(self.driver, wait).until(lambda driver: driver.element(*loc).is_displayed())
                return self.driver.element(*loc)
        except:
            L.logger.warning('%s 查找超时,未找到元素 : %s' % loc)
            return


    # 重新封装find_elements
    def find_elements(self, loc, wait=pc.time2wait):
        '''
        重新封装find_element,查找元素设置了等待时间
        :param loc: 查找元素变量
        :param wait: 等待时间
        :return: 找到元素返回元素对象列表,否则返回空
        :eg : find_elements((By.ID,id_value),10)
        '''
        try:
            if self.runmode == pc.appium:
                WebDriverWait(self.driver, wait).until(lambda driver: driver.find_elements(*loc))
                return self.driver.find_elements(*loc)
            else:
                WebDriverWait(self.driver, wait).until(lambda driver: driver.elements(*loc))
                return self.driver.elements(*loc)
        except:
            L.logger.warning('%s 查找超时,未找到元素 : %s' % loc)
            return

    def find_element_orign(self,by,value):
        L.logger.info('查找元素: %s, %s' % (by,value))
        if self.runmode == pc.appium:
            return self.driver.find_element(by,value)
        else:
            return self.driver.element(by, value)

    def find_elements_orign(self,loc):
        L.logger.info('查找元素: %s' % loc)
        if self.runmode == pc.appium:
            return self.driver.find_elements(*loc)
        else:
            return self.driver.elements(*loc)

    def element_by(self,by_type,by_value,by_index):
        by_dict={eBy.by_id:lambda :self.by_id(by_value)[by_index],
                 eBy.by_name:lambda :self.by_name(by_value)[by_index],
                 eBy.by_xpath:lambda :self.by_xpath(by_value)[by_index],
                 eBy.by_classname:lambda :self.by_classname(by_value)[by_index]
	    }
        if by_dict.has_key(by_type):
            return by_dict[by_type]()
        else:
            L.logger.warning('暂不支持的方法')

    def by_id(self,id):
        '''
        通过id 进行查找
        :param id: 查找的id值
        :return: 元素对象
        '''
        # element = self.driver.find_element_by_id(id)
        element = self.find_element((By.ID,id))
        L.logger.info('查找id: %s' % id)
        return element


    def by_ids(self, id):
        '''
        通过id 进行查找
        :param id: 查找的id值
        :return: 元素对象列表
        '''
        # elements = self.driver.find_elements_by_id(id)
        elements = self.find_elements((By.ID,id))
        L.logger.info('查找 id: %s' % id)
        return elements


    def by_name(self,name):
        '''by_Id 在1.5.x版本以上取代了by_name,所以请不要再使用by_name'''
        # element = self.driver.find_element_by_name(name)
        element = self.find_element((By.NAME,name))
        L.logger.info('查找 name: %s' % name)
        return element


    def by_names(self, names):
        '''by_Id 在1.5.x版本以上取代了by_name,所以请不要再使用by_name'''
        # elements = self.driver.find_elements_by_name(names)
        elements = self.find_elements((By.NAME,names))
        L.logger.info('查找 names: %s' % names)
        return elements

    def by_xpath(self,xpath):
        '''
        通过xpath查找元素
        :param xpath:
        :return:
        '''
        # element = self.driver.find_element_by_xpath(xpath)
        element = self.find_element((By.XPATH,xpath))
        L.logger.info('查找 xpath: %s' % xpath)
        return element

    def by_xpaths(self,xpath):
        '''
        通过xpath查找元素
        :param xpath:
        :return:
        '''
        # elements = self.driver.find_elements_by_xpath(xpath)
        elements = self.find_elements((By.XPATH,xpath))
        L.logger.info('查找 xpath: %s' % xpath)
        return elements

    def by_classname(self,classname):
        '''
        通过classname 进行元素查找
        :param classname:
        :return:
        '''
        # element = self.driver.find_element_by_class_name(classname)
        element = self.find_element((By.CLASS_NAME,classname))
        L.logger.info('查找 classname: %s' % classname)
        return element

    def by_classnames(self,classname):
        '''
        通过classname 进行元素查找
        :param classname:
        :return:
        '''
        elements = self.find_elements((By.CLASS_NAME,classname))
        L.logger.info('查找 classname: %s' % classname)
        return elements

    def click(self,element_object):
        '''
        点击方法
        :param element_object:
        :return:
        '''
        L.logger.info('click 点击操作')
        element_object.click()

    def quit(self):
        '''
        退出服务
        :return:
        '''
        L.logger.info('driver quit!')
        self.driver.quit()

    def get_current_url(self):
        '''
        get current url
        :return:
        '''
        url = self.driver.current_url
        L.logger.info('获取当前URL: %s' % url)
        return url

    def screenshot_as_base64(self):
        '''
        Gets the screenshot of the current window as a base64 encoded string
           which is useful in embedded images in HTML.
        :Usage:
            driver.screenshot_as_base64()
        :return:
        '''
        L.logger.info('截图保存为base64格式')
        if self.runmode == pc.appium:
            return self.driver.get_screenshot_as_base64()
        else:
            return self.driver.take_screenshot()

    def screenshot_as_file(self,filepath):
        '''
        截屏并保存到指定文件路径
        :param filepath:保存截图的文件路径
        :return:
        '''
        L.logger.info('截屏')
        if self.runmode == pc.appium:
            return self.driver.get_screenshot_as_file(filepath)
        else:
            return self.driver.save_screenshot(filepath)

    def get_size(self):
        '''
        获取当前窗口大小
        :return:
        '''
        el = self.driver.get_window_size()
        L.logger.info('获取当前窗口大小: %s' % el)
        return el


    def swipe_up(self):
        '''swpie 在1.5.x版本以上iOS已经使用偏移量来滑动,
        所以end_x,end_y是相对于start_x,start_y偏移的值;
        但是Android仍采用起始坐标到终点坐标进行滑动
        这里是向上滑动'''
        try:
            size = self.get_size()
            width = size.get('width')
            height = size.get('height')
            if self.runmode == pc.appium:
                if str(S.device[Dc.platformName]).lower() == 'ios':
                    L.logger.info('向上滑动,起始滑动坐标: (%s,%s),坐标偏移量(%s,%s)' % (width / 2, height * 3/4, 0, height * (-1)/4))
                    self.driver.swipe(width / 2, height * 3/4, 0, (-1)/4*height, 200)
                else:
                    L.logger.info('向上滑动,起始滑动坐标: (%s,%s),终点坐标(%s,%s)' % (width / 2, height * 3 / 4, width / 2,  height * 1 /4))
                    self.driver.swipe(width * 4/ 8, height * 7 / 8, width * 4/ 8, height * 1 / 8, 200)
            else:
                # args = {'fromX': width / 2, 'fromY': height * 7/ 10, 'toX': width * 1 / 2,
                #         'toY': height * 3 / 10, 'duration': 0.5}
                args = {'fromX': width * 1 / 2, 'fromY': height * 9 / 10, 'toX': width * 1 / 2, 'toY': height * 1 / 10,
                 'duration':0.02}
                L.logger.info(
                    '向上滑动,起始滑动坐标: (%s,%s),终点坐标(%s,%s)' % (width / 2, height * 9 / 10, width / 2, height * 1 / 10))
                self.driver.touch('drag', args)
            # time.sleep(1)
        except:
            raise


    def swipe_down(self):
        '''swpie 在1.5.x版本以上iOS已经使用偏移量来滑动,
        所以end_x,end_y是相对于start_x,start_y偏移的值;
        但是Android仍采用起始坐标到终点坐标进行滑动
        这里是向下滑动'''
        try:
            size = self.get_size()
            width = size.get('width')
            height = size.get('height')
            if self.runmode == pc.appium:
                if str(S.device[Dc.platformName]).lower() == 'ios':
                    L.logger.info('向下滑动,起始滑动坐标: (%s,%s),坐标偏移量(%s,%s)' % (width / 2, height * 1/4, 0, height * 3/4))
                    self.driver.swipe(width / 2, height * 1/4, 0, (-3)/4 * height , 200)
                else:

                    L.logger.info('向下滑动,起始滑动坐标: (%s,%s),终点坐标(%s,%s)' % (width / 2, height * 1 / 4, width / 2, height * 3 / 4))

                    self.driver.swipe(width / 2, height * 1 / 4, width /2, 3 / 4 * height, 200)
            else:
                args = {'fromX': width / 2, 'fromY': height * 1 / 4, 'toX': width * 1 / 2,
                        'toY': height * 3 / 4, 'duration': 0.05}
                L.logger.info(
                    '向下滑动,起始滑动坐标: (%s,%s),终点坐标(%s,%s)' % (width / 2, height * 1 / 4, width / 2, height * 3 / 4))
                self.driver.touch('drag', args)
            time.sleep(1)
        except:
            raise


    def swipe_right(self):
        '''swpie 在1.5.x版本以上iOS已经使用偏移量来滑动,
        所以end_x,end_y是相对于start_x,start_y偏移的值;
        但是Android仍采用起始坐标到终点坐标进行滑动
        这里是向右滑动'''
        try:
            size = self.get_size()
            width = size.get('width')
            height = size.get('height')
            if self.runmode == pc.appium:
                if str(S.device[Dc.platformName]).lower() == 'ios':
                    L.logger.info('向右滑动,起始滑动坐标: (%s,%s),坐标偏移量(%s,%s)' % (width * 1 / 10, height * 9 / 10, width * 3 / 5,0))
                    self.driver.swipe(width * 1/10, height * 9/10, width * 3/5, 0,1000)
                else:
                    L.logger.info('向右滑动,起始滑动坐标: (%s,%s),终点坐标(%s,%s)' % (width / 10, height * 9 / 10, width * 6/ 10, height * 9 / 10))
                    self.driver.swipe(width / 10, height * 9 / 10, width * 6/ 10, height * 9 / 10, 1000)
            else:
                args = {'fromX': width / 10, 'fromY': height * 9 / 10, 'toX': width * 8 / 10,
                        'toY': height * 9 / 10, 'duration': 0.05}
                L.logger.info('向右滑动,起始滑动坐标: (%s,%s),终点坐标(%s,%s)' % (width / 10, height * 9 / 10, width * 8 / 10, height * 9 / 10))
                self.driver.touch('drag',args)
            time.sleep(1)

        except:
            raise


    def swipe_left(self):
        '''
        swpie 在1.5.x版本以上iOS已经使用偏移量来滑动,
        所以end_x,end_y是相对于start_x,start_y偏移的值;
        但是Android仍采用起始坐标到终点坐标进行滑动
        这里是向左滑动
        '''
        try:
            size = self.get_size()
            width = size.get('width')
            height = size.get('height')
            if self.runmode == pc.appium:
                if str(S.device[Dc.platformName]).lower() == 'ios':
                    L.logger.info('向左滑动,起始滑动坐标: (%s,%s),坐标偏移量(%s,%s)' % (width * 9 / 10, height * 9 / 10, width * (-3) / 5,0))
                    self.driver.swipe(width * 9 / 10, height * 9 / 10, width * (-3) / 5,0,1000)
                else:
                    L.logger.info('向左滑动,起始滑动坐标: (%s,%s),终点坐标(%s,%s)' % (width * 7 / 10, height * 9 / 10, width / 10, height * 9 / 10))
                    self.driver.swipe(width * 7 / 10, height * 9 / 10, width / 10, height * 9 / 10, 1000)
            else:
                args = {'fromX': width *7/ 10, 'fromY': height * 9 / 10, 'toX': width * 1 / 10,
                        'toY': height * 9 / 10, 'duration': 0.05}
                L.logger.info(
                    '向左滑动,起始滑动坐标: (%s,%s),终点坐标(%s,%s)' % (width * 7 / 10, height * 9 / 10, width / 10, height * 9 / 10))
                self.driver.touch('drag', args)
            time.sleep(1)

        except:
            raise
    def swipe_all(self, t):
        """
        选择如何滑动屏幕
        """
        if t == 'swipe_left':
            self.swipe_left()
        elif t == 'swipe_right':
            self.swipe_right()
        elif t == 'swipe_up':
            self.swipe_up()
        elif t == 'swipe_down':
            self.swipe_down()

    def send_key_event(self, arg):
        """
        参考文献：http://blog.csdn.net/jlminghui/article/details/39268419
        操作实体按键
        :return:
        """
        event_list = {'entity_home': 3, 'entity_back': 4, 'entity_menu': 82, 'entity_volume_up': 24,
                      'entity_volume_down': 25, "entity_enter": 66}
        if arg in event_list:
            self.driver.keyevent(int(event_list[arg]))

    def tap(self,position,duration =None):
        '''
        Usage:
            driver.tap([(100, 20), (100, 60), (100, 100)], 500)
        '''
        try:
            self.driver.tap(position, duration)
            L.logger.info('点按tap')
        except:
            raise

    def back(self):
        L.logger.info('Android设备点按back键')
        return self.driver.keyevent(4)

    def swith_h5(self):
        try:
            L.logger.info('切换到h5')
            self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT,{'name':'com.pingan.rympush'})
        except:
            L.logger.error('切换到h5异常')

    def swith_app(self):
        try:
            L.logger.info('切换到NATIVE_APP')
            self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {'name': 'NATIVE_APP'})
        except:
            L.logger.error('切换到app异常')

    def implicitly_wait(self,second):
        L.logger.info('隐式等待 %s 秒' % second)
        if self.runmode == pc.appium:
            return self.driver.implicitly_wait(second)
        else:
            return self.driver.set_implicitly_wait(second)

    def page_source(self):
        L.logger.info('获取 page_source')
        if self.runmode == pc.appium:
            return self.driver.page_source
        else:
            return self.driver.source

    def load_page_timeout(self,second):
        L.logger.info('页面加载等待,超时时间 %s 秒' % second)
        return self.driver.set_page_load_timeout(second)

    def context(self):
        context = self.driver.context()
        L.logger.info('获取当前上下文 context: %s' % context)
        return context

    def contexts(self):
        contexts = self.driver.contexts()
        L.logger.info('获取当前上下文 contexts %s ' % contexts)
        return contexts

    def current_context(self):
        current_context = self.driver.current_context()
        L.logger.info('获取当前页面上下文 current_context : %s' % current_context)
        return current_context


    def device_time(self):
        device_time = self.driver.device_time()
        L.logger.info('获取设备时间 device_time : %s ' % device_time)
        return device_time

    def close_app(self):
        L.logger.info('关闭App')
        if self.runmode == pc.appium:
            return self.driver.close_app()
        else:
            return self.driver.close()

    def send_keys(self,element,text):
        L.logger.info('发送内容:%s' % text)
        element.clear()
        return element.send_keys(text)


    def keyevent(self,keycode):
        L.logger.info('键盘事件,输入keycode:%s' % keycode)
        '''收起键盘,sendKeyEvent(4)
        for Android
        附录 keycode

        电话键

        KEYCODE_CALL 拨号键 5
        KEYCODE_ENDCALL 挂机键 6
        KEYCODE_HOME 按键Home 3
        KEYCODE_MENU 菜单键 82
        KEYCODE_BACK 返回键 4
        KEYCODE_SEARCH 搜索键 84
        KEYCODE_CAMERA 拍照键 27
        KEYCODE_FOCUS 拍照对焦键 80
        KEYCODE_POWER 电源键 26
        KEYCODE_NOTIFICATION 通知键 83
        KEYCODE_MUTE 话筒静音键 91
        KEYCODE_VOLUME_MUTE 扬声器静音键 164
        KEYCODE_VOLUME_UP 音量增加键 24
        KEYCODE_VOLUME_DOWN 音量减小键 25

        控制键

        KEYCODE_ENTER 回车键 66
        KEYCODE_ESCAPE ESC键 111
        KEYCODE_DPAD_CENTER 导航键 确定键 23
        KEYCODE_DPAD_UP 导航键 向上 19
        KEYCODE_DPAD_DOWN 导航键 向下 20
        KEYCODE_DPAD_LEFT 导航键 向左 21
        KEYCODE_DPAD_RIGHT 导航键 向右 22
        KEYCODE_MOVE_HOME 光标移动到开始键 122
        KEYCODE_MOVE_END 光标移动到末尾键 123
        KEYCODE_PAGE_UP 向上翻页键 92
        KEYCODE_PAGE_DOWN 向下翻页键 93
        KEYCODE_DEL 退格键 67
        KEYCODE_FORWARD_DEL 删除键 112
        KEYCODE_INSERT 插入键 124
        KEYCODE_TAB Tab键 61
        KEYCODE_NUM_LOCK 小键盘锁 143
        KEYCODE_CAPS_LOCK 大写锁定键 115
        KEYCODE_BREAK Break/Pause键 121
        KEYCODE_SCROLL_LOCK 滚动锁定键 116
        KEYCODE_ZOOM_IN 放大键 168
        KEYCODE_ZOOM_OUT 缩小键 169

        组合键

        KEYCODE_ALT_LEFT Alt+Left
        KEYCODE_ALT_RIGHT Alt+Right
        KEYCODE_CTRL_LEFT Control+Left
        KEYCODE_CTRL_RIGHT Control+Right
        KEYCODE_SHIFT_LEFT Shift+Left
        KEYCODE_SHIFT_RIGHT Shift+Right

        基本

        KEYCODE_0 按键'0' 7
        KEYCODE_1 按键'1' 8
        KEYCODE_2 按键'2' 9
        KEYCODE_3 按键'3' 10
        KEYCODE_4 按键'4' 11
        KEYCODE_5 按键'5' 12
        KEYCODE_6 按键'6' 13
        KEYCODE_7 按键'7' 14
        KEYCODE_8 按键'8' 15
        KEYCODE_9 按键'9' 16
        KEYCODE_A 按键'A' 29
        KEYCODE_B 按键'B' 30
        KEYCODE_C 按键'C' 31
        KEYCODE_D 按键'D' 32
        KEYCODE_E 按键'E' 33
        KEYCODE_F 按键'F' 34
        KEYCODE_G 按键'G' 35
        KEYCODE_H 按键'H' 36
        KEYCODE_I 按键'I' 37
        KEYCODE_J 按键'J' 38
        KEYCODE_K 按键'K' 39
        KEYCODE_L 按键'L' 40
        KEYCODE_M 按键'M' 41
        KEYCODE_N 按键'N' 42
        KEYCODE_O 按键'O' 43
        KEYCODE_P 按键'P' 44
        KEYCODE_Q 按键'Q' 45
        KEYCODE_R 按键'R' 46
        KEYCODE_S 按键'S' 47
        KEYCODE_T 按键'T' 48
        KEYCODE_U 按键'U' 49
        KEYCODE_V 按键'V' 50
        KEYCODE_W 按键'W' 51
        KEYCODE_X 按键'X' 52
        KEYCODE_Y 按键'Y' 53
        KEYCODE_Z 按键'Z' 54'''
        return self.driver.keyevent(keycode)

    def hide_keyboard_andr(self,key_name=None,key=None,strategy=None):
        ''' for Android'''
        L.logger.info('隐藏键盘')
        return self.driver.hide_keyboard(key_name,key,strategy)

    def hide_keyboard_iOS(self):
        '''for ios'''
        size = self.driver.get_window_size()
        width = size.get('width')
        height = size.get('height')
        L.logger.info('隐藏键盘')
        self.driver.tap([(width / 2, height / 2)])

    def find_toast_element(self,toast,timeout=10,poll_frequency=0.5):
        '''查询toast'''
        toast = '//*[@text={}]'.format(toast)
        element = WebDriverWait(self.driver,timeout,poll_frequency).until(self.find_element((By.XPATH,toast),pc.time2wait))
        return element

