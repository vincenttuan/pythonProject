# 建立資料庫 demo.db
import sqlite3

# 連接資料庫, 若 demo.db 不存在會自動建立
conn = sqlite3.connect('demo.db')
print('連接資料庫成功!')
conn.close()  # 關閉連線

