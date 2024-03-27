print('1)==================>')
txt = "abcdefg"
print(txt, ' = ', len(txt), ' символов')
print(txt[0:3])
print(txt[2:5])
print(txt[5:2])
print(txt[1:15])
# print(txt[15])

print('\n2)==================>')
txt = "987654321"
print(txt[-4:-1])
print(txt[-1:-4])
print(txt[-1:-1])

print('\n3)==================>')
txt = "0123456789"
print(txt[:4])
print(txt[2:])
print(txt[:])

print('\n4)==================>')
txt = "987654321"
print(txt[-4:-1])
print(txt[-4:3])
print(txt[-4:7])
print(txt[-4:0])

print('\n5)==================>')
price = 3433.61
dot = str(price).find(".")
print(dot)
print(f'Сумма покупки {str(price)[0:dot]} руб., скидка {str(price)[(dot + 1):]} коп.')
