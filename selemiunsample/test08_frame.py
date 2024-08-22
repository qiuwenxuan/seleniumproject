import sys
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import test01 as t


if __name__ == "__main__":
    # 设置 EdgeOptions 并指定浏览器驱动路径

    wd = webdriver.Chrome()
    wd.implicitly_wait(5)

    wd.get("https://cdn2.byhy.net/files/selenium/sample2.html")

    # 切换到frame窗口
    wd.switch_to.frame(wd.find_element(By.CSS_SELECTOR, '[src="sample1.html"]'))
    plant_elements = wd.find_elements(By.CSS_SELECTOR, ".plant")
    for element in plant_elements:
        print(element.text)

    # 切换到窗口外的默认窗口
    wd.switch_to.default_content()
    wd.find_element(By.CSS_SELECTOR, "#outerbutton").click()

    # 退出程序
    sleep(2)
    input()
    wd.quit()
