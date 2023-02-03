import statistics as stat
import matplotlib.pyplot as plt

# 某公司有18位員工，其中10位在去年投資股票，一年的獲利率如下(單位：%)：
#   7.6 3.9 15.6 28.3 1.2 10.8 35.3 45.6 10.2 0.5
# 另外8位員工投資買公債一年內獲利率如下(單位：%)
#   6.8 7.2 6.8 7.5 6.9 7.9 7.9 7.1 7.2
# 試分別求此公司的員工投資股票與公債的獲利率變異係數。
# 繪製股票與公債獲利圖表

stock = (7.6, 3.9, 15.6, 28.3, 1.2, 10.8, 35.3, 45.6, 10.2, 0.5)
bond = (6.8, 7.2, 6.8, 7.5, 6.9, 7.9, 7.9, 7.1, 7.2)
stock_cv = stat.stdev(stock) / stat.mean(stock)
bond_cv = stat.stdev(bond) / stat.mean(bond)
print('stock cv: %.2f%%' % (stock_cv*100))
print('bond cv: %.2f%%' % (bond_cv*100))

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
plt.plot(stock, marker="o", label='股票')
plt.plot(bond, label='債券')
plt.legend(loc='upper right')
plt.ylabel("獲利")
plt.grid(True)
plt.title('股票債券獲利表')
plt.show()
