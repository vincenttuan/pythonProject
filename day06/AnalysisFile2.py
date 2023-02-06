import matplotlib.pyplot as plt
import statistics as stat
from day06.ReadFile import get_employees

if __name__ == '__main__':
    employees = get_employees('salary_age.txt', column3='age')
    print(employees)
    # 繪製薪資與年齡的折線圖
    names = [emp['name'] for emp in employees]
    salary = [emp['salary']//1000 for emp in employees]  # 將薪資除以 1000
    age = [emp['age'] for emp in employees]
    print(names)
    print(salary)
    print(age)
    # 計算 CV
    salary_cv = stat.stdev(salary) / stat.mean(salary)
    age_cv = stat.stdev(age) / stat.mean(age)

    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(names, salary, marker="o", label="薪資(K) CV:{0:.2f}% 平均:{1:,.1f}K".format(salary_cv*100, stat.mean(salary)))
    plt.plot(names, age,    marker="o", label="年齡 CV:{0:.2f}% 平均:{1:.1f}".format(age_cv*100, stat.mean(age)))
    plt.legend()
    plt.grid(True)
    plt.ylabel("年齡/薪資(K)")
    plt.xlabel("姓名")
    plt.title("員工資料統計表")
    plt.show()
