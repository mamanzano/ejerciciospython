# -*- coiding: utf-8 -*-

def palindrome(word):

    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0,letter)

    reversed_word = ''.join(reversed_letters)

    if reversed_word == word:
        return True
    else:
        return False


if __name__ == "__main__":
    word = str(input('Ingresa una palabra: '))
    result = palindrome(word)
    if result:
        print('la palabra {} es un palíndromo'.format(word))
    else:
        print('la palabra {} no es un palíndromo'.format(word))