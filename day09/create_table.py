import sqlite3
# 建立 employee 資料表
# 欄位 id, employee_name, employee_salary, create_time
sql = '''
    create table if not exists employee(
        id integer not null primary key autoincrement, 
        employee_name text not null,
        employee_salary integer,
        create_time timestamp default current_timestamp
    )
'''

# 1. 連線到資料庫
conn = sqlite3.connect('demo.db')
# 2. 取得資料庫操作權(指標) -> cursor
cursor = conn.cursor()
# 3. 透過 cursor 執行 sql 語句
cursor = cursor.execute(sql)
print('建立資料表 OK')
# 4. 任務提交
conn.commit()
# 5. 關閉連線
conn.close()


