import re
# 資料讀取
def get_employees(filename, colume1='name', column2='salary'):
    file = open(filename, 'r', encoding='UTF-8')
    rows = file.readlines()
    # print(rows)
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
        if len(row.strip()) == 0:
            continue
        # print(row)
        data = re.split(' |, |,', row)  # 使用 re.split() 來切割資料
        # print(data)
        # --------------------------------------
        emp = {}  # 建立一個 dict 數組
        emp.setdefault(colume1, data[0])
        emp.setdefault(column2, int(data[1]))
        # --------------------------------------
        employee_salary.append(emp)

    return employee_salary



