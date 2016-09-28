# -*- coding:utf-8 -*-
#######################################################
#filename:Element.py
#author:Jeff
#date:2016-09-21
#function:封装操作驱动元素
#######################################################
from appium.webdriver.mobilecommand import MobileCommand
from Public.logger import *
from Global import *
from driver import appdriver

class Element():
    def __init__(self):
        # getdriver = appdriver()
        # self.driver = getdriver.get_driver()
        global driver
        self.driver = driver



    def by_id(self,id):
        '''by_Id 在1.5.x版本以上取代了by_name'''
        element = self.driver.find_element_by_id(id)
        logger.debug('查找id: %s' % id)
        return element


    def by_ids(self, id):
        '''by_Id 在1.5.x版本以上取代了by_name'''
        elements = self.driver.find_elements_by_id(id)
        return elements


    def by_name(self,name):
        '''by_Id 在1.5.x版本以上取代了by_name'''
        element = self.driver.find_element_by_name(name)
        return element


    def by_names(self, names):
        '''by_Id 在1.5.x版本以上取代了by_name'''
        elements = self.driver.find_elements_by_name(names)
        return elements

    def by_xpath(self,xpath):
        element = self.driver.find_element_by_xpath(xpath)
        return element

    def by_xpaths(self,xpath):
        elements = self.driver.find_elements_by_xpath(xpath)
        return elements

    def by_classname(self,classname):
        element = self.driver.find_element_by_name(classname)
        return element

    def quit(self):
        return self.driver.quit()

    def get_size(self):
        return self.driver.get_window_size()


    def swipe_up(self):
        '''swpie 在1.5.x版本以上已经使用偏移量来滑动,
        所以end_x,end_y是相对于start_x,start_y偏移的值,
        这里是向上滑动'''
        try:
            size = self.get_size()
            width = size.get('width')
            height = size.get('height')
            self.driver.swipe(width / 2, height * 3/4, 0, height * (-2)/4, 1000)
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
            self.driver.swipe(width / 2, height * 1/4, 0, height * 2/4, 1000)
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
            self.driver.swipe(width * 2 / 10, height * 8 / 10, width * 3 / 5, 0,1000)
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
            self.driver.swipe(width * 8 / 10, height * 8 / 10, width * (-4) / 10, 0, 1000)
        except:
            raise

    def tap(self,position,duration =None):
        '''
        Usage:
            driver.tap([(100, 20), (100, 60), (100, 100)], 500)
        '''
        try:
            self.driver.tap(position, duration)
        except:
            raise

    def back(self):
        return self.driver.keyevent(4)

    def swith_h5(self):
        try:
            self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT,{'name':''})
        except:
            raise

    def swith_app(self):
        try:
            self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {'name': 'NATIVE_APP'})
        except:
            raise

    def implicitly_wait(self,second):
        return self.driver.implicitly_wait(second)

    def page_source(self):
        return self.driver.page_source

    def load_page_timeout(self,second):
        return self.driver.set_page_load_timeout(second)

    def content(self):
        return self.driver.context

    def contents(self):
        return self.driver.contexts

    def current_content(self):
        return self.driver.current_context


    def device_time(self):
        return self.driver.device_time

    def send_keys(self,element,text):
        return element.send_keys(text)


    def keyevent(self,keycode):
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

    def hide_keyboard(self,key=None,key_name=None,strategy=None):
        ''' for Android'''
        return self.driver.hide_keyboard(key,key_name,strategy)

if __name__ == '__main__':
    try:
        wd = Element()
        wd.swipe_right()
        wd.by_id('个人中心').click()
        wd.by_xpath("//*[@value='一账通号/手机号/身份证号/邮箱']").click()
        wd.by_xpath("//*[@value='一账通号/手机号/身份证号/邮箱']").clear()
        wd.by_xpath("//*[@value='一账通号/手机号/身份证号/邮箱']").send_keys('18589091413')
        wd.by_xpath("//*[@value='密码']").click()
        wd.by_xpath("//*[@value='密码']").clear()
        wd.by_xpath("//*[@value='密码']").send_keys('Solution123')
        wd.by_id('完成').click()
        wd.by_xpath("//UIALink[@name='登 录']").click()
        wd.implicitly_wait(10)
        wd.swipe_left()
    except Exception:
        raise
    finally:
        wd.quit()
    # wd.swipe_left()
    # wd.swipe_up()
    # wd.swipe_down()

    # print '当前上下文: ', wd.current_content()
    # wd.by_id('PA01100000000_02_PAZB').click()
    # wd.implicitly_wait(5)
    # wd.by_id('Home ZoomLevel cut').click()
    # wd.implicitly_wait(5)
    # page = wd.page_source()
    # print 'page = ',page
    # if 'mapSelected' in page:
    #     print 'success'
    #     assert True
    # print '当前上下文: ', wd.contents()
    # wd.implicitly_wait(5)
    # wd.by_id('关闭').click()


