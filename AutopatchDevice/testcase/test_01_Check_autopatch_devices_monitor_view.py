import configparser
import logging
import os
from time import time
import pytest

from AutopatchDevice.TestTools import save_screenshot, ele_input, ele_click, get_ele_html


@pytest.fixture(scope="module")
def config():
    """读取配置文件并返回 'settings' 部分"""
    config = configparser.ConfigParser()
    print(os.getcwd())
    # 读取配置文件
    config_file_path = r"E:\workspace\seleniumproject\AutopatchDevice\config.ini"
    if not os.path.exists(config_file_path):
        raise FileNotFoundError(f"Config file not found at: {config_file_path}")

    config.read(config_file_path, encoding='utf-8')

    if 'settings' not in config:
        raise KeyError("The 'settings' section is not found in the config file.")

    return config["settings"]


def test_01_Check_autopatch_devices_monitor_view(driver, config):
    """测试检查 autopatch 设备监控视图"""
    url = config.get("url")
    username = config.get("username")
    password = config.get("password")
    length = int(config.get("windows_length"))
    width = int(config.get("windows_width"))
    wait_time = float(config.get("wait_time"))

    logging.info("url:" + url)
    logging.info("username:" + username)
    logging.info("password:" + password)
    logging.info("wait_time:" + str(wait_time))

    # 打开PPE环境网址
    driver.set_window_size(length, width)  # 设置页面窗口的大小
    driver.get(url)

    # 登录界面输入框,输入用户名密码
    ele_input(driver, '//input[@type="email"]', username, "\n")
    ele_input(driver, '//input[@name="passwd"]', password)
    ele_click(driver, '//input[@id="idSIButton9"]')

    logging.info("driver.title:" + driver.title)  # 登录到 Microsoft Azure
    # 保持登录状态弹窗确认
    if driver.title == "登录到 Microsoft Azure":
        ele_click(driver, "//*[@id='KmsiCheckboxField']")
        ele_click(driver, "//*[@id='idSIButton9']")

    # 登录到device->windows update->monitor->autopatch device
    ele_click(driver, "//div[text()='Devices']")
    ele_click(driver, "//div[text()='Windows updates']")

    # 跳转到frame内部代码，点击Monitor按钮
    driver.switch_to.frame("_react_frame_2")
    ele_click(driver, "//span[text()='Monitor']")

    # 判断"Devices ready", "Devices not ready", "Devices not registered"是否显示在界面上
    element_text = get_ele_html(driver, "//span[text()='Devices ready']/../../../../..")
    logging.info("element_text" + element_text)

    # 窗口截图命名并保存
    save_screenshot(driver)

    # 定义期望出现的文本
    expected_texts = ["Devices ready", "Devices not ready", "Devices not registered"]
    # 检查每个期望的文本是否存在于页面中
    for text in expected_texts:
        assert text in element_text, f"{text} is not found in the page."
