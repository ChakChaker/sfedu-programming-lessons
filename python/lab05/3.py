print('1)==================>')
print("%4.4f" % 12.34)
print("%4.4f" % 123456.78)
print("%4.4f" % 1234.56987)
print("%4.0f" % 1234.56987)

print('\n2)==================>')
price = 387.68
dot = str(price).find(".")
print('Сумма покупки %d руб., скидка %s коп.' % (price, str(price)[(dot + 1):]))
