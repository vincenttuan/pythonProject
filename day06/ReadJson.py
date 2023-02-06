import json

json_str = '{"name": "John", "salary": 45000, "age": 28}'
emp = json.loads(json_str) # json string 轉 dict 數組
print(emp, type(emp))
# 改變薪資
emp['salary'] = emp['salary'] * 1.2
print(emp, type(emp))
print("--------------------------------------------------")
# 傳送給雲端
json_str = json.dumps(emp)  # 將 dict 數組轉 json string
print(json_str, type(json_str))
