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
