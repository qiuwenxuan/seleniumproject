import configparser
import logging
import os
from time import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def config():
    """读取配置文件并返回 'settings' 部分"""
    config = configparser.ConfigParser()
    config_file_path = r"/AutopatchDevice/config.ini"

    # 读取配置文件
    config.read(config_file_path)

    # 确保 'settings' 部分存在
    if not config.has_section("settings"):
        pytest.fail("The 'settings' section is missing in the config file.")

    return config["settings"]


def test_01_Check_autopatch_devices_monitor_view(driver, config):
    """测试检查 autopatch 设备监控视图"""
    url = config.get("url")
    username = config.get("username")
    password = config.get("password")
    length = int(config.get("windows_length"))
    width = int(config.get("windows_width"))
    wait_time = float(config.get("wait_time"))

    logging.debug(url)
    logging.debug(username)
    logging.debug(password)

    # 打开PPE环境网址
    driver.set_window_size(length, width)  # 设置页面窗口的大小
    driver.get(url)

    logging.debug(wait_time)

    # 登录界面输入框,输入用户名密码
    WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@type="email"]'))
    ).send_keys(f"{username}\n")
    WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@name="passwd"]'))
    ).send_keys(password)
    WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@id="idSIButton9"]'))
    ).click()

    logging.debug(driver.title)  # 登录到 Microsoft Azure
    # 保持登录状态弹窗确认
    if driver.title == "登录到 Microsoft Azure":
        WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='KmsiCheckboxField']"))
        ).click()
        WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='idSIButton9']"))
        ).click()

    # 登录到device->windows update->monitor->autopatch device
    WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Devices']"))
    ).click()
    WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Windows updates']"))
    ).click()

    # 跳转到frame内部代码，点击Monitor按钮
    driver.switch_to.frame("_react_frame_2")
    WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Monitor']"))
    ).click()

    # 判断"Devices ready", "Devices not ready", "Devices not registered"是否显示在界面上
    element_text = driver.find_element(
        By.XPATH, "//span[text()='Devices ready']/../../../../.."
    ).get_attribute("outerHTML")
    logging.debug(element_text)

    # 窗口截图命名并保存
    file_name = os.path.basename(__file__).split("_")[1]
    time_stamp = round(time() * 1000)
    phone_name = f"{file_name}_{time_stamp}.png"
    logging.debug(f"保存的文件名为{phone_name}")
    driver.get_screenshot_as_file(phone_name)

    # 定义期望出现的文本
    expected_texts = ["Devices ready", "Devices not ready", "Devices not registered"]
    # 检查每个期望的文本是否存在于页面中
    for text in expected_texts:
        assert text in element_text, f"{text} is not found in the page."
