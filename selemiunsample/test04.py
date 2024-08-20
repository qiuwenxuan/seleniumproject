import sys
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import test01 as t


def wait_for_element_decorator(wait_time=10):
    """
    装饰器，增强查找函数，给函数添加一个超时机制，用于在找不到元素时自动等待。
    :param wait_time: 最大等待时间（秒）。
    :return: 返回增强后的函数。
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time()
            while True:
                try:
                    # 调用原始的 find_element 函数
                    element = func(*args, **kwargs)
                    return element
                except NoSuchElementException:
                    if time() - start_time > wait_time:
                        raise TimeoutError(f"等待时间超过 {wait_time} 秒，未能找到元素")
                    sleep(0.5)
                    sys.stderr.write(f"等待{time() - start_time}秒\n")

        return wrapper

    return decorator


if __name__ == "__main__":
    # 打开谷歌浏览器，指定浏览器驱动，返回一个 WebDriver类型 的全局页面对象用于操作元素
    wd = webdriver.Chrome()

    # 打开指定浏览器网址
    wd.get("https://www.byhy.net/_files/stock1.html")

    # 查找查询文本框，输入“通信”
    kw_element = wd.find_element(By.ID, "kw")
    kw_element.send_keys("通信\n")

    # 点击查询按钮
    go_element = wd.find_element(By.ID, "go")
    go_element.click()

    # 方法1：使用装饰器增强 find_element 函数
    find_element_with_wait = wait_for_element_decorator(10)(wd.find_element)

    # 打印查询到的第一个内容的文本
    element = find_element_with_wait(By.CLASS_NAME, "result-item")
    print(element.text)

    # 方法2：我们也可以直接写一个简单的while循环判断
    while True:
        try:
            element = wd.find_element(By.TAG_NAME, "result-item")
            print(element.text)
            break
        except NoSuchElementException as e:
            sleep(1)

    # 方法3：WebElement对象设置隐式等待时间（10s内）
    wd.implicitly_wait(10)
    print(element.text)

    # 方法4：设置定时任务
    start_time = time()
    while True:
        try:
            if time() - start_time > 10:
                raise TimeoutError(f"查找元素超时{time() - start_time}秒")
            element = wd.find_element(By.TAG_NAME, "result-item")
        except NoSuchElementException as e:
            sleep(1)
        else:
            print(element.text)
            break

    # 退出程序
    sleep(2)
    wd.quit()
