# 數組 List
nums = [100, 90, 80, 70]
print(nums)
print(sum(nums))
# ----------------------------
data = "100 90 80 70"
nums = []
for i in data.split():
    nums.append(int(i))
print(nums)
print(sum(nums))
# ----------------------------
data = "100 90 80 70"
nums = [int(i) for i in data.split()]
print(nums)
print(sum(nums))
