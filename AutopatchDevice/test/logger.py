import logging

# logging模块（默认日志打印）
# 配置默认logging采用的是basicConfig方法
# logging模块默认日志级别为level=logging.WARNING,只打印级别在warning及以上的级别日志，level=logging.INFO可以设置日志级别
# format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'可以自定义logging的日志输出格式
# filename定义了日志的输出文件名路径，filemode为w表示日志输出模块为write会覆盖之前的内容，filemode为a时，会创建日志文件，如果日志文件存在则追加内容在文件后;默认日志打印在控制台
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='../log/log.txt',
                    filemode='a')

logging.debug("debug...")
logging.info("info...")
logging.warning("warning...")
logging.error("error...")
logging.critical("critical...")

# 自定义logger,logging.getLogger()返回一个自定义logger对象实例，test_logger表示自定义logger名称，全局logger和logging名称为root，当logger名称相同时，返回相同的logger实例
test_logger = logging.getLogger("test_logger")
test_logger.setLevel(logging.INFO)

# 定义文件输出handler
file_handler = logging.FileHandler('test_logger.txt', mode='w')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
test_logger.addHandler(file_handler)

# 定义控制台输出handler
stream_handler = logging.StreamHandler()
file_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
test_logger.addHandler(stream_handler)

# 输出自定义logger日志,可以发现日志当中的name变为test_logger
test_logger.debug("test_logger error1")
test_logger.debug("test_logger error2")

try:
    1 / 0
except Exception as e:
    test_logger.exception(f"get exception{e}")
    logging.exception(f"get exception{e}")
