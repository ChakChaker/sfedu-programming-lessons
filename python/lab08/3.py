ege4 = [["Математика", 78], ["Информатика", 75], ["Русский язык", 62]]
print(ege4)
print(ege4[1][0])


def total(ege):
    math = ege[0][1]
    inf = ege[1][1]
    rus = ege[2][1]
    return math + inf + rus


result = total(ege4)
print('Общая сумма баллов: ', result)

ege3 = ["Математика", 78, "Информатика", 75, "Русский язык", 62]


def total2(ege):
    math = ege[1]
    inf = ege[3]
    rus = ege[5]
    return math + inf + rus


result2 = total2(ege3)
print('Общая сумма баллов 2:', result2)


def convert_list(ege):
    ege2 = [[ege[0], ege[1]], [ege[2], ege[3]], [ege[4], ege[5]]]
    # math = ege[0:2]
    # inf = ege[2:4]
    # rus = ege[4:6]
    # ege2 = [math, inf, rus]
    return ege2


ege5 = convert_list(ege3)
print(ege5)
print('Общая сумма баллов 3:', total(ege5))

math = ege3[0:2]
print(math)
