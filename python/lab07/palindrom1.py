import sys


def get_word():
    word = input("Введите слово: ")
    if not word.isalpha():
        print('Ошибка ввода!!!')
        sys.exit()
    else:
        return word


def is_palindrome_old(word):
    return "палиндром" if word == word[::-1] else "не палиндром"


def is_palindrome(word):
    return word.lower() == word.lower()[::-1]


def create_message(word, prefix):
    print('Слово %s - %s палиндром' % (word, prefix))


def check_palindrome():
    word = get_word()
    prefix = '' if is_palindrome(word) else 'не'
    create_message(word, prefix)


check_palindrome()
