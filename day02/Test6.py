# 排版
name1, name2, name3 = 'John', 'Helen', 'Jo'
score1, score2, score3 = 90, 100, 45

print('name = %5s score = %3d' % (name1, score1))
print('name = %5s score = %3d' % (name2, score2))
print('name = %5s score = %3d' % (name3, score3))

print('name = %-5s score = %3d' % (name1, score1))
print('name = %-5s score = %3d' % (name2, score2))
print('name = %-5s score = %3d' % (name3, score3))

print('name = %-5s score = %03d' % (name1, score1))
print('name = %-5s score = %03d' % (name2, score2))
print('name = %-5s score = %03d' % (name3, score3))
