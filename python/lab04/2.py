print('\n 1)\n')

x = 1000
y = x
print('x= ' + str(x) + ', id x = ' + str(id(x)))
print('y= ' + str(y) + ', id y = ' + str(id(y)))
print('------------ x = 1001 -------')
x = 1001
print('x= ' + str(x) + ', id x = ' + str(id(x)))
print('y= ' + str(y) + ', id y = ' + str(id(y)))

print('\n 2)\n')

print('---- x = 2; x *= 2 + 3-------')
x = 2
x *= 2 + 3
print('x= ' + str(x) + ', id x = ' + str(id(x)))

print('\n 3)\n')

x = 81
print('---- x = 81 -------')
print('x= ' + str(x) + ', id x = ' + str(id(x)))

x *= 3
print('---- x *= 3 -------')
print('x= ' + str(x) + ', id x = ' + str(id(x)))

print()

x = 512
print('---- x = 512 --------')
print('x= ' + str(x) + ', id x = ' + str(id(x)))

x *= 3
print('---- x *= 3 ---------')
print('x= ' + str(x) + ', id x = ' + str(id(x)))

print('\n 4)\n')

next_day = 'После 28 февраля будет '
year = 2016
next_day += '1 марта' if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) else '29 февраля'
print(next_day)
