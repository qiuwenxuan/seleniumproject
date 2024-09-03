from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get("https://cdn2.byhy.net/files/selenium/test4.html")

# 获取windows窗口的大小,get_window_size()返回一个dict字典对象{'width': 1011, 'height': 1086}
windows_size = wd.get_window_size()
print(windows_size)
sleep(1)

# 修改windows窗口的大小
wd.set_window_size(2022, 1086)  # 传入字典的宽x和高y

# 跳转到163网站，并打印网站标题和url
wd.get("https://www.163.com")
print("title:" + wd.title + ",url:" + wd.current_url)  # 网易  https://www.163.com/
sleep(0.5)

# 截屏保存为图片文件
wd.get_screenshot_as_file("1.png")


# 退出程序
input()

sleep(2)
wd.quit()
