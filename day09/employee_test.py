from day09.employee_crud import create_employee, create_many_employee

if __name__ == '__main__':
    # 新增單筆資料
    # create_employee('John', 45000)
    # create_employee('Mary', 55000)
    # 新增多筆資料
    employees = [
        ('Helen', 72000),
        ('Alen', 120000),
        ('Bob', 88000)
    ]
    create_many_employee(employees)


