# 字串的處理
words = 'she sell sea shell on the sea shore'
print('字數:', len(words))
print(words[2:10])
print('有幾個 s:', words.count('s'))
print('words 中是否有包含 sea:', words.find('sea'), '有' if words.find('sea') >= 0 else '無')
print('words 中是否有包含 sky:', words.find('sky'), '有' if words.find('sky') >= 0 else '無')
# words 有幾個單字
# amount = len(words.split(" "))  # split 切割字串
amount = len(words.split())  # split 切割字串 (預設就是以 " " 切割)
print(amount)
# 取得每一個單字
word = words.split()
print(words, type(words))
print(word, type(word))
print(word[0])  # 取第一個字
print(word[1])  # 取第二個字
print(word[-1])  # 取最後一個字

