# 迴圈 while
import random as r
play = True
while play:
    n = r.randint(1, 100)
    print(n)
    if n == 99:
        play = False

print('程式結束')




