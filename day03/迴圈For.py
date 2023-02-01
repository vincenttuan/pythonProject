# for-loop 步進迴圈
# 印出 10 個 Python
count = 10
while count > 0:
    print('Python')
    count = count - 1
# ---------------------
for i in range(0, 10):  # 0~9, 預設i每次+1
    print(i, 'Python')
# ---------------------
for i in range(0, 10, 2):  # 0~9, i每次+2
    print(i, 'Python')
# ---------------------
for score in [100, 90, 80, 70, 60]:
    print(score)
# ---------------------
for i, score in enumerate([100, 90, 80, 70, 60]):
    print(i, score)

