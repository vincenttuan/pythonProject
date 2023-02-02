# 求 9 是否是質數 = ?
num = 9
is_prime = True  # 假設 num 是質數
for i in range(2, num//2+1):
    print('{0} % {1} == 0, {2}'.format(num, i, (num % i == 0)))
    if num % i == 0:
        is_prime = False
        break

if is_prime:
    print('{} 是質數'.format(num))
else:
    print('{} 不是質數'.format(num))
