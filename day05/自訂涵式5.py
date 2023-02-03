import statistics as stat
# 調查有5位同學的身高與體重
no = [1, 2, 3, 4, 5]  # 座號
h = [172, 168, 164, 170, 176]  # cm
w = [62, 57, 58, 64, 64]  # kg
# 問該學生的身高與體重哪一個分散程度大
# 變異係數 cv = sd(標準差) / avg(平均)
h_cv = stat.stdev(h) / stat.mean(h)  # 身高的變異係數
w_cv = stat.stdev(w) / stat.mean(w)  # 體重的變異係數
print('身高 CV: %.2f%%' % (h_cv*100))
print('體重 CV: %.2f%%' % (w_cv*100))
result = '身高' if h_cv > w_cv else '體重'
print('[%s]分散程度大' % result)

