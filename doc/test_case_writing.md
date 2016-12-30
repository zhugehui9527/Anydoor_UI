## 测试用例编写规范

* 1: 参考TestCase目录下的测试用例
    Excel目录  :存放excel测试用例
    Scripts目录:存放python脚本测试用例
    
* 2: 用例名不可重复,会影响用例的继承

## 测试用例字段解释
* 以Excel用例为例:

| 字段               | 解释                 | 演示        |  是否必须   |
| ----------------- | -------------------- | ---------  | ---------  | 
| CaseSuite         | 用例名                | login      |     是      | 
| CaseID            | 步骤id                | 1          |     是      | 
| Description       | 用例描述信息           | 登录       |     否      |  
| Action_Keyword    | 操作api               | click      |     是      | 
| ios or android    | iOS或Android 独有操作  |            |     否      | 
| Element           | 元素封装               | 登录       |     是      |  
| PageObject        | 页面元素               |           |     否      | 
| Parameter         | 入参                  |            |     否      | 

* api解释(api主要封装在ReadApi)

| Action_Keyword          | 解释              |  配合字段                     | 辅助配合字段      |
| ----------------------- | ------------------| --------------------------- | --------------- |
| click                   | 点击              |  Element                     | ios |  android  |
| send_keys               | 发送文本           |  Element，Parameter          | ios |  android  |
| sleep                   | 等待               |  Parameter                  | ios |  android  |
| assertTrue              | 断言真             |  PageObject，Parameter       | ios |  android  |
| assertFalse             | 断言假             |  PageObject，Parameter       |     ios         |
| assertTrueCheckPlugin   | 断言插件为真        |  PageObject，Parameter       | ios |  android  |
| swipe2left              | 左滑动             |   /                          | ios |  android  |
| swipe2right             | 右滑动             |   /                          | ios |  android  |
| hidekeyboard            | 隐藏键盘           |   Parameter                  | ios |  android  |
| waitFortext             | 智能等待           |   Element，Parameter          |     ios         |
| checkPlugin             | 检查插件           |   Element，Parameter          |     ios         |
| closeH5                 | 关闭H5             |   /                          |     ios         |
| closeH5ByPluginId       | 通过插件ID关闭H5    |   Element                    | ios |  android  |
| getScreenShot           | 截图               |   /                          |       /         |
| getPluginList           | 获取插件列表        |   /                          |       /         |

## 完整测试用例范例

|CaseSuite（案例） |CaseID(步骤id)|Description（步骤描述）|	Action_Keyword(操作)	 |ios or android(ios或android独有操作)|Element（元素封装）	 |PageObject(页面元素)|Parameter（传入参数）
| --------------- | ------------| ---------------------|---------------------|-----------------------------------|-------------------|-------------------|--------------------------|
| 登录_1000	      |    1	    | 滑动打开个人中心        |公共库				 |                  /                |          /        |         /         |SwipeToClickPersonalCenter|
| 登录_1001	      |    2	    | H5页面登录	            |公共库				 |                  /                |          /        |         /         |loginyztByH5              |

## 完整公共案例库用例范例

|CaseSuite（案例） |CaseID(步骤id)|Description（步骤描述）|	Action_Keyword(操作)	 |ios or android(ios或android独有操作)|Element（元素封装）	 |PageObject(页面元素)|Parameter（传入参数）
| --------------- | ------------| ---------------------|---------------------|-----------------------------------|-------------------|-------------------|--------------------------|
| ClickMsgCenter  |    1	    | 向右滑动              |swipe2right			 |                  /                |          /        |         /         |         /                |
|        /	      |    2	    | 等待文本显示（消息中心） |waitFortext		     |                  /                |     消息中心       |         /         |         30               |
|        /	      |    3	    | 点击消息中心           |click   		     |                  /                |     消息中心       |         /         |         /                |
|        /	      |    4	    | 延迟等待              |sleep		         |                  /                |       /           |         /         |         5                |
