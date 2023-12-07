# find_element_by_css_selector 的应用：根据 id 定位


from selenium import webdriver  # 导入 webdriver 模块
from time import sleep  # 导入 sleep 模块，可以使程序强制休眠
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # 调用 Chrome 浏览器
driver.maximize_window()  # 窗口最大化
driver.get('https://www.baidu.com/')  # 打开 百度
sleep(2)  # 强制休眠 2 秒
element = driver.find_element(By.CSS_SELECTOR, "#kw")  # 根据 id 定位元素
element.send_keys("自动化测试")  # 输入内容
sleep(3)  # 强制休眠 3 秒
driver.quit()  # 关闭浏览器
