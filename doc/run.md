## 框架介绍
### UI自动化框架:AnyDoor_UI

### 工具要求
* appium: 1.6.0 以上
* WebDriverAgent：latest

### 框架支持用例

- [x] 支持python语言脚本用例

- [x] 支持excel编写的测试用例

### 框架支持单元测试框架

- [x] unittest

- [x] pytest

### 框架支持失败重跑

- [x] 失败重跑次数设置

- [x] 失败重跑开关控制

### 框架支持多机并行执行
- [x] 支持IOS和Android并行

- [x] 支持IOS和IOS并行

- [x] 支持Android和Android并行

### 输出

- [x] 输出测试日志

- [x] 输出html测试报告

* 脚本用例可支持unittest、pytest生成的html报告
* excel用例报告为自定义

- [x] 截图

## AnyDoor_UI配置文档

#### 安装node

[官网地址](https://nodejs.org/en/download/)

* OS:brew install node
* windows,linux参照官网

#### 安装appium

* 1: npm install -g cnpm --registry=https://registry.npm.taobao.org

* 2: cnpm install -g appium --no-cache

### python

* 版本:2.7.11

* 安装:方法请自行查找

* 编译器:推荐PyCharm

* 使用模块:xlrd,xlwt,Appium-Python-Client,selenium,xlutils,PyH,ConfigParser,Pytest,Pytest-html,Pytest-rerunfailures  

* 模块安装:运行setup.py会自行安装

### 运行
#### 命令窗口进入到项目:Anydoor_UI根目录
* python Run.py

### 参数配置

* 参见:parameter_configuration文档

### 用例编写

* 参见test_case_writing文档

### 测试报告

* 参见test_report文档

### 其他

* appium:appium_wiki文档

* 控件查找:controls_operations文档