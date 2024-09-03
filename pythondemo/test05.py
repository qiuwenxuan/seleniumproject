# 摄氏温度转华氏温度
# 用户输入摄氏温度

# 接收用户输入
type = input("输入为摄氏温度选C,华氏温度选F:")
w = float(input("输入温度: "))
if type.upper() == "C":
    # 计算华氏温度
    s = (w * 1.8) + 32
elif type.upper() == "F":
    # 计算摄氏温度
    s = (w - 32) / 1.8
else:
    raise ("type error!")
print("%0.1f 摄氏温度转为华氏温度为 %0.1f " % (w, s))
