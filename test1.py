# -*- coding:utf-8 -*-
from macaca import WebDriver,WebElement
from selenium.webdriver.common.by import By
from src.Public.Common import public as pc
from selenium.webdriver.support.ui import WebDriverWait

desired_caps = {
    'autoAcceptAlerts' : True,
    'platformName':'iOS',
    'deviceName':'iPhone 6s',
    'platformVersion': '10.2',
    'reuse':3,
    'bundleId':'rym.pingan.rympush',
    # 'udid':'ae679a86542a57c31e57a1d66351c87570c9bac7'
}
driver = WebDriver(desired_caps)

driver.init()



def switch_to_webview(driver):
    contexts = driver.contexts
    driver.context = contexts[-1]
    return driver

def switch_to_native(driver):
    contexts = driver.contexts
    driver.context = contexts[0]
    return driver

def find_element(loc, wait=pc.time2wait):

    try:
        # if self.runmod == pc.appium:
        WebDriverWait(driver, wait).until(lambda driver: driver.element(*loc).is_displayed())
        return driver.element(*loc)
    except:
        print '%s 查找超时,未找到元素 : %s' % loc
        return

size = driver.get_window_size()
driver.take_screenshot()
width = size.get('width')
height = size.get('height')
print 'width: %s, height: %s' % (width,height)
left ={'fromX':width *9/10,'fromY':height * 9 /10,'toX':width *1/10,'toY':height * 9 /10,'duration':2}
up ={'fromX':width *1/2,'fromY':height * 9 /10,'toX':width *1/2,'toY':height * 1 /10,'duration':0.05}
# touch('drag',{'fromX':200, 'fromY':400, 'toX':200, 'toY':100, 'duration':2})
# driver.touch('drag',left)
# driver.swipe(width *9/10,height * 9 /10,width *1/10,height * 9 /10,2000)

while not find_element((By.ID,'PA01100000000_02_RYG')):
    driver.touch('drag', left)
else:
    find_element((By.ID,'PA01100000000_02_RYG')).click()
    print '点击: PA01100000000_02_RYG'

print 'base64: ',driver.take_screenshot()

# ele = driver.wait_for_element(By.ID,'加油站2')
# print 'wait_for_element :',ele
print driver.contexts

while not find_element((By.ID,'个人中心')):
    driver.touch('drag',up)
else:
    print '找到插件: 个人中心'
# print driver.context
# switch_to_webview(driver)
# print driver.context
print 'close h5'
try:
    find_element((By.XPATH,'//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]')).click()
except:
    # driver.close()
    find_element((By.ID,'closeButton')).click()
finally:
    find_element((By.XPATH,'//*[@name="closeButton"]')).click()

# driver.close()
# print 'close'

driver.quit()
print 'quit'


# driver.element(By.ID,'PA01100000000_02_PAZB').click()
# try:
#     driver.element(By.XPATH, "//*[@name='com nav ic back']").click()
# except:
#     driver.element(By.XPATH,
#                    '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeButton[1]').click()


driver.quit()

