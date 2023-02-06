import statistics as stat
from day06.ReadFile import get_employees
# 資料分析
if __name__ == '__main__':
    # 資料讀取
    employee_salary = get_employees('salary.txt')
    print(len(employee_salary))
    print(employee_salary)
    # 資料分析(薪資)
    # 取得所有薪資[] -> [45000, 85000, 75000, ...]
    salary = [emp['salary'] for emp in employee_salary]
    print(salary)
    print('薪資總和: {:,}'.format(sum(salary)))
    print('薪資平均: {:,}'.format(stat.mean(salary)))
    print('薪資中位數: {:,}'.format(stat.median(salary)))
    print('薪資標準差 SD: {:,.1f}'.format(stat.stdev(salary)))
    print('薪資變異係數 CV: {:.2f}'.format(stat.stdev(salary)/stat.mean(salary)))
    # --------------------------------------------------------------------------
    # 資料讀取
    employee_age = get_employees('age.txt', column2='age')
    print(employee_age)
    # 資料分析(年齡)
    # 取得所有年齡[] -> [25, 52, 45, ...]
    age = [emp['age'] for emp in employee_age]
    print(age)
    print('年齡總和: {:,}'.format(sum(age)))
    print('年齡平均: {:,}'.format(stat.mean(age)))
    print('年齡中位數: {:,}'.format(stat.median(age)))
    print('年齡標準差 SD: {:,.1f}'.format(stat.stdev(age)))
    print('年齡變異係數 CV: {:.2f}'.format(stat.stdev(age) / stat.mean(age)))