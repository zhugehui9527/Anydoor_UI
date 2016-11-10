# -*- coding:utf-8 -*-
#######################################################
#filename:Element.py
#author:Jeff
#date:2016-09-21
#function:封装操作驱动元素
#######################################################
from appium.webdriver.mobilecommand import MobileCommand
from selenium.webdriver.support.ui import WebDriverWait
from Global import *
from Public.Log import *
import time
import sys
sys.path.append('.')
reload(sys)
sys.setdefaultencoding('utf-8')

class Element(object):
    def __init__(self):
        pass

    def find_element(self,value):
        '''find element'''
        try:
            WebDriverWait(driver,20).until(lambda: driver.find_element_by_id(value))
            return True
        except:
            logger.warning('未找到元素: %s' % value)
            return False


    def by_id(self,id):
        '''by_Id 在1.5.x版本以上取代了by_name'''
        element = driver.find_element_by_id(id)
        logger.debug('查找id: %s' % id)
        return element


    def by_ids(self, id):
        '''by_Id 在1.5.x版本以上取代了by_name'''
        elements = driver.find_elements_by_id(id)
        logger.debug('查找 id: %s' % id)
        return elements


    def by_name(self,name):
        '''by_Id 在1.5.x版本以上取代了by_name'''
        element = driver.find_element_by_name(name)
        logger.debug('查找 name: %s' % name)
        return element


    def by_names(self, names):
        '''by_Id 在1.5.x版本以上取代了by_name'''
        elements = driver.find_elements_by_name(names)
        logger.debug('查找 names: %s' % names)
        return elements

    def by_xpath(self,xpath):
        '''
        通过xpath查找元素
        :param xpath:
        :return:
        '''
        element = driver.find_element_by_xpath(xpath)
        logger.debug('查找 xpath: %s' % xpath)
        return element

    def by_xpaths(self,xpath):
        elements = driver.find_elements_by_xpath(xpath)
        logger.debug('查找 xpath: %s' % xpath)
        return elements

    def by_classname(self,classname):
        element = driver.find_element_by_class_name(classname)
        logger.debug('查找 classname: %s' % classname)
        return element

    def by_classnames(self,classname):
        elements = driver.find_element_by_class_name(classname)
        logger.debug('查找 classname: %s' % classname)
        return elements

    def click(self,id):

        element = driver.find_element_by_id(id)
        element.click()

    def quit(self):
        logger.debug('driver quit!')
        return driver.quit()

    def get_current_url(self):
        '''
        get current url
        :return:
        '''
        url = driver.current_url()
        logger.debug('获取当前URL: %s' % url)
        return url
    def screenshot_as_base64(self):
        '''
        Gets the screenshot of the current window as a base64 encoded string
           which is useful in embedded images in HTML.
        :Usage:
            driver.screenshot_as_base64()
        :return:
        '''
        logger.debug('截图保存为base64格式')
        return driver.get_screenshot_as_base64()

    def screenshot_as_file(self,filepath):
        '''
        截屏并保存到指定文件路径
        :param filepath:
        :return:
        '''
        logger.debug('截屏')
        return driver.get_screenshot_as_file(filepath)

    def get_size(self):
        logger.debug('获取当前窗口大小')
        return driver.get_window_size()


    def swipe_up(self):
        '''swpie 在1.5.x版本以上已经使用偏移量来滑动,
        所以end_x,end_y是相对于start_x,start_y偏移的值,
        这里是向上滑动'''
        try:
            size = self.get_size()
            width = size.get('width')
            height = size.get('height')
            logger.debug('向上滑动,起始滑动坐标: (%s,%s),坐标偏移量(%s,%s)' % (width / 2, height * 3/4, 0, height * (-2)/4))
            driver.swipe(width / 2, height * 3/4, 0, height * (-2)/4, 1000)
        except:
            raise


    def swipe_down(self):
        '''swpie 在1.5.x版本以上已经使用偏移量来滑动,
        所以end_x,end_y是相对于start_x,start_y偏移的值,
        这里是向下滑动'''
        try:
            size = self.get_size()
            width = size.get('width')
            height = size.get('height')
            logger.debug('向下滑动,起始滑动坐标: (%s,%s),坐标偏移量(%s,%s)' % (width / 2, height * 1/4, 0, height * 2/4))
            driver.swipe(width / 2, height * 1/4, 0, height * 2/4, 1000)
        except:
            raise


    def swipe_right(self):
        '''swpie 在1.5.x版本以上已经使用偏移量来滑动,
        所以end_x,end_y是相对于start_x,start_y偏移的值,
        这里是向右滑动'''
        try:
            size = self.get_size()
            width = size.get('width')
            height = size.get('height')
            logger.debug('向右滑动,起始滑动坐标: (%s,%s),坐标偏移量(%s,%s)' % (width * 2 / 10, height * 8 / 10, width * 3 / 5,0))
            driver.swipe(width * 2 / 10, height * 8 / 10, width * 3 / 5, 0,1000)
        except:
            raise


    def swipe_left(self):
        '''swpie 在1.5.x版本以上已经使用偏移量来滑动,
        所以end_x,end_y是相对于start_x,start_y偏移的值,
        这里是向左滑动'''
        try:
            size = self.get_size()
            width = size.get('width')
            height = size.get('height')
            logger.debug('向左滑动,滑动起始坐标: (%s,%s),偏移量(%s,%s)' % (width * 8 / 10, height * 8 / 10, width * (-4) / 10,0))
            driver.swipe(width * 8 / 10, height * 8 / 10, width * (-4) / 10, 0, 1000)
        except:
            raise

    def tap(self,position,duration =None):
        '''
        Usage:
            driver.tap([(100, 20), (100, 60), (100, 100)], 500)
        '''
        try:
            driver.tap(position, duration)
            logger.debug('点按tap')
        except:
            raise

    def back(self):
        logger.debug('Android设备点按back键')
        return driver.keyevent(4)

    def swith_h5(self):
        try:
            logger.debug('切换到h5')
            driver.execute(MobileCommand.SWITCH_TO_CONTEXT,{'name':''})
        except:
            logger.error('切换到h5异常')

    def swith_app(self):
        try:
            logger.debug('切换到NATIVE_APP')
            driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {'name': 'NATIVE_APP'})
        except:
            logger.error('切换到app异常')

    def implicitly_wait(self,second):
        logger.debug('隐式等待 %s 秒' % second)
        return driver.implicitly_wait(second)

    def page_source(self):
        logger.debug('获取 page_source')
        return driver.page_source

    def load_page_timeout(self,second):
        logger.debug('页面加载等待,超时时间 %s 秒' % second)
        return driver.set_page_load_timeout(second)

    def context(self):
        logger.debug('获取当前上下文:context')
        return driver.context

    def contexts(self):
        logger.debug('获取当前上下文:contexts')
        return driver.contexts

    def current_content(self):
        logger.debug('获取当前页面上下文:current_content')
        return driver.current_content


    def device_time(self):
        logger.debug('获取设备时间:device_time')
        return driver.device_time

    def send_keys(self,element,text):
        logger.debug('元素:%s,发送内容:%s' % (element,text))
        return element.send_keys(text)


    def keyevent(self,keycode):
        logger.debug('键盘事件,输入keycode:%s' % keycode)
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
        return driver.keyevent(keycode)

    def hide_keyboard(self,key=None,key_name=None,strategy=None):
        ''' for Android'''
        logger.debug('隐藏键盘')
        return driver.hide_keyboard(key,key_name,strategy)


