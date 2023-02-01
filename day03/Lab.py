import re
data = '國文=100,數學=90,英文:70'
# 請計算總分與平均
data = data.split(",")
print(data)
total = 0
for item in data:
    score = re.split('=|:', item)  # 將 '國文=100' -> ['國文', '100']
    print(score)  # ['國文', '100']
    print(score[1])  # '100'
    total = total + int(score[1])

print(total, total/len(data))

