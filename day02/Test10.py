words = '小明本薪$65000,今年公司發放6個月,試問小明年終'
print(words[5:10])
print(words[words.find('$')+1:words.find(',')])
print(words[words.find('發放')+2:words.find('個月')])
# --------------------------------------------------------
salary = int(words[words.find('$')+1:words.find(',')])
month = int(words[words.find('發放')+2:words.find('個月')])
print(salary * month)
