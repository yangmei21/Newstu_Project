# 导包
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# 获取driver对象
driver = webdriver.Chrome()
# 打开URL
url = "http://202.111.177.155:8081/manager/static/ng-ant-admin/index.html#/login/login-form"
driver.get(url)

# 最大化浏览器
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(20)

# 输入用户名
username_input = driver.find_elements(By.CSS_SELECTOR, 'input[formcontrolname="userName"]')
username_input[0].send_keys("admin")
# 输入密码
password_input = driver.find_elements(By.CSS_SELECTOR, 'input[formcontrolname="password"]')
password_input[0].send_keys("123456")

# 点击登录
login_button = driver.find_element(By.CSS_SELECTOR, 'button.ant-btn-primary')
login_button.click()

sleep(10)
# 获取正确title信息
msg = driver.title
# 断言
print("title", msg)
assert msg == "工作台"

driver.quit()
