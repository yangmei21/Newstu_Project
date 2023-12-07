"""测试用例
测试对象：yx后台环境 http://202.111.177.155:8081/manager/static/ng-ant-admin/index.html#/login/login-form
"""

import unittest
import time
from parameterized import parameterized  # 引入parameterized模块
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase):
    """
    1.打开浏览器：就使用setUp(self)方法打开浏览器
    2.查找用户名输入框
    3.查找密码的输入框
    4.点击登录
    5.断言登录成功与否 使登录后的页面上的用户名进行断言
    """

    # 创建登录数据，这里可以写多个账号进行测试  组织测试数据 格式[( ), ( ), ( )],一个元组就是一组测试数据
    # data=[
    #     ('账号','密码'),
    #     ('账号', '密码'),
    #     ('账号', '密码'),
    # ]

    data = [
        ('admin', '123456'),
    ]

    wrong_data = [
        ('1dmin', '122356'),
    ]

    def setUp(self) -> None:
        # 创建一个浏览器对象
        self.driver = webdriver.Chrome("E:/Python3.9/chromedriver.exe")
        # 发送请求
        self.driver.get("http://202.111.177.155:8081/manager/static/ng-ant-admin/index.html#/login/login-form")
        self.driver.maximize_window()
        time.sleep(3)

    def tearDown(self) -> None:
        # 关闭浏览器
        self.driver.close()
        # 退出浏览器
        self.driver.quit()

    @parameterized.expand(data)  # 参数化，在测试方法上方使用装饰器 @parameterized.expand(测试数据)
    def test_login(self, username, password):
        # 查找输入账号的文本框，并输入账号
        '''验证是否可以正确登录'''
        time.sleep(2)
        username_input = self.driver.find_elements(By.CSS_SELECTOR, 'input[formcontrolname="userName"]')
        username_input[0].send_keys(username)  # 输入账号

        # 查找输入密码的文本框，并输入密码
        time.sleep(2)
        password_input = self.driver.find_elements(By.CSS_SELECTOR, 'input[formcontrolname="password"]')
        password_input[0].send_keys(password)  # 输入密码

        time.sleep(3)

        login_button = self.driver.find_element(By.CSS_SELECTOR, 'button.ant-btn-primary')
        login_button.click()

        time.sleep(2)

        self.assertEqual(self.driver.title, "工作台")



