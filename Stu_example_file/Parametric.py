"""
通过Parameterized实现参数化
参考：https://www.jianshu.com/p/f44dcd1a0d8d
"""

import unittest
from time import sleep
from selenium import webdriver
from parameterized import parameterized

class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.base_url="https://www.baidu.com"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def baidu_search(self,search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(2)


    #通过Parameterized实现参数化
    @parameterized.expand([
        ("case1","selenium"),
        ("case2","unittest"),
        ("case3","parameterized"),
    ])
    def test_search(self,name,search_key):
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")

if __name__=='__main__':
    unittest.main(verbosity=2)