import logging

# 配置日志记录器
logger = logging.getLogger("test")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"
)

file_handler = logging.FileHandler(r"pythonstudy\log\test.log", encoding="utf-8")

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def logging_format(
    message: str,
    form: str = "info",
    signal: str = "=",
    total_length: int = 80,
) -> None:
    """
    格式化字符串以居中显示，并输出为不同级别的日志信息。

    Args:
        form (str): 选择采用 info、debug、error 级别打印日志。
        message (str): 打印的字符串信息。
        signal (str, optional): 输出日志的符号。默认是 "="。
        total_length (int, optional): 输出日志的长度。默认是 80。

    Returns:
        None
    """
    # 计算需要填充的符号的数量
    if message == None or message == "":
        logging.debug(message)
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
