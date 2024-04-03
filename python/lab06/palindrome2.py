
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
    get_word()
    is_palindrome()
    answer = 'Слово %s - %s' % (word, what_is)
    print(answer)


create_message()
