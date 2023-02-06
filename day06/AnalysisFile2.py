import matplotlib.pyplot as plt
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

    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(names, salary, marker="o", label="薪資(K)")
    plt.plot(names, age, marker="o", label="年齡")
    plt.legend()
    plt.grid(True)
    plt.show()
