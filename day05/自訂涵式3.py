# 有三組(h, w)資料 170, 50 ; 180, 70 ; 160, 60
# 請試做一個 def calcBmi 方法
# calcBmi 方法可以輸入 2 個參數
# 可以印出 bmi 值 與 bmi 是否正常 (18<bmi<=23 正常範圍)
def calcBmi(h, w):
    # 1. 計算 bmi 值
    bmi = w / (h/100)**2
    # 2. 驗證 bmi
    result = '正常'  # 假設驗證結果正常
    if bmi > 23:
        result = '過胖'
    elif bmi <= 18:
        result = '過輕'
    # 3. 印出資料
    print('BMI: {0:.1f} {1}'.format(bmi, result))

