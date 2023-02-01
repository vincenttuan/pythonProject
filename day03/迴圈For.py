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
