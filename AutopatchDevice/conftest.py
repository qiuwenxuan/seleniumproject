import logging
from time import sleep
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver(config):
    """初始化Chrome浏览器驱动"""

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")  # 启用隐私模式
    driver = webdriver.Chrome(options=chrome_options)
    # 初始化logger对象
    setup_logging()
    global WAIT_TIME
    driver.implicitly_wait(float(config.get("wait_time")))  # 设置隐式等待时间

    yield driver  # 在测试函数中使用这个 driver 实例

    # 测试结束后，关闭浏览器
    sleep(2)
    driver.quit()


def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    file_handler = logging.FileHandler(r"C:\workspace\pythonstudy\log\test.log")
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
