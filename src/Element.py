# -*- coding:utf-8 -*-
#######################################################
#filename:Element.py
#author:Jeff
#date:2016-09-21
#function:封装操作驱动元素
#######################################################
from appium.webdriver.mobilecommand import MobileCommand
from driver import driver

class Element():
    def __init__(self):
        at = driver()
        self.driver = at.get_driver()

    def by_id(self,id):
        element = self.driver.find_element_by_id(id)
        return element

    def by_ids(self, id):
        elements = self.driver.find_elements_by_id(id)
        return elements

    def by_name(self,name):
        element = self.driver.find_element_by_name(name)
        return element

    def by_names(self, names):
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
        try:
            size = self.get_size()
            width = size.get('width')
            height = size.get('heitht')
            self.driver.swipe(width /2,height *3/4,width /2,height *1/4,1000)
        except:
            raise

    def swipe_down(self):
        try:
            size = self.get_size()
            width = size.get('width')
            height = size.get('heitht')
            self.driver.swipe(width /2,height *1/4,width /2,height *3/4,1000)
        except:
            raise

    def swipe_right(self):
        try:
            size = self.get_size()
            width = size.get('width')
            height = size.get('heitht')
            self.driver.swipe(width * 2/10,height * 8/10,width * 8/10,height * 8/10,1000)
        except:
            raise

    def swipe_left(self):
        try:
            size = self.get_size()
            width = size.get('width')
            height = size.get('heitht')
            self.driver.swipe(width * 8 / 10, height * 8 / 10, width * 2 / 10, height * 8 / 10, 1000)
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

    def implicitly_wait(self,time_to_wait):
        return self.driver.implicitly_wait(time_to_wait)

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
