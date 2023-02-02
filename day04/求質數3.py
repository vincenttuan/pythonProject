# 求小於 10000 的最大值數 = ?
for num in range(10000, 2, -1):
    is_prime = True  # 假設 num 是質數
    for i in range(2, num//2+1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print('{} 是質數'.format(num))
        break
