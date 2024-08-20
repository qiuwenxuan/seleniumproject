import sys
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import test01 as t


if __name__ == "__main__":
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)

    wd.get("https://cdn2.byhy.net/files/selenium/sample1.html")

    # 1. 通过css元素选择器选择.animal的所有元素（css选择器以.开头）
    animal_elements = wd.find_elements(By.CSS_SELECTOR, ".animal")
    # wd.find_elements(By.CLASS_NAME, "animal")功能与find_elements(By.CSS_SELECTOR, ".animal")完全一致
    for element in animal_elements:
        print(element.get_attribute("innerHTML"))

    # 2. css元素选择器也可以根据id名查找元素(以#开头)
    search_elements = wd.find_elements(
        By.CSS_SELECTOR, "#searchtext"
    )  # 查找页面当中id为searchtext的元素
    for element in animal_elements:
        print(element.get_attribute("innerHTML"))

    # 退出程序
    sleep(2)
    wd.quit()
