# 隨機數
import random as r

num = r.randint(1, 5)  # 含 1 與 5 的隨機數 1 <= r <= 5
print(num)
num = r.randrange(1, 5)  # 含 1 不含 5 的隨機數 1 <= r < 5
print(num)

# 樂透電腦選號三星彩 (0~9) 選 3 個可以重複的數字
n1 = r.randint(0, 9)
n2 = r.randint(0, 9)
n3 = r.randint(0, 9)
print('電腦選號: %d %d %d' % (n1, n2, n3))
print('電腦選號:', end=' ')
print(n1, end=' ')
print(n2, end=' ')
print(n3)
