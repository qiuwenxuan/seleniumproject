import configparser

file = r"/AutopatchDevice/config/config.ini"

# 创建配置文件对象
con = configparser.ConfigParser()

# 读取文件
con.read(file, encoding="utf-8")

# 获取所有section
sections = con.sections()
print(sections)
# ['url', 'email']


# 获取特定section
items = con.items("settings")  # 返回结果为元组
print(items)
# [('baidu','http://www.baidu.com'),('port', '80')] 	# 数字也默认读取为字符串

# 可以通过dict方法转换为字典
items = dict(items)
print(items)
