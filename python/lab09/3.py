ege1 = "Математика                 - 78,                      Информатика -      75,  Русский язык      -      62"


def convert_list14(ege: str):
    out = []
    out2 = []
    for elem in ege.split(','):
        out.append(elem)
    for elem in out:
        elem_sub = elem.split(' - ')[0].strip()
        elem_mark = int(elem.split(' - ')[1].strip())
        out2.append(elem_sub)
        out2.append(elem_mark)
    return out2


print(convert_list14(ege1))
