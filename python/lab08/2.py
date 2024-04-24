print('1 -----------------------------')
mark1 = ['хорошо', 'удовлитворительно']
print(mark1)
print(id(mark1))
mark1.append('неудовлитворительно')
print(mark1)
mark1.insert(0, 'отлично')
print(mark1)
print(id(mark1))
print(mark1[0:3])

print('2 -----------------------------')

mark2 = ['четный', 'нечетный']
print(mark2)
print(id(mark2))
mark3 = mark2 * 2
print(mark3)
print(id(mark3))
