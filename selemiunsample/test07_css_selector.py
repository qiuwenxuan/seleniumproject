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

    # 通过css选择器选择具有限制的元素定位（id为container元素的后代元素id为inner21的直接标签为span的元素）
    elements = wd.find_elements(By.CSS_SELECTOR, "#container #inner21 > span")
    for element in elements:
        print("css selector:" + element.get_attribute("outerHTML"))

    # 根据css选择器查找对应属性值的元素，
    # elements = wd.find_elements(By.CSS_SELECTOR, "[href]")
    # 我们也可以写详细一点的属性对应值，如href="http://www.miitbeian.gov.cn
    elements = wd.find_elements(By.CSS_SELECTOR, '[href="http://www.miitbeian.gov.cn"]')
    for element in elements:
        print("attribute:" + element.get_attribute("outerHTML"))

    # 退出程序
    sleep(2)
    wd.quit()
