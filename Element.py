# -*- coding:utf-8 -*-
from driver import driver
from appium.webdriver.mobilecommand import MobileCommand
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
        size = self.get_size()
        width = size.get('width')
        height = size.get('heitht')
        self.driver.swipe(width /2,height *3/4,width /2,height *1/4,1000)

    def swipe_down(self):
        size = self.get_size()
        width = size.get('width')
        height = size.get('heitht')
        self.driver.swipe(width /2,height *1/4,width /2,height *3/4,1000)

    def swipe_right(self):
        size = self.get_size()
        width = size.get('width')
        height = size.get('heitht')
        self.driver.swipe(width *1/4,height /2,width *3/4,height /2,1000)

    def swipe_left(self):
        size = self.get_size()
        width = size.get('width')
        height = size.get('heitht')
        self.driver.swipe(width *3/4, height /2, width * 1/4, height /2, 1000)

    def back(self):
        return self.driver.keyevent(4)

    def swith_h5(self):
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT,{'name':''})

    def swith_app(self):
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {'name': 'NATIVE_APP'})