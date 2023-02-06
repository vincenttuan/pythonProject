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


