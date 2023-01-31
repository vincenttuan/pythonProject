# 排版 format
name1, name2, name3 = 'John', 'Helen', 'Jo'
score1, score2, score3 = 90, 100, 45

print('name = {} score = {}'.format(name1, score1))
print('name = {0} score = {1}'.format(name1, score1))
print('name = {1} score = {0}'.format(name1, score1))
print('name = {1} score = {5}'.format(name1, name2, name3, score1, score2, score3))

cash = 1234567890
print('cash = {0:,}'.format(cash))

amount = 1234567890.54321
# 請印到小數點二位並帶千分號 -> 1,234,567,890.54
print("{:,}".format(float('%.2f' % amount)))
print("{:,.2f}".format(amount))

