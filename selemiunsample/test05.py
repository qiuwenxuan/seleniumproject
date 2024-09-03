import sys
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import test01 as t


if __name__ == "__main__":
    # 打开谷歌浏览器，指定浏览器驱动，返回一个 WebDriver类型 的对象用于操作元素
    #   wd = webdriver.Chrome(service=Service(r"C:\browersDriver\chromedriver.exe"))
    #   我们也可以将浏览器所在文件夹路径放在环境变量PATH当中，就可以无需申明浏览器驱动路径
    wd = webdriver.Chrome()
    # 设置最大等待时间
    wd.implicitly_wait(10)

    # 打开指定浏览器网址
    wd.get("https://www.byhy.net/_files/stock1.html")

    # 1. 在输入框查询"通信"字样并获取输入框内的值
    kw_element = wd.find_element(By.ID, "kw")

    kw_element.send_keys("通信\n")
    # 获取输入框内的文本（采用text不会打印输入框内的文本，需要涛哥value属性获取）
    value = kw_element.get_attribute("value")
    print(value)

    elements = wd.find_elements(By.CLASS_NAME, "result-item")
    for element in elements[:5]:  # 输出5条搜索结果
        # 输出test文本的几种方案：text、innerTest、testContent
        print("text:" + element.text)
        print("innertext:" + element.get_attribute("innerText"))
        print("textContent:" + element.get_attribute("textContent"))

    # 获取id为suggestion的元素
    sg_element = wd.find_element(By.ID, "suggestion")

    # 2. 获取id为suggestion的元素的placeholder属性值，返回字符串属性值
    placeholder = sg_element.get_attribute("placeholder")
    print(type(placeholder))  # <class 'str'>
    print(placeholder)  # “一句话建议”

    # 3. get_attribute("outerHTML") 用于获取符合条件的整个前端html源码
    element = wd.find_element(By.ID, "1")
    print(element.get_attribute("outerHTML"))
    # <div class="result-item" id="1">
    #       <p class="name">包钢股份</p>
    #       <p>代码：<span>600010</span></p>
    #     </div>

    # 4. get_attribute("innerHTML") 用于获取符合条件的内部的html源码
    element = wd.find_element(By.ID, "1")
    print(element.get_attribute("innerHTML"))
    #   <p class="name">包钢股份</p>
    #   <p>代码：<span>600010</span></p>

    # 退出程序
    sleep(2)
    wd.quit()
