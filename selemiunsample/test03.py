from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

import test01 as t

if __name__ == "__main__":
    # 打开谷歌浏览器，指定浏览器驱动，返回一个 WebDriver类型 的对象用于操作元素
    wd = webdriver.Chrome()

    # 打开指定浏览器网址
    wd.get("https://cdn2.byhy.net/files/selenium/sample1.html")

    # 调用wd对象方法返回整个web页面范围内的指定的element元素
    web_elements = wd.find_elements(By.TAG_NAME, "span")
    for element in web_elements:
        print(element.text)  # 打印整个web界面下的tag="span"标签的所有属性

    t.print_debug()
    web_element = wd.find_element(By.ID, "container")
    # 调用单个element元素的方法返回该元素范围内的指定element元素
    tag_elements = web_element.find_elements(By.TAG_NAME, "span")
    for element in tag_elements:
        print(
            element.text
        )  # 打印id="container"范围内的所有tag="span"标签的所有元素的text文本属性
    sleep(3)
    wd.quit()
