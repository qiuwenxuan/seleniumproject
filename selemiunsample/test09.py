import sys
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import test01 as t


# 设置 EdgeOptions 并指定浏览器驱动路径

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get("https://cdn2.byhy.net/files/selenium/sample3.html")

wd.find_element(By.CSS_SELECTOR, "a").click()

bing_window_handle = None  # bing窗口的handle
main_Window_handle = wd.current_window_handle  # 当前老窗口的handle

# 切换到Bing窗口
for handle in wd.window_handles:  # wd.window_handles输出当前浏览器所有的窗口handle

    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if "Bing" in wd.title:
        bing_window_handle = handle
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break

    # 切换到该窗口
    wd.switch_to.window(handle)

search_element = wd.find_element(By.CSS_SELECTOR, "input#sb_form_q")
search_element.send_keys("菜鸟教程\n")

# 切换为原来的白月黑羽窗口
wd.switch_to.window(main_Window_handle)

# 点击原来窗口的功能按钮
wd.find_element(By.CSS_SELECTOR, "button#outerbutton").click()

add_elements = wd.find_elements(By.CSS_SELECTOR, "#add li")
for element in add_elements:
    if "你点击了外部按钮" in element.text:
        print("按钮被正确点击")


# 退出程序
input()

sleep(2)
wd.quit()
