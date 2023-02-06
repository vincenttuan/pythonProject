# 資料讀取
file = open('salary.txt', 'r', encoding='UTF-8')
rows = file.readlines()
print(rows)
# 資料整理
'''
例如:
employee_salary = 
[
    {"name": "John", "salary": 45000},
    {"name": "Mary", "salary": 85000},
    {"name": "傑克", "salary": 75000},
    {"name": "蘿絲", "salary": 60000},
    ...
]
'''
employee_salary = []
for row in rows:
    # print(row)
    data = row.split()  # 預設是 " " 切割字串
    # print(data)
    # --------------------------------------
    emp = {}  # 建立一個 dict 數組
    emp.setdefault('name', data[0])
    emp.setdefault('salary', int(data[1]))
    # --------------------------------------
    employee_salary.append(emp)

print(employee_salary)
# 資料分析

