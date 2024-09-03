from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get("https://www.baidu.com/")

main_window_handle = wd.current_window_handle

# 创建ActionChains对象，调用对象方法用于实现一些高级操作
ac = ActionChains(wd)

# 调用move_to_element方法实现光标移动到指定元素上，调用perform()执行操作。
ac.move_to_element(wd.find_element(By.CSS_SELECTOR, "[name=tj_briicon]")).perform()

# 点击更多内的百度翻译
wd.find_element(By.CSS_SELECTOR, '[href="http://fanyi.baidu.com/"]').click()

# 切换到百度翻译
for handle in wd.window_handles:
    if "百度翻译" in handle.title():
        break
    wd.switch_to.window(handle)

# 获取翻译输入框元素
trans_input_element = wd.find_element(By.CSS_SELECTOR, "div[role]")

# 点击元素
trans_input_element.click()

# 输入你好翻译
trans_input_element.send_keys("你好")
sleep(3)

# 获取翻译结果
trans_result = wd.find_element(By.CSS_SELECTOR, "span[data-sent-id][spellcheck]")
print(trans_result.text)

# 返回百度网站
wd.switch_to.window(main_window_handle)
print(main_window_handle.title())
# 退出程序
input()

sleep(2)
wd.quit()
