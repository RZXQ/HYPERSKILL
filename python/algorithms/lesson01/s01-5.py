import random

x = int(input('输入红包的总金额：'))
a = random.randint(1, x - 1)
b = x - a
print('第一个红包的金额是：', a)
print('第二个红包的金额是：', b)
