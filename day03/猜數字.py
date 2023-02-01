# 猜數字遊戲
import random as r
min, max = 0, 100
# answer = 84
answer = r.randint(min + 1, max - 1)

while True:
    guess = input('玩家 {} ~ {} 之間猜一個數字: '.format(min, max))
    guess = int(guess)
    if guess < answer:
        min = guess
    elif guess > answer:
        max = guess
    else:
        print('答案: {} 恭喜玩家答對了'.format(answer))
        break


