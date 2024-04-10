import sys


def get_word():
    word = input("Введите слово: ")
    if not word.isalpha():
        print('Ошибка ввода!!!')
        sys.exit()
    else:
        return word


def is_palindrome_old(word):
    if word == word[::-1]:
        return "палиндром"
    else:
        return "не палиндром"


def is_palindrome(word):
    word_lower = word.lower()
    return word_lower == word_lower[::-1]


def create_message():
    word = get_word()
    prefix = '' if is_palindrome(word) else 'не'
    answer = 'Слово %s - %s палиндром' % (word, prefix)
    print(answer)


create_message()
