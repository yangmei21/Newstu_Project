# 导包
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
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
password_input[0].send_keys("12341256")

# 点击登录
login_button = driver.find_element(By.CSS_SELECTOR, 'button.ant-btn-primary')
login_button.click()

try:
    # 设置等待时间为10秒
    wait = WebDriverWait(driver, 10)

    # 等待直到元素可见
    element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.ng-tns-c69-14.ng-star-inserted[style]')))

    # 获取弹框文本内容
    element_content = element.text
    print("弹框内容:", element_content)

except Exception as e:
    print("未找到弹框或超时:", e)

# 关闭浏览器
driver.quit()


