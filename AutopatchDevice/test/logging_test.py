import sys
import logging

# 设置标准输出流的编码为 UTF-8
sys.stdout.reconfigure(encoding="utf-8")

# 创建一个名为 'my_logger' 的 Logger 对象
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# 创建一个 Handler，输出日志到控制台
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 创建一个 Handler，输出日志到文件
file_handler = logging.FileHandler("my_log.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# 创建一个 Formatter，定义日志信息的格式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# 为 Handler 设置 Formatter
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 为 Logger 添加 Handler
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 记录日志信息
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")

import os

print(os.getcwd())
