import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


import sys


# 用于debug调试输出
def print_debug(debug: str = "") -> None:
    sys.stdout.write(
        f"========================================\\{debug}\\========================================\n"
    )


# 用于error报错输出
def print_error(error: str = "") -> None:
    sys.stderr.write(
        f"========================================\\{error}\\========================================\n"
    )


if __name__ == "__main__":
    # 打开谷歌浏览器，指定浏览器驱动，返回一个 WebDriver类型 的对象用于操作元素
    #   wd = webdriver.Chrome(service=Service(r"C:\browersDriver\chromedriver.exe"))
    #   我们也可以将浏览器所在文件夹路径放在环境变量PATH当中，就可以无需申明浏览器驱动路劲
    wd = webdriver.Chrome()

    # 打开指定浏览器网址
    wd.get("https://www.byhy.net/_files/stock1.html")

    # 调用find_element方法返回ID="kw"元素的 WebElemen类型 的对象对象
    element = wd.find_element(By.ID, "kw")

    # 调用元素对象的send_keys方法，操作对象输入字符串“通信”进行查询
    element.send_keys("通信\n")

    # 查找id=“go”的元素并获取WebElement对象，查找“查询”按钮
    element = wd.find_element(By.ID, "go")

    # 对WebElement对象进行点击操作，点击查询按钮
    element.click()
    print_error("查找含“通信”的元素")

    # 退出浏览器驱动
    sleep(3)
    wd.quit()
