ege2 = ["Математика - 78", "Информатика - 75", "Русский язык - 62"]
lst3, lst4 = [], []


def get_info(string):
    ege = string.split(' - ')
    return [ege[0], int(ege[1])]


for element in ege2:
    info = get_info(element)
    lst3.append(info[0])
    lst3.append(info[1])
    lst4.append([info[0], info[1]])


def subjects(ege):
    out = []
    for elem in ege:
        out.append(elem.split(' - ')[0])
    return out


def marks(ege):
    out = []
    for elem in ege:
        out.append(int(elem.split(' - ')[1]))
    return out


def print_results(sub, mark):
    for i in range(len(sub)):
        print(f'{sub[i]} - {mark[i]}')
    print(f'суммарные баллы: {sum(mark)}')


print('  list3-4:')
print(lst3)
print(lst4)

print()
print('  subjects-marks:')
lst3 = subjects(ege2)
lst4 = marks(ege2)
print(lst3)
print(lst4)

print()
print('  print_results:')
print_results(lst3, lst4)
