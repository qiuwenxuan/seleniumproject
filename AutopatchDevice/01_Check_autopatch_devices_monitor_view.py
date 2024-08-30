from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from TestTools import logging_format


# 设置Chrome选项
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")  # 启用隐私模式

# 初始化Chrome浏览器驱动，以隐私模式打开，并设置最大等待时间
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(30)

# 打开PPE环境网址
driver.get("https://aka.ms/mmdmemppe")
driver.set_window_size(2022, 1086)  # 设置页面窗口的大小

# 登录界面输入框,输入用户名密码
driver.find_element(By.XPATH, "//input[@type='email']").send_keys(
    "admin@MMDPPESHLiweiTest.onmicrosoft.com\n"
)
driver.find_element(By.XPATH, "//input[@name='passwd']").send_keys("Jj[tzT{33>fl^)K\n")

# 保持登录状态弹窗确认
if (
    "保持登录状态"
    == driver.find_element(By.XPATH, '//div[@class="row text-title"]').text
):
    driver.find_element(By.XPATH, "//input[@id='KmsiCheckboxField']").click()
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

# 登录到device->windows update->monitor->autopatch device
elements = driver.find_elements(By.XPATH, "//div[@class='fxs-sidebar-label']")
for element in elements:
    if "Device" == element:
        element.click()

driver.find_element(By.XPATH, "(//div[@class='fxc-menu-listView-item'])[20]").click()
driver.find_element(By.XPATH, "//span[@elementtiming='72']").click()

# 判断"Devices ready", "Devices not ready", "Devices not registered"是否显示在界面上
elements = driver.find_elements(
    By.XPATH, "//div[@class='root-306']//span[@class='annotationText-308']"
)
element_set = {element.text for element in elements}
assert element_set.issubset(
    {"Devices ready", "Devices not ready", "Devices not registered"}
), "Devices ready, Devices not ready, Devices not registered is not be finded"
# 调试element_set
for e in element_set:
    logging_format(e)

# 关闭浏览器
input()
sleep(2)
driver.quit()
