from day06.ReadFile import get_employees

if __name__ == '__main__':
    employees = get_employees('salary_age.txt', column3='age')
    print(employees)
