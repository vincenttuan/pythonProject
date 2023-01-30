import math
# 數學相關的應用
x = 9
y = math.sqrt(x)  # 開根號
print(y)
z = math.pow(y, 2)  # 次方, 等同 **
print(z)
# 題目: 有二點A, B, A點(5, 3), B點(-6, 8) 求二點間的距離
x1, y1 = 5, 3
x2, y2 = -6, 8
dx = math.pow(x1 - x2, 2)
dy = math.pow(y1 - y2, 2)
d = math.sqrt(dx + dy)
print('距離 = %.1f' % d)


