def get_word():
    word = input("Введите слово: ")
    return word


def is_palindrome(word):
    if word == word[::-1]:
        return "палиндром"
    else:
        return "не палиндром"


def create_message():
    word = get_word()
    what_is = is_palindrome(word)
    answer = 'Слово %s - %s' % (word, what_is)
    print(answer)


create_message()
