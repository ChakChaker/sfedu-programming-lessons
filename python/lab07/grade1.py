def grade1(mark):
    print('Вузовский эквивалент вашей оценки: ')
    if mark == 5:
        print('Отлично')
    elif mark == 4:
        print('Хорошо')
    elif mark == 3:
        print('Удовлетворительно')
    elif mark == 2:
        print('Неудовлетворительно')
    else:
        print('Неверный формат оценки.')


grade1(int(input('Введите школьную оценку: ')))
