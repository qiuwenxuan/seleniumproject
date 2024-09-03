# 测试一
num1 = input("num1:")  # input函数默认返回的是字符串，因此需要将其转型为float类型
num2 = input("num2:")

sum = float(num1) + float(num2)
print("数字{0}和数字{1}相加结果为{2}".format(num1, num2, sum))

# 测试二
print("两数之和为%.1f" % (float(input("num1:")) + float(input("num2:"))))
