ege1 = 'Математика - 78, информатика - 75, русский язык - 62'
subjects = ['Математика', 'Информатика', 'Физика', 'Фехтование']


def get_tested(ege: str, subject: str):
    return True if ege.lower().find(subject.lower()) != -1 else False


for elem in subjects:
    print(f'Егэ по {elem} сдан' if get_tested(ege1, elem) else f'Егэ по {elem} не сдан')
