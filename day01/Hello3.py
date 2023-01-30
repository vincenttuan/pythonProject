# 變數的應用
h = 170  # 身高cm
w = 60  # 體重kg
print(h, w)  # 印出 h, w 變數的內容
print(type(h), type(w))  # 印出 h, w 變數的型態
# 請計算 BMI 值
bmi = w / (h/100)**2
print(bmi)
print(type(bmi))
print("%.2f" % bmi)

