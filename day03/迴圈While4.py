# 猜數字 1 ~ 9
# 若猜得比答案大 -> 顯示猜大了
# 若猜得比答案小 -> 顯示猜小了
import random as r

answer = r.randint(1, 9)
while True:
    guess = input('玩家請輸入 1~9 數字: ')
    guess = int(guess)
    # 進行判斷
    if guess > answer:
        print('猜大了')
    elif guess < answer:
        print('猜小了')
    else:
        print('答案: {}, 玩家贏了'.format(answer))
        break

print('GG')
