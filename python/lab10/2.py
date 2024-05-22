import sys


def get_word2():
    max_attempts = 5
    for i in range(max_attempts):
        word = input("Введите слово: ")
        if word.isalpha():
            return word
        else:
            print("Ошибка ввода!")
    print(f"Выполнено {max_attempts} неудачных попыток ввода. Выход из программы.")
    sys.exit()


print(get_word2())
