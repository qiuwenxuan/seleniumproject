import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


wd = webdriver.Chrome()
wd.implicitly_wait(10)

wd.get("https://tinypng.com/")

# 查找上传输入框
upload_input = wd.find_element(
    By.CSS_SELECTOR, ".bg-gradient  #upload-dropbox-zone input"
)

# send_keys上传图片
upload_input.send_keys(r"C:\workspace\1.png")

# 压缩结束，点击下载按钮
wd.find_element(By.CSS_SELECTOR, ".button-wrapper span").click()

# 退出程序
input()

sleep(2)
wd.quit()
