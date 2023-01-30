# https://zh.wikipedia.org/zh-tw/%E9%B8%A1%E5%85%94%E5%90%8C%E7%AC%BC
# 今有雉、兔同籠，上有三十五頭，下九十四足。問雉、兔各幾何？
total = 35
feet = 94
rabbit = (feet - (total*2))/(4-2)
chicken = total - rabbit
print('雞 = %d, 兔 = %d' % (chicken, rabbit))

