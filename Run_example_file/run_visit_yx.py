import unittest
from BeautifulReport import BeautifulReport
import time
"""
使用run文件执行unittest文件是，可以直接导入
这时unittest会自动查找导入文件中类去执行
但是文件的开头以test文件的类和函数也必须以test开头
"""

if __name__ == '__main__':
    """
    defaultTestLoader
    使用unittest.defaultTestLoader()类。
    这个类的作用就是调用这个类的discover（）方法，搜索指定目录下指定开头的.py，
    并将搜索到的测试用例组装成一个测试集合
    """

    # 先确定一个要搜索的路径
    test_dir = './'
    # 创建集合对象
    dis = unittest.defaultTestLoader.discover(test_dir, pattern='visit_yx.py')
    runner = BeautifulReport(dis)
    runner.report(
        description="yx登录",
        filename="yx_login01"
    )
