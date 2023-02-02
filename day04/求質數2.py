# 請印出 1~100 之間的質數
for num in range(2, 100):
    is_prime = True  # 假設 num 是質數
    for i in range(2, num//2+1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print('{} 是質數'.format(num))
