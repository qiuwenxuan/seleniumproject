import pytest

from AutopatchDevice.exception.EleNotFoundException import EleNotFoundException
from AutopatchDevice.testcase.conftest import driver, config, my_logger
from AutopatchDevice.tools.UnitTool import save_screenshot, ele_input, ele_click, get_ele_html


def test_01_Check_autopatch_devices_monitor_view(driver, config, my_logger):
    """测试检查 autopatch 设备监控视图"""
    url = config.get("url")
    username = config.get("username")
    password = config.get("password")
    length = int(config.get("windows_length"))
    width = int(config.get("windows_width"))
    wait_time = float(config.get("wait_time"))

    my_logger.info("url:" + url)
    my_logger.info("username:" + username)
    my_logger.info("password:" + password)
    my_logger.info("wait_time:" + str(wait_time))

    # 打开PPE环境网址
    driver.set_window_size(length, width)  # 设置页面窗口的大小
    driver.get(url)

    # 登录界面输入框,输入用户名密码
    ele_input(driver, '//input[@type="email"]', username, "\n")
    ele_input(driver, '//input[@name="passwd"]', password)
    ele_click(driver, '//input[@id="idSIButton9"]')

    my_logger.info("driver.title:" + driver.title)  # 登录到 Microsoft Azure
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
    my_logger.info("element_text" + element_text)

    # 窗口截图命名并保存
    save_screenshot(driver)

    # 定义期望出现的文本
    expected_texts = ["Devices ready", "Devices not ready", "Devices not registered"]
    # 检查每个期望的文本是否存在于页面中
    try:
        for text in expected_texts:
            if text not in element_text:
                my_logger.error(f"{text} is not found in the page.")
                raise EleNotFoundException(f"{text} is not found in the page.")
    except EleNotFoundException as e:
        my_logger.exception(e)
    else:
        my_logger.info(f"test_01_Check_autopatch_devices_monitor_view is passed")


if __name__ == "__main__":
    pytest.main([r'.\AutopatchDevice\testcase\test_01_Check_autopatch_devices_monitor_view.py ',
                 '-vs'])
