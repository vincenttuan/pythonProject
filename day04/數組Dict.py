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
