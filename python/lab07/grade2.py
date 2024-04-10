def grade2(mark):
    if mark < 0 or mark > 100:
        print('Неверный формат оценки.')
    elif mark < 60:
        print('Неудовлетворительно')
    elif mark < 71:
        print('Удовлетворительно')
    elif mark < 85:
        print('Хорошо')
    else:
        print('Отлично')


grade2(int(input('Введите баллы: ')))
