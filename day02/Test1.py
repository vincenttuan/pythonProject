import keyword
# 保留字
print(keyword.kwlist)

# 變數的覆值
a = b = c = 100

age, name, ok = 18, "John", True
print(age, type(age))
print(name, type(name))
print(ok, type(ok))

# 刪除變數
del age
print(age)  # 刪除後就不可以再使用
