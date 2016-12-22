## 执行的参数配置


* 配置 conf/Run_conf.ini

```ini

#monitor.ini
###############################################
[appium]
ip = 127.0.0.1
port = 4723
deviceName = iPhone 5s
bundleId = com.pingan.rympush
platformName = iOS
platformVersion = 10.1
autoAcceptAlerts = True
noReset = True
automationName = XCUITest
unicodeKeyboard = True
resetKeyboard = True
autoWebview = True
app = /usr/local/anydoor/app_package/PAAnydoorSDK_New.ipa

###############################################
[logger]
log_file = /Users/zengyuanchen/Documents/SVN/ShareFromCloud/share/Project/Anydoor_UI/output/log/AnyDoor_UI.log
logger_name = root
# DEBUG:10 INFO:20 WARN:30 ERROR:40 CRITICAL:50
log_level_in_console = 20
log_level_in_logfile = 10
level = 20
format = |(asctime)s : |(filename)s[line:|(lineno)d] [ |(levelname)s ] |(message)s
datefmt = %Y-%m-%d %H:%M:%S
filemode = a
#handles 模式 0:日志名不滚动,日志每次重写 ; 1:日志根据大小滚动, 每次接着写; 2:日志根据时间滚动, 每次接着写
handles_mode = 0
#rw_mode:日志读写模式
rw_mode = wb
#console_log_on  = 1 开启控制台日志，logfile_log_on = 1 开启文件日志
console_log_on = 1
logfile_log_on = 1
#10485760 = 10M
max_bytes_each = 10485760
backup_count = 0
###############################################
[command]
start_appium = appium -a 127.0.0.1 -p 4723 -bp 4733

###############################################
[plugin]
plugin_url_iOS = https://maam.pingan.com.cn/maam/getPluginList.do?sdkVersion=3.6.0.32&osVersion=7.1.2&deviceId=2abb53d0f829972ba905cca44662d89f1fd4fcda&appId=PA01100000000_01_SDK&appVersion=1.0&deviceType=ios
###############################################
[login]
login_username =18602753065
login_password =qweqwe123

###############################################
[testcase]
xls_case_path = /Users/zengyuanchen/Documents/SVN/ShareFromCloud/share/Project/Anydoor_UI/TestCase/Excel/TestCase.xlsx
project_path = /Users/zengyuanchen/Documents/SVN/ShareFromCloud/share/Project/Anydoor_UI

###############################################
[screenshot]
screen_shot_isTrue = False
screen_shot_path = /Users/zengyuanchen/Documents/SVN/ShareFromCloud/share/Project/Anydoor_UI/output/screen/{}.png

###############################################
[retry]
#失败重跑次数
retry_num = 1
#失败重跑开关
retry_isTrue = True
###############################################
[runmode]
# mode
# 0 --- script
# 1 --- excel
mode = 0

###############################################


```
注:windows路径也如此相同写法:d:/file/1.x


