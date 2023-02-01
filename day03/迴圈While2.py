# 迴圈 while
# break, continue
import random as r

while True:
    n = r.randint(1, 100)
    if n % 2 == 0:
        continue  # 重跑迴圈
    print(n)
    if n == 99:
        break  # 跳離迴圈

print('程式結束')
