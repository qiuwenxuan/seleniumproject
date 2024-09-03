import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


wd = webdriver.Edge()
wd.implicitly_wait(10)

wd.get("https://cdn2.byhy.net/files/selenium/test1.html")

elements = wd.find_elements(By.XPATH, "//p[@style]/..//p[@id]")
for element in elements:
    print(element.text)

# 退出程序
input()

sleep(2)
wd.quit()
