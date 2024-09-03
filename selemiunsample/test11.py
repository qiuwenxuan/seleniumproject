from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get("https://cdn2.byhy.net/files/selenium/test4.html")

# alert弹窗
# 1.点击b1按钮
wd.find_element(By.CSS_SELECTOR, "#b1").click()

# 2.打印弹窗输出
print(wd.switch_to.alert.text)
sleep(2)

# 3.点击alert弹窗的ok按钮，关闭弹窗
wd.switch_to.alert.accept()
sleep(2)

# confirm弹窗
# 1.点击b2
wd.find_element(By.CSS_SELECTOR, "#b2").click()

# 2.打印弹窗输出
print(wd.switch_to.alert.text)
sleep(2)

# 3.可以对弹窗操作accept和dismiss
# wd.switch_to.alert.dismiss() 取消
wd.switch_to.alert.accept()  # 接受
sleep(2)

# Prompt弹窗
# 1.点击b3
wd.find_element(By.CSS_SELECTOR, "#b3").click()

# 2.给弹窗输入框输入文字
wd.switch_to.alert.send_keys("hello world!")

# 3.打印弹窗输出
print(wd.switch_to.alert.text)
sleep(2)

# 4.可以对弹窗操作accept和dismiss
# wd.switch_to.alert.dismiss() 取消
wd.switch_to.alert.accept()  # 接受
sleep(2)


# 退出程序
input()

sleep(2)
wd.quit()
