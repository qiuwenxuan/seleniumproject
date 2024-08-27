import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


wd = webdriver.Chrome()
wd.implicitly_wait(10)

wd.get("https://tinypng.com/")

# 查找上传输入框并点击
upload_input = wd.find_element(
    By.CSS_SELECTOR, ".bg-gradient  #upload-dropbox-zone input"
)
upload_input.click()

# 发送键盘交互给当前页面，键盘传入图片路径并回车
import win32com.client

sleep(2)
shell = win32com.client.Dispatch("WScript.Shell")
shell.Sendkeys(r"C:\workspace\1.png" + "\n")

# 压缩结束，点击下载按钮
wd.find_element(By.CSS_SELECTOR, ".button-wrapper span").click()

# 退出程序
input()

sleep(2)
wd.quit()
