from day05.自訂涵式1 import hello
from day05.自訂涵式2 import add
from day05.自訂涵式3 import calcBmi, get_bmi, verify_bmi

# 主程式
if __name__ == '__main__':
     hello()
     add(10, 20)
     calcBmi(170, 50)
     calcBmi(180, 70)
     calcBmi(160, 60)
     bmi = get_bmi(170, 60)
     print(bmi)
     print(verify_bmi(30.5))
