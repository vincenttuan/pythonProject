# 字串分析
data = "一杯咖啡55元買一送一,小明買5 杯共要多少錢"
price = data[data.find('咖啡')+2:data.find('元')].strip()
cup = data[data.find('小明買')+3:data.find('杯共')].strip()
print(price, cup)
price = int(price)
cup = int(cup)
total = price * cup
print(total)
total = price * (cup - cup // 2)
print(total)