if __name__ == '__main__':
    screenshot_path = os.path.abspath('../output/screenshot')+'_'+str(time.time())+'.png'
    try:
        wd = Element()
        # wd.swipe_right()
        # wd.implicitly_wait(10)
        # wd.by_id('个人中心').click()
        # wd.implicitly_wait(15)
        # wd.by_xpath("//*[@value='一账通号/手机号/身份证号/邮箱']").click()
        # wd.implicitly_wait(1)
        # wd.by_xpath("//*[@value='一账通号/手机号/身份证号/邮箱']").clear()
        # wd.implicitly_wait(1)
        # wd.by_xpath("//*[@value='一账通号/手机号/身份证号/邮箱']").send_keys('18589091413')
        # wd.implicitly_wait(10)
        # wd.by_xpath("//*[@value='密码']").click()
        # wd.by_xpath("//*[@value='密码']").clear()
        # wd.by_xpath("//*[@value='密码']").send_keys('Solution123')
        # wd.by_id('完成').click()
        # wd.by_xpath("//UIALink[@name='登 录']").click()
        # wd.implicitly_wait(60)
        # wd.swipe_left()
        print 'screenshot_as_base64 : ',wd.screenshot_as_base64()
        wd.screen_shot_as_file(screenshot_path)
    except Exception:
        raise
    else:
        wd.quit()

