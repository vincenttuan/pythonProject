from day06.ReadFile import get_employees
# 資料分析
if __name__ == '__main__':
    employee_salary = get_employees('salary.txt')
    print(len(employee_salary))
    print(employee_salary)
