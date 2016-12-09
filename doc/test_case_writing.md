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
| Action_Keyword | 解释     | 所有字段                                     | 配合字段                                     | 辅助配合字段    |
| -----------    | ----    | ---------------------------------------- | ---------------------------------------- | --------- |
| click          | 点击     | click                                    | test_control_type，test_control           | /         |
| send_keys      | 发送文本 | send_keys                                | test_control_type，test_control，test_text | /         |
| swipe          | 滑动     | swipe_left,swipe_right,swipe_up,swipe_down | /                                        | /         |
| assert         | 断言     | assert                                   | test_control_type，test_control，test_text | test_wait |
| entity         | 实体按键 | entity_home，entity_back，entity_menu，entity_volume_up，entity_volume_down | /                                        | /         |

## 完整用例范例,用例名:login

```yaml
---
-
  test_name: 点击跳过
  test_id: 0001
  test_control_type: id
  test_action: click
  test_control: test.joko.com.myapplication:id/button1
-
  test_name: 输入帐号名
  test_id: 0002
  test_control_type: id
  test_action: send_keys
  test_control: test.joko.com.myapplication:id/editText
  test_text: 199999999
-
  test_name: 输入密码
  test_id: 0003
  test_control_type: id
  test_action: send_keys
  test_control: test.joko.com.myapplication:id/editText2
  test_text: 9999

-
  test_name: 点击登录
  test_id: 0004
  test_control_type: xpath
  test_action: click
  test_control: //android.widget.Button[contains(@text,'确定')]

-
  test_name: 向上滑动页面
  test_id: 0005
  test_action: swipe_up
  test_range: 3

-
  test_name: 向下滑动页面
  test_id: 0005
  test_action: swipe_down
  test_range: 3

```