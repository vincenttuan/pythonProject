# if-else 練習
# 使用者輸入一個數, 並可以判斷奇/偶數
num = int(input('請輸入一個數字: '))
if num % 2 == 0:
    print(num, '是偶數')
else:
    print(num, '是奇數')
# --------------------------------
is_odd = num % 2 == 0
print(is_odd, type(is_odd))
if is_odd:
    print(num, '是偶數')
else:
    print(num, '是奇數')
# --------------------------------
print(num, '是偶數' if is_odd else '是奇數')
