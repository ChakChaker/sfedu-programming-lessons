def get_word1():
    no_data = True
    while no_data:
        word = input("Введите слово: ")
        if word.isalpha():
            no_data = False
            return word
        else:
            print("Ошибка ввода!")


print(get_word1())
