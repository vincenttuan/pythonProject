import random as r
# 數組/陣列 set() 元素不可重複
nums = set()
nums.add(10)
nums.add(10)
nums.add(9)
print(nums, len(nums))
# 樂透 539 , 1~39 取出 5 個不重複的數字
# 請寫出電腦選號程式
lotto = set()
while len(lotto) < 5:
    lotto.add(r.randint(1, 39))
print(lotto, len(lotto))
# set() 沒有 index
# 所以要轉成 list
lotto = list(lotto)
print(lotto)
# 改成唯讀陣列
lotto = tuple(lotto)
print(lotto)
print(lotto[0])
print(lotto[1])


