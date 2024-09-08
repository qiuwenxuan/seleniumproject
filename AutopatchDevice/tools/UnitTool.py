import logging
import os
from time import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


# 获取元素的OuterHTML
def get_ele_html(driver, xpath_exp):
    return driver.find_element(
        By.XPATH, xpath_exp
    ).get_attribute("outerHTML")


# 显示等待输入框函数
def ele_input(driver, xpath_exp, input_str, esc="", wait_time=30):
    WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.XPATH, xpath_exp))
    ).send_keys(f"{input_str}{esc}")


# 显示等待点击函数
def ele_click(driver, xpath_exp, wait_time=30):
    WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((By.XPATH, xpath_exp))
    ).click()


# 截图生成图片方法
def save_screenshot(driver, directory=r"E:\workspace\seleniumproject\file"):
    """
    截图并保存图片到指定目录。

    :param driver: Selenium WebDriver 对象
    :param directory: 保存截图的目录路径，默认为 'file'
    :return: 保存的截图文件的路径
    """
    # 获取当前脚本名称，不包含扩展名
    script_name = os.path.basename(__file__)
    logging.info("script_name" + script_name)
    script_name = os.path.basename(__file__).split('_')[1]

    # 获取时间戳
    timestamp = round(time() * 1000)

    # 组合文件名
    screenshot_filename = f"{script_name}_{timestamp}.png"

    # 创建保存截图的目录，如果目录不存在
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 拼接完整的文件路径
    file_path = os.path.join(directory, screenshot_filename)

    # 保存截图
    driver.get_screenshot_as_file(file_path)
    logging.debug(f"Screenshot saved as {file_path}")

    return file_path


# 格式化输出日志
def logging_format(
        message,
        form: str = "info",
        signal: str = "=",
        total_length: int = 80,
) -> None:
    """
    格式化字符串以居中显示，并输出为不同级别的日志信息。

    Args:
        message (str): 打印的字符串信息。
        form (str): 选择采用 info、debug、error 级别打印日志。
        signal (str, optional): 输出日志的符号。默认是 "="。
        total_length (int, optional): 输出日志的长度。默认是 80。

    Returns:
        None
    """
    message = str(message)

    # 计算需要填充的符号的数量
    if message is None or message == "":
        logging.info(message)
        return

    padding_length = total_length - len(message)

    # 确保 padding_length 不小于 0
    if padding_length < 0:
        padding_length = 0

    # 计算左右填充的符号数量
    left_padding = padding_length // 2
    right_padding = padding_length - left_padding

    # 格式化字符串
    formatted_message = f"{signal * left_padding}{message}{signal * right_padding}"

    # 根据日志级别输出日志
    if form == "debug" or form.upper() == "D":
        logging.debug(formatted_message)
    elif form == "info" or form.upper() == "I":
        logging.info(formatted_message)
    elif form == "error" or form.upper() == "E":
        logging.error(formatted_message)
    else:
        raise ValueError(
            f"Invalid form parameter: {form}. Expected 'debug', 'info', or 'error'."
        )


if __name__ == "__main__":
    # 示例使用
    element_text = "element"  # 用实际的 element.text 替换
    logging_format(element_text)
