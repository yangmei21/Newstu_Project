"""
用于巩固css_selector用法
"""

# find_element_by_css_selector 的应用：根据标签（tag）名定位
from selenium import webdriver  # 导入 webdriver 模块
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # 调用 Chrome 浏览器
driver.get('https://www.douban.com/')  # 打开豆瓣
element = driver.find_element(By.CSS_SELECTOR,"a")  # 根据 a 标签定位元素
print(element.text)  # 打印 定位元素 的文本

driver.quit()  # 关闭浏览器
