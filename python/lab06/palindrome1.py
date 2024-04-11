def get_word():
    word = input("Введите слово: ")
    return word


def is_palindrome(word):
    return "палиндром" if word == word[::-1] else "не палиндром"


def create_message(word, what_is):
    print('Слово %s - %s' % (word, what_is))


def check_palindrome():
    word = get_word()
    what_is = is_palindrome(word)
    create_message(word, what_is)


check_palindrome()
