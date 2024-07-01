n = int(input('输入借书的天数：'))
if n == 1:
    s = 2
else:
    s = 2 + (n - 1) * 0.8
print('费用是', s, '元')
