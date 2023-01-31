# 撰寫一個 BMI 計算系統
try:
    h = float(input('請輸入身高: '))
    w = float(input('請輸入體重: '))
    print(h, type(h))
    print(w, type(w))
    bmi = w / (h/100)**2
    print('BMI = %.2f' % bmi)
    if 18 < bmi <= 23:
        print("正常")
    else:
        print("不正常")
    # -----------------------------
    if bmi <= 18:
        print("過輕")
    elif bmi > 23:
        print("過重")
    else:
        print("正常")
except:
    print('請輸入數字資料...')




