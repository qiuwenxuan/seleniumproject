# 随机数生成
import random

list1 = list([1, 2, 3, 4, 5])

rnum_A = random.random()  # 返回一个介于0.0和1.0之间的小数
rnum_B = random.randint(0, 9)  # 返回介于0~9之前的数，包含两边的端点
rnum_C = random.choice(list1)  # 随机返回任意迭代对象的值
rnum_D = random.shuffle(list1)  # 随机排序迭代对象的顺序，返回None值

print(rnum_A)
print(rnum_B)
print(rnum_C)
print(list1)
