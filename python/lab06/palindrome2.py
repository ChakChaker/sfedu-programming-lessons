
def get_word():
    global word
    word = input("Введите слово: ")


def is_palindrome():
    global what_is
    if word == word[::-1]:
        what_is = "палиндром"
    else:
        what_is = "не палиндром"


def create_message():
    print('Слово %s - %s' % (word, what_is))


def check_palindrome():
    get_word()
    is_palindrome()
    create_message()


check_palindrome()
