my_list = ["победа", "ничья", "поражение"]
print(type(my_list))
print(len(my_list))
print(my_list[1])

print("---------------------------")

print(id(my_list[0]))
print(id(my_list[1]))
print(id(my_list[2]))

print("2a  ---------------------------")

list2 = []
print(type(list2))
print(len(list2))

print("2б  ---------------------------")

print("не пустой" if [] else "пустой")

print("2в  ---------------------------")

list3 = [[], []]
print(type(list3))
print(len(list3))
print(id(list3))
print(id(list3[0]))
print(id(list3[1]))
