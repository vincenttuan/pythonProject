# 字典數組 : Dict
emp1 = {'name': 'John', 'salary': 50000}
print(emp1)
print(emp1['name'], type(emp1['name']))
print(emp1['salary'], type(emp1['salary']))
emp1['salary'] = 55000
print(emp1['salary'])
emp2 = {'name': 'Mary', 'salary': 80000}
emp3 = {'name': 'Bobo', 'salary': 60000}
# ------------------------------------------
employees = [emp1, emp2, emp3]
print(employees)
# ------------------------------------------
# 印出每一個員工姓名與薪資
for emp in employees:
    print('姓名:{} 薪資:${:,}'.format(emp['name'], emp['salary']))
# ------------------------------------------
# Part I 計算總薪資 = ?
salary_list = [emp['salary'] for emp in employees]
print(salary_list)  # [55000, 80000, 60000]
print(sum(salary_list))  # 195000
# ------------------------------------------
print(sum([emp['salary'] for emp in employees]))
# ------------------------------------------
# PartII 計算總薪資 = ?
total = 0  # 預設總薪資 = 0
for emp in employees:
    total = total + emp['salary']
print(total)
# ------------------------------------------
# PartIII 計算總薪資 = ?
total = employees[0]['salary'] + employees[1]['salary'] + employees[2]['salary']
print(total)
# ------------------------------------------
# 請問最高薪資 ?
high_salary = 0  # 假設最高薪資 = 0
for emp in employees:
    if emp['salary'] > high_salary:
        high_salary = emp['salary']  # 將最高薪資替換
print('最高薪資: {:,}'.format(high_salary))
# ------------------------------------------
# 請問最低薪資 ? 自行練習看看
low_salary = high_salary  # 假設最低薪資 = 最高薪資
for emp in employees:
    if emp['salary'] < low_salary:
        low_salary = emp['salary']
print('最低薪資: {:,}'.format(low_salary))
# ------------------------------------------
# 將最高與最低薪資的人名放入到一個 names 的列表中
# 印出 names 例如: ['John', 'Mary']
salary_list = [emp['salary'] for emp in employees]
high_salary = max(salary_list)  # 80000
low_salary = min(salary_list)  # 55000
names = []
for emp in employees:
    if emp['salary'] == high_salary or emp['salary'] == low_salary:
        names.append(emp['name'])
print(names)
