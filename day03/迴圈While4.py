# 猜數字 1 ~ 9
# 若猜得比答案大 -> 顯示猜大了
# 若猜得比答案小 -> 顯示猜小了
import random as r

answer = r.randint(1, 9)
while True:
    # 玩家:
    # ---------------------------------------
    guess = input('玩家請輸入 1~9 數字: ')
    # 防呆1: 判斷是否輸入的都是數字
    if not guess.isdigit():
        print('請輸入數字')
        continue
    guess = int(guess)
    # 防呆2: 判斷數字是否合法
    if guess < 1 or guess > 9:
        print('數字範圍不正確')
        continue
    # ---------------------------------------
    # 進行判斷
    if guess > answer:
        print('猜大了')
    elif guess < answer:
        print('猜小了')
    else:
        print('答案: {}, 玩家贏了'.format(answer))
        break
    # 電腦:
    # ---------------------------------------
    pc_guess = r.randint(1, 9)
    print('電腦請輸入 1~9 數字: {}'.format(pc_guess))
    # ---------------------------------------
    # 進行判斷
    if pc_guess > answer:
        print('電腦猜大了')
    elif pc_guess < answer:
        print('電腦猜小了')
    else:
        print('答案: {}, 電腦贏了'.format(answer))
        break

print('GG')
