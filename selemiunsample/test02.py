from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

import test01 as t

if __name__ == "__main__":
    # 打开谷歌浏览器，指定浏览器驱动，返回一个 WebDriver类型 的对象用于操作元素
    wd = webdriver.Chrome()

    # 打开指定浏览器网址
    wd.get("https://cdn2.byhy.net/files/selenium/sample1.html")

    element = wd.find_element(By.CLASS_NAME, "plant")  # 返回列表的第一个元素

    # 调用find_element方法返回ID="kw"元素的 WebElemen类型 的对象列表
    elements = wd.find_elements(By.CLASS_NAME, "plant")
    for element in elements:
        # test01.print_debug(element)
        print(
            element.text
        )  # 打印WebElement的text属性，及就是元素在网页上文本的显示：土豆、养成、白菜

    t.print_debug()

    elements = wd.find_elements(By.TAG_NAME, "span")
    for element in elements:
        print(element.text)  # 打印WebElement的text文本属性，及在网页上显示的文本内容

    sleep(3)
    wd.quit()
