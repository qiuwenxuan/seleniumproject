import configparser
import logging.config
import os
from time import sleep
import pytest
import yaml
from selenium import webdriver


@pytest.fixture(scope="function")
def driver(config):
    """初始化Chrome浏览器驱动"""

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")  # 启用隐私模式
    driver = webdriver.Chrome(options=chrome_options)

    driver.implicitly_wait(float(config.get("wait_time")))  # 设置隐式等待时间

    yield driver  # 在测试函数中使用这个 driver 实例

    # 测试结束后，关闭浏览器
    sleep(2)
    driver.quit()


@pytest.fixture(scope="module")
def config():
    """读取配置文件并返回 'settings' 部分"""
    config = configparser.ConfigParser()
    print(os.getcwd())
    # 读取配置文件
    config_file_path = r"E:\workspace\seleniumproject\AutopatchDevice\config\config.ini"
    if not os.path.exists(config_file_path):
        raise FileNotFoundError(f"Config file not found at: {config_file_path}")

    config.read(config_file_path, encoding='utf-8')

    if 'settings' not in config:
        raise KeyError("The 'settings' section is not found in the config file.")

    return config["settings"]


@pytest.fixture(scope="function")
def my_logger(default_path=r"E:\workspace\seleniumproject\AutopatchDevice\config\logging.yaml",
              default_level=logging.INFO, env_key="LOG_CFG"):
    path = default_path
    value = os.getenv(env_key)

    # 添加调试信息
    print(f"Environment variable {env_key}: {value}")

    if value:
        path = value
    print(f"Using config file path: {path}")

    if os.path.exists(path):
        with open(path, "r", encoding='utf-8') as f:
            config = yaml.safe_load(f)
            logging.config.dictConfig(config)
            my_logger = logging.getLogger("my_logger")
            return my_logger
    else:
        logging.basicConfig(level=default_level)
        return logging
